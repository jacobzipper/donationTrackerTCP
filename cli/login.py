import click
import requests
from __init__ import API_URL

CONTEXT_SETTINGS = dict(help_option_names = ['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('username')
@click.argument('password')
def login(username, password):
    """This command logs you into the service for this session

    POST to rest service with <username> <password>"""
    r = requests.post(API_URL + '/login', data = {'username': username, 'password': password})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('Welcome to Donation Tracker %s %s! You are a %s.' % (js['firstname'], js['lastname'], js['role'][:len(js['role']) - 1]))
        click.echo(str(js))

