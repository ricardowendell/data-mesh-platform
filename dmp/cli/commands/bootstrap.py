import click

import dmp.platform.bootstrap as bootstrap


@click.command()
def cli():
    """Bootstrap Data Mesh Platform"""
    bootstrap.run()
