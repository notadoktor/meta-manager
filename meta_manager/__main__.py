#!/usr/bin/env python3

from pathlib import Path

# lazy dev import
if (Path(__file__).parents[1] / ".venv").exists():
    import sys

    sys.path.insert(0, str(Path(__file__).parents[1]))

from meta_manager import MetaManager
from meta_manager.util import DbFormat
from typer import BadParameter, Option, Typer, echo

app = Typer()
DB_FILENAME = "mm_metadata"

tags_opt: list[str] = Option("tags", help="Comma-separated list of tags to add")
attrs_opt: list[dict[str, str]] = Option(
    "attrs", help="Comma-separated list of key=value pairs to add"
)
files_opt: list[Path] = Option("files", help="Comma-separated list of files to add")

###


def comma_list(value: str, *, val_type: type = str) -> list[str]:
    return value.split(",")


###


@app.command()
def add(file: list[Path], *, tags=tags_opt, attrs=attrs_opt):
    """Add a new file to the database."""
    echo(f"Adding {file} to the database.")


@app.command()
def init(*, root: Path = Path(), fmt: str = "json"):
    """Initialize the database."""
    try:
        db_fmt = DbFormat[fmt.upper()]
    except KeyError:
        raise BadParameter(f"Unsupported database format: {fmt}")
    db_file = root.resolve() / f"{DB_FILENAME}.{db_fmt}"
    mgr = MetaManager(db_file)
    mgr.save()
    echo(f"Initial database created at {db_file}")


@app.command()
def set_tags(names=tags_opt, files=files_opt):
    """Add a tag to file(s)"""
    echo(f"Adding tag to {files}.")


@app.command()
def show_file(file: Path):
    """Shows details for the given file"""
    echo("Searching for files.")


@app.command("list")
def list_files():
    """List all files in the database."""
    echo("Listing all files.")


if __name__ == "__main__":
    app()
