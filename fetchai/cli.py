#!/usr/bin/env python3

import os
import click
from dotenv import load_dotenv, set_key, dotenv_values
from cli import env, identity, readme, register

# Load environment variables from .env file
load_dotenv()


@click.group()
def cli():
    """CLI tool for AgentVerse registration and identity management."""
    pass

cli.add_command(readme)
cli.add_command(identity)
cli.add_command(register)




if __name__ == "__main__":
    cli()
