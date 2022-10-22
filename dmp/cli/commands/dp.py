import json

import click
from dacite import from_dict

import dmp.platform.dataproduct as dp


@click.group()
def cli():
    """Data Product Experience Plane commands"""


@cli.command()
def init():
    click.echo("Initializing Data Product...")


@cli.command()
@click.option("--spec", type=click.Path(exists=True), prompt="Your spec file")
def create(spec):
    specification = read_specification(spec)
    results = dp.create(specification)
    click.echo(results)


def read_specification(filename):
    with open(filename) as json_file:
        spec = json.load(json_file)
        return from_dict(data_class=dp.DataProductSpecification, data=spec)
