import os

import click


class DataMeshPlaftormCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "commands")
        )
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename != "__init__.py":
                commands.append(filename.replace(".py", ""))

        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            command_module = f"dmp.cli.commands.{name}"
            module = __import__(command_module, None, None, ["cli"])
        except ImportError:
            return
        return module.cli


@click.command(cls=DataMeshPlaftormCLI)
def cli():
    """Welcome to the Data Mesh Platform CLI"""
