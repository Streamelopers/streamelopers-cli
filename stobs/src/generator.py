import os
import json
import click

from stobs.config import ConfigOBS


def create_file(data, name):
    click.echo(click.style('Creating config file of scenes collection...'))

    if not os.path.isdir(f'{ConfigOBS.HOME}/stobs'):
        os.mkdir(f'{ConfigOBS.ConfigOBS.HOME}/stobs')

    with open(f'{ConfigOBS.HOME}/stobs/{name}.json', 'w') as _file:
        _file.write(data)

    click.echo(click.style('Created!', fg='green'))

def parser_values(data, name):
    data['name'] = name

    return data

def _generator(name):
    data = parser_values(ConfigOBS.TEMPLATE, name)
    data = json.dumps(data, indent=4)

    create_file(data, name)