import click
import requests
from __init__ import API_URL

CONTEXT_SETTINGS = dict(help_option_names = ['-h', '--help'])

DONATION_FORMAT = """
NAME:    %s
LCID:    %d
TSTP:    %s
SDSC:    %s
DSCR:    %s
CMTS:    %s
VALU:    %s
CATG:    %s
"""

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('jwt')
@click.argument('location', nargs = -1)
def userget(jwt, location):
    """This command gets all donations at <location> (name of location) from the service"""
    location = ' '.join(location)
    r = requests.get(API_URL + '/users/searchdonations', params = {'location': location}, headers = {'Authorization': 'Bearer ' + jwt})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('\n'.join(map(lambda x: DONATION_FORMAT % (x['name'], x['locationid'], x['tstamp'], x['shortdescription'], x['description'], x['comments'], x['value'], x['category']), js['donations'])))

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('jwt')
@click.argument('location', nargs = -1)
def employeeget(jwt, location):
    """This command gets all donations at <location> (name of location) from the service"""
    location = ' '.join(location)
    r = requests.get(API_URL + '/employees/searchdonations', params = {'location': location}, headers = {'Authorization': 'Bearer ' + jwt})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('\n'.join(map(lambda x: DONATION_FORMAT % (x['name'], x['locationid'], x['tstamp'], x['shortdescription'], x['description'], x['comments'], x['value'], x['category']), js['donations'])))

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('jwt')
@click.argument('location', nargs = -1)
def managerget(jwt, location):
    """This command gets all donations at <location> (name of location) from the service"""
    location = ' '.join(location)
    r = requests.get(API_URL + '/managers/searchdonations', params = {'location': location}, headers = {'Authorization': 'Bearer ' + jwt})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('\n'.join(map(lambda x: DONATION_FORMAT % (x['name'], x['locationid'], x['tstamp'], x['shortdescription'], x['description'], x['comments'], x['value'], x['category']), js['donations'])))

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('jwt')
@click.argument('location', nargs = -1)
def adminget(jwt, location):
    """This command gets all donations at <location> (name of location) from the service"""
    location = ' '.join(location)
    r = requests.get(API_URL + '/managers/searchdonations', params = {'location': location}, headers = {'Authorization': 'Bearer ' + jwt})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('\n'.join(map(lambda x: DONATION_FORMAT % (x['name'], x['locationid'], x['tstamp'], x['shortdescription'], x['description'], x['comments'], x['value'], x['category']), js['donations'])))



@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('jwt')
@click.argument('name', default = None, nargs = -1)
def usersearch(jwt, category, name):
    """This command searches for donations using fuzzy match on <name> and exact match on <category> from the service"""
    if name:
        name = ' '.join(name)
    if category:
        name = ' '.join(name)
    r = requests.get(API_URL + '/users/searchdonations', params = {'category': category, 'name': name}, headers = {'Authorization': 'Bearer ' + jwt})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('\n'.join(map(lambda x: DONATION_FORMAT % (x['name'], x['locationid'], x['tstamp'], x['shortdescription'], x['description'], x['comments'], x['value'], x['category']), js['donations'])))

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('jwt')
@click.option('--category', '-c', default = None)
@click.argument('name', default = None, nargs = -1)
def employeesearch(jwt, category, name):
    """This command searches for donations using fuzzy match on <name> and exact match on <category> from the service"""
    if name:
        name = ' '.join(name)
    if category:
        name = ' '.join(name)
    r = requests.get(API_URL + '/employees/searchdonations', params = {'category': category, 'name': name}, headers = {'Authorization': 'Bearer ' + jwt})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('\n'.join(map(lambda x: DONATION_FORMAT % (x['name'], x['locationid'], x['tstamp'], x['shortdescription'], x['description'], x['comments'], x['value'], x['category']), js['donations'])))

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('jwt')
@click.option('--category', '-c', default = None)
@click.argument('name', default = None, nargs = -1)
def managersearch(jwt, category, name):
    """This command searches for donations using fuzzy match on <name> and exact match on <category> from the service"""
    if name:
        name = ' '.join(name)
    if category:
        name = ' '.join(name)
    r = requests.get(API_URL + '/managers/searchdonations', params = {'category': category, 'name': name}, headers = {'Authorization': 'Bearer ' + jwt})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('\n'.join(map(lambda x: DONATION_FORMAT % (x['name'], x['locationid'], x['tstamp'], x['shortdescription'], x['description'], x['comments'], x['value'], x['category']), js['donations'])))

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('jwt')
@click.option('--category', '-c', default = None)
@click.argument('name', default = None, nargs = -1)
def adminsearch(jwt, category, name):
    """This command searches for donations using fuzzy match on <name> and exact match on <category> from the service"""
    if name:
        name = ' '.join(name)
    if category:
        category = ' '.join(category)
    r = requests.get(API_URL + '/admins/searchdonations', params = {'category': category, 'name': name}, headers = {'Authorization': 'Bearer ' + jwt})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('\n'.join(map(lambda x: DONATION_FORMAT % (x['name'], x['locationid'], x['tstamp'], x['shortdescription'], x['description'], x['comments'], x['value'], x['category']), js['donations'])))


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('jwt')
@click.argument('name')
@click.argument('shortdescription')
@click.argument('description')
@click.argument('value', type = int)
@click.argument('category', type = click.Choice(['Clothing', 'Household', 'Hat', 'Other', 'Electronics']))
def employeeadd(jwt, name, shortdescription, description, value, category):
    """This command adds a donation to the service"""
    category = category[0].upper() + category[1:]
    r = requests.post(API_URL + '/employees/adddonation', data = {'category': category, 'name': name, 'shortdescription': shortdescription, 'description': description, 'value': value}, headers = {'Authorization': 'Bearer ' + jwt})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('Successfully added your donation to your location!')

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('jwt')
@click.argument('name')
@click.argument('shortdescription')
@click.argument('description')
@click.argument('value', type = int)
@click.argument('category', type = click.Choice(['Clothing', 'Household', 'Hat', 'Other', 'Electronics']))
def manageradd(jwt, name, shortdescription, description, value, category):
    """This command adds a donation to the service"""
    category = category[0].upper() + category[1:]
    r = requests.post(API_URL + '/managers/adddonation', data = {'category': category, 'name': name, 'shortdescription': shortdescription, 'description': description, 'value': value}, headers = {'Authorization': 'Bearer ' + jwt})
    js = r.json()
    if js['error'] != 0:
        click.echo(js['msg'])
    else:
        click.echo('Successfully added your donation to your location!')