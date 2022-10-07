from pathlib import Path
from typing import Optional

from meta_manager.db import DatabaseFile
from meta_manager.classes import DbFormat, MetaFile


class MetaManager:
    db: DatabaseFile

    def __init__(self, db: Path):
        try:
            db_format = DbFormat(db.suffix)
        except ValueError:
            raise ValueError(f"Unsupported database format: {db.suffix}")

        self.db = DatabaseFile.load_file(db, db_format)

    @property
    def root(self):
        return self.db.root

    def save(self):
        self.db.save_data()

    def add_file(
        self,
        file: Path,
        *,
        tags: Optional[set[str]] = None,
        attrs: Optional[dict[str, str]] = None,
    ) -> MetaFile:
        ...

    def add_tags(self, files: set[Path], tags: set[str]) -> MetaFile:
        ...

    def add_attrs(self, files: set[Path], attrs: dict[str, str]) -> MetaFile:
        ...

    def list_files(self, *, filter=None):
        ...

    def get_data(self, file: Path) -> MetaFile:
        ...

    def clear_data(self, file: Path, *, delete_file: bool = False) -> None:
        ...

    def fetch_file(self, url: str, *, filename: Optional[str] = None) -> Path:
        ...
