from __future__ import annotations

import datetime
from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path
from typing import Optional

import toml
import yaml
from pydantic import BaseModel, Field

from meta_manager.util import hash_data, hash_file


class DbFormat(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    def __str__(self) -> str:
        return self.value[1:]

    JSON = ".json"
    YAML = ".yaml"
    TOML = ".toml"


class MetaFile(BaseModel):
    path: str
    md5: str
    source: Optional[str] = None
    date_added: datetime.datetime = Field(default_factory=datetime.datetime.now)
    tags: set[str] = Field(default_factory=set)
    attrs: dict[str, str] = Field(default_factory=dict)


class MetaDatabase(BaseModel):
    files: dict[Path, MetaFile] = Field(default_factory=dict)
    date_created: datetime.datetime = Field(default_factory=datetime.datetime.now)
    last_modified: datetime.datetime = Field(default_factory=datetime.datetime.now)
    description: Optional[str] = None


class DatabaseFile(ABC):
    path: Path
    db_format: DbFormat
    data: MetaDatabase

    def __init__(self, path: Path, db_format: DbFormat) -> None:
        self.path = path.resolve()
        self.db_format = db_format
        self.load_data()

    @property
    def root(self):
        return self.path.parent

    def exists(self):
        return self.path.exists()

    @staticmethod
    def load_file(path: Path, db_format: DbFormat):
        if db_format == DbFormat.JSON:
            return JsonDatabase(path, db_format)
        elif db_format == DbFormat.YAML:
            return YamlDatabase(path, db_format)
        elif db_format == DbFormat.TOML:
            return TomlDatabase(path, db_format)
        else:
            raise ValueError(f"No loader defined for format: {db_format}")

    def load_data(self):
        if self.path.exists():
            self.data = self._read()
        else:
            self.data = MetaDatabase()

    def save_data(self):
        new_data = self._serialize().encode("utf-8")
        if not new_data.endswith(b"\n"):
            new_data += b"\n"

        if self.path.exists():
            if hash_data(new_data) == hash_file(self.path):
                print("Database unchanged, no data written")
                return

        self.path.write_bytes(new_data)

    @abstractmethod
    def _read(self) -> MetaDatabase:
        ...

    @abstractmethod
    def _serialize(self) -> str:
        ...


class JsonDatabase(DatabaseFile):
    def _read(self) -> MetaDatabase:
        return MetaDatabase.parse_file(self.path)

    def _serialize(self):
        return self.data.json(indent=2, sort_keys=True)


class YamlDatabase(DatabaseFile):
    def _read(self) -> MetaDatabase:
        return MetaDatabase.parse_obj(yaml.safe_load(self.path.read_text()))

    def _serialize(self):
        return yaml.safe_dump(self.data.dict())


class TomlDatabase(DatabaseFile):
    def _read(self) -> MetaDatabase:
        return MetaDatabase.parse_obj(toml.loads(self.path.read_text()))

    def _serialize(self):
        return toml.dumps(self.data.dict())
