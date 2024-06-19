from typing import Annotated
import typer

version = "0.1.0"

help_text = f"""
fhash version {version}
Append hash to file name

"""


app = typer.Typer(help=help_text, no_args_is_help=True)
###############################################################################


@app.command()
def main(file: Annotated[str, typer.Argument(help="File to hash")] = None):
    print(help_text)

    if not file:
        typer.echo("No file specified", color=typer.colors.RED)
        raise typer.Exit(code=1)


###############################################################################
if __name__ == "__main__":
    app()
