from pathlib import Path
import typer


class Check:

    @classmethod
    def file_defined(cls, filename: str):
        if not filename:
            typer.secho("No file specified", fg=typer.colors.RED)
            raise typer.Exit(code=1)

    @classmethod
    def file_exists(cls, file: Path):
        if not file.exists():
            typer.secho(f"File {file} not found", fg=typer.colors.RED)
            raise typer.Exit(code=1)

    @classmethod
    def algoritm_supported(cls, algorithm: str, algorithms: list[str]):
        if algorithm not in algorithms:
            typer.secho(f"Algorithm {algorithm} not supported", fg=typer.colors.RED)
            raise typer.Exit(code=1)
