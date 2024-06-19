from typing import Annotated
import typer

FileArg = Annotated[str, typer.Argument(help="File to hash")]

AlgorithmOpt = Annotated[
    str,
    typer.Option(
        "--algorithm",
        "-a",
        help="Algorithm to use [md5, sha1, sha256, sha512]",
        case_sensitive=False,
        show_default=True,
    ),
]
