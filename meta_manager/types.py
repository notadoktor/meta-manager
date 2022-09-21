import datetime
from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field


class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class DbFormat(StrEnum):
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
