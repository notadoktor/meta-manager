#!/usr/bin/env python3

from pathlib import Path

from typer import BadParameter, Context, Option, Typer, echo

from meta_manager import MetaManager
from meta_manager.classes import DbFormat
from meta_manager.util import comma_list

app = Typer(add_completion=False)
DB_FILENAME = ".mm.metadata"
DEFAULT_FORMAT = DbFormat.JSON
DEFAULT_FILENAME = f"{DB_FILENAME}.{DEFAULT_FORMAT}"

TAGS_OPT = Option([], help="Comma-separated list of tags to add", callback=comma_list)
ATTRS_OPT = Option([], help="Comma-separated list of key=value pairs to add", callback=comma_list)
FILES_OPT = Option([], help="Comma-separated list of files to add", callback=comma_list)


###


@app.callback()
def init_context(ctx: Context):
    for fmt in DbFormat:
        db_file = Path(f"{DB_FILENAME}.{fmt}")
        if db_file.exists():
            ctx.obj = MetaManager(db_file)
            return
    ctx.obj = MetaManager(Path(DEFAULT_FILENAME))


@app.command()
def add(
    ctx: Context,
    file: list[str],
    tags: list[str] = TAGS_OPT,
    attrs: list[str] = ATTRS_OPT,
):
    """Add a new file to the database."""
    echo(f"Adding {file} to the database.")


@app.command()
def init(ctx: Context, root: Path = Path(), fmt: str = "json"):
    """Initialize the database."""
    try:
        db_fmt = DbFormat[fmt.upper()]
    except KeyError:
        raise BadParameter(f"Unsupported database format: {fmt}")

    db_file = root.resolve() / f"{DB_FILENAME}.{db_fmt}"
    if db_file.exists():
        echo(f"Database already exists at {db_file}, not initializing.")
        return

    mgr = MetaManager(db_file)
    mgr.save()
    echo(f"Initial database created at {db_file.relative_to(Path().resolve())}")


@app.command()
def set_tags(ctx: Context, names: list[str] = TAGS_OPT, files: list[Path] = FILES_OPT):
    """Add a tag to file(s)"""
    echo(f"Adding tag to {files}.")


@app.command()
def show_file(ctx: Context, file: Path):
    """Shows details for the given file"""
    echo("Searching for files.")


@app.command("list")
def list_files(ctx: Context):
    """List all files in the database."""
    echo("Listing all files.")


if __name__ == "__main__":
    breakpoint()
    app()
