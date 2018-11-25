import click
import requests
from __init__ import API_URL

CONTEXT_SETTINGS = dict(help_option_names = ['-h', '--help'])

GMAPS_FORMAT = 'https://www.google.com/maps/dir/?api=1&origin=%s&destination=%s&travelmode=driving&waypoints=%s'

@click.command(context_settings=CONTEXT_SETTINGS)
def maps():
    """This command gets all locations from the service"""
    r = requests.get(API_URL + '/locations')
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        locs = map(lambda x: x['address'], js['locations'])
        origin = locs.pop(0)
        dest = locs.pop()
        waypoints = '|'.join(locs)
        click.echo(GMAPS_FORMAT % (origin, dest, waypoints))

