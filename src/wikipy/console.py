import textwrap

import click
import requests

from . import __version__

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
@click.argument("title_arg", required=False)
def main(title_arg):
    """The wikipy project."""
    if title_arg:
        with requests.get(
            f"https://en.wikipedia.org/api/rest_v1/page/summary/{title_arg}"
        ) as response:
            response.raise_for_status()
            data = response.json()

    else:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            data = response.json()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
