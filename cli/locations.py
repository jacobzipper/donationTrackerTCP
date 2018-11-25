import click
import requests
from __init__ import API_URL

CONTEXT_SETTINGS = dict(help_option_names = ['-h', '--help'])

LOCATION_FORMAT = """
NAME:    %s
TYPE:    %s
LATD:    %f
LONG:    %f
ADDR:    %s
PHNE:    %s
"""

@click.command(context_settings=CONTEXT_SETTINGS)
def locations():
    """This command gets all locations from the service"""
    r = requests.get(API_URL + '/locations')
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('\n'.join(map(lambda x: LOCATION_FORMAT % (x['name'], x['type'], x['latitude'], x['longitude'], x['address'], x['phone']), js['locations'])))

