from pathlib import Path
from typing import Optional

from meta_manager.db import DatabaseFile, DbFormat, MetaFile


class MetaManager:
    db_file: DatabaseFile

    def __init__(self, db: Path):
        try:
            db_format = DbFormat(db.suffix[1:])
        except ValueError:
            raise ValueError(f"Unsupported database format: {db.suffix}")

        self.db_file = DatabaseFile.load_file(db, db_format)

    @property
    def db(self):
        return self.db_file.data

    @property
    def last_modified(self):
        return self.db.last_modified

    @property
    def date_created(self):
        return self.db.date_created

    @property
    def description(self):
        return self.db.description

    @property
    def root(self):
        return self.db_file.root

    def save(self):
        self.db_file.save_data()

    def add_file(
        self,
        file: Path,
        *,
        tags: Optional[set[str]] = None,
        attrs: Optional[dict[str, str]] = None,
    ) -> MetaFile:
        raise NotImplementedError()

    def add_tags(self, files: set[Path], tags: set[str]) -> MetaFile:
        raise NotImplementedError()

    def add_attrs(self, files: set[Path], attrs: dict[str, str]) -> MetaFile:
        raise NotImplementedError()

    def list_files(self, *, filter=None):
        return self.db.files.values()

    def get_data(self, file: Path) -> MetaFile:
        raise NotImplementedError()

    def clear_data(self, file: Path, *, delete_file: bool = False) -> None:
        raise NotImplementedError()

    def fetch_file(self, url: str, *, filename: Optional[str] = None) -> Path:
        raise NotImplementedError()
