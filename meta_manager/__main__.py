#!/usr/bin/env python3

from pathlib import Path

from typer import BadParameter, Context, Option, Typer, echo

from meta_manager import MetaManager
from meta_manager.util import comma_list
from meta_manager.db import DbFormat

app = Typer(add_completion=False)
DB_FILENAME = ".mm.metadata"
DEFAULT_FORMAT = DbFormat.JSON
DEFAULT_FILENAME = f"{DB_FILENAME}.{DEFAULT_FORMAT}"

TAGS_OPT = Option([], help="Comma-separated list of tags", callback=comma_list)
ATTRS_OPT = Option([], help="Comma-separated list of key=value pairs", callback=comma_list)
FILES_OPT = Option([], help="Comma-separated list of files", callback=comma_list)

###


class AppContext(Context):
    obj: MetaManager


###


@app.callback()
def init_context(ctx: AppContext):
    for fmt in DbFormat:
        db_file = Path(f"{DB_FILENAME}.{fmt}")
        if db_file.exists():
            ctx.obj = MetaManager(db_file)
            return
    ctx.obj = MetaManager(Path(DEFAULT_FILENAME))


@app.command("init")
def init_db_file(
    ctx: AppContext,
    fmt: DbFormat = Option(DbFormat.JSON, help="Database format", show_default=True),
):
    """Initialize the database."""
    if ctx.obj.db_file.db_format != fmt:
        ctx.obj = MetaManager(ctx.obj.db_file.root / f"{DB_FILENAME}.{fmt}")

    if ctx.obj.db_file.exists:
        echo(f"Database already exists at {ctx.obj.db_file.path}, not initializing.")
    else:
        ctx.obj.save()
        echo(f"Initial database created at {ctx.obj.db_file.path.name}")


@app.command()
def add(
    ctx: AppContext,
    file: Path,
    tags: list[str] = TAGS_OPT,
    attrs: list[str] = ATTRS_OPT,
):
    """Add a new file to the database."""
    echo(f"Adding {file} to the database.")
    raise NotImplementedError()


@app.command()
def update(
    ctx: AppContext,
    file: Path,
    tags: list[str] = TAGS_OPT,
    attrs: list[str] = ATTRS_OPT,
):
    """Update an existing file in the database."""
    echo(f"Updating {file} in the database.")
    raise NotImplementedError()


@app.command()
def show_file(ctx: AppContext, file: Path):
    """Shows details for the given file"""
    echo("Searching for files.")
    raise NotImplementedError()


@app.command("list")
def list_files(ctx: AppContext):
    """List all files in the database."""
    files = ctx.obj.list_files()
    if files:
        echo("Files:")
        for file in files:
            echo(f"  {file}")
    else:
        echo("No files in the database.")


@app.command("info")
def show_info(ctx: AppContext):
    """Show database information."""
    if ctx.obj.db_file.path.exists():
        echo(f"Database: {ctx.obj.db_file.path.name}")
        if ctx.obj.description:
            echo(f"Description: {ctx.obj.description}")
        echo(f"Created:  {ctx.obj.date_created}")
        echo(f"Modified: {ctx.obj.last_modified}")
        echo(f"Files: {len(ctx.obj.db.files)}")
    else:
        echo("No database found.")


if __name__ == "__main__":
    app()
