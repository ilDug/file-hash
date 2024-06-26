from pathlib import Path
import shutil
import typer

from modules import FileArg, AlgorithmOpt, Check, hash_file, name_file, detect_algorithm

version = "0.2.0"

help_text = f"""
fhash version {version}
File Haseher Utils

"""

algorithms = ["md5", "sha1", "sha256", "sha512"]

app = typer.Typer(help=help_text, no_args_is_help=True)
###############################################################################


def parse_input(file: str, algorithm: str) -> tuple[str, Path, str]:
    Check.file_defined(file)
    path = Path(file)
    Check.file_exists(path)
    Check.algoritm_supported(algorithm, algorithms)
    hash = hash_file(path, algorithm)
    new_name = name_file(path, hash)

    return hash, path, new_name


@app.command()
def hash(
    file: FileArg = None,
    algorithm: AlgorithmOpt = "md5",
):
    """calcola l'hash di un file e lo mostra al terminale"""
    (hash, _, _) = parse_input(file, algorithm)
    typer.echo(f"file-hash [{algorithm}]: {hash}")


@app.command()
def rename(
    file: FileArg = None,
    algorithm: AlgorithmOpt = "md5",
):
    """rinomina il file aggiungendo l'hash al nome"""
    (_, path, new_name) = parse_input(file, algorithm)
    res = path.rename(new_name)
    typer.echo(f"File renamed: {res.absolute()}")


@app.command()
def copy(
    file: FileArg = None,
    algorithm: AlgorithmOpt = "md5",
):
    """copia il file con il nome modificato"""
    (_, path, new_name) = parse_input(file, algorithm)
    shutil.copy2(str(path), new_name)
    typer.echo(f"File copied: {Path(new_name).absolute()}")


@app.command()
def verify(file: FileArg = None):
    """verifica che il file corrisponda all'hash contenuto nel nome"""
    Check.file_defined(file)
    path = Path(file)
    Check.file_exists(path)
    fingerprint = path.stem.split(".[")[-1]
    fingerprint = fingerprint.split("]")[0]
    algorithm = detect_algorithm(fingerprint)
    hash = hash_file(path, algorithm)
    res = hash == fingerprint
    if res:
        typer.secho(f"File {path} verified", fg=typer.colors.GREEN)
    else:
        typer.secho(f"File {path} not verified", fg=typer.colors.RED)


@app.callback()
def callback():
    typer.secho(help_text, fg=typer.colors.BRIGHT_BLACK)


###############################################################################
if __name__ == "__main__":
    app()
