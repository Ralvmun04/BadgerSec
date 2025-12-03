import typer

from .banner import get_banner
from .scan import port_scanner
from .colors import ROSA, RESET
from .logger import logger

app = typer.Typer(help="BadgerSec — Persistence Penetration Testing Tool")

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print(get_banner())
        print("\nWelcome to BadgerSec, Persistence Penetration Testing Tool")
        print("Use -h or --help to list the existing commands.\n")
        logger.info("BadgerSec started")
        raise typer.Exit()

@app.command()
def scan(target: str):
    print(get_banner())
    print(f"Scanning {ROSA}{target}{RESET}...\n")
    logger.info(f"Scanning {target} for open TCP ports...")

    puertos_abiertos = port_scanner.scan_tcp_ports(target)


    if puertos_abiertos:
        print("\nOpen ports found:", puertos_abiertos)
        logger.info(f"Open ports found in {target}: {puertos_abiertos}")
    else:
        print("\nNo open ports found.")


if __name__ == "__main__":
    app()
