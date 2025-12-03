import click
from .banners import BANNER
from .scanner import scan_target

@click.group()
def cli():
    print(BANNER)

@cli.command()
@click.argument("target")
def scan(target):
    scan_target(target)
