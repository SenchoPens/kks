import sys

import click

from kks.util.compat import subprocess


@click.command()
@click.argument('args', nargs=-1)
def upgrade(args):
    """Runs "pip install --upgrade kokos" """
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'kokos'] + list(args))


@click.command()
@click.argument('args', nargs=-1)
def update(args):
    """Runs "pip install --upgrade kokos" """
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'kokos'] + list(args))
