import click
import requests
from __init__ import API_URL

CONTEXT_SETTINGS = dict(help_option_names = ['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('role', default = 'users', type = click.Choice(['users', 'employees', 'managers', 'admins']))
@click.argument('username')
@click.argument('password')
@click.argument('firstname', default = '')
@click.argument('lastname', default = '')
def register(role, username, password, firstname, lastname):
    """This command registers you into the service as a <role>

    <role> can be one of users, employees, managers, or admins

    POST to rest service with <role> <username> <password> and optionally <firstname> <lastname>"""
    r = requests.post(API_URL + '/registration', data = {'role': role, 'username': username, 'password': password, 'firstname': firstname, 'lastname': lastname})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('Welcome to Donation Tracker! You may now log in.')

