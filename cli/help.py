import click
import __init__ as cli

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

allCmds = {
    'guests': [
        ('help', 'DISPLAY THIS HELP'),
        ('login', 'LOGIN TO THE SERVICE'),
        ('register', 'REGISTER WITH THE SERVICE'),
        ('locations', 'GET LOCATIONS FROM THE SERVICE'),
        ('map', 'GET A MAP LINK FROM THE SERVICE'),
        ('end', 'END CONNECTION TO DONATION TRACKER TELNET')
    ],
    'users': [
        ('help', 'DISPLAY THIS HELP'),
        ('locations', 'GET LOCATIONS FROM THE SERVICE'),
        ('map', 'GET A MAP LINK FROM THE SERVICE'),
        ('getdonations', 'GET DONATIONS FROM THE SERVICE'),
        ('searchdonations', 'SEARCH DONATIONS FROM THE SERVICE'),
        ('logout', 'LOGOUT FROM THE SERVICE'),
        ('end', 'END CONNECTION TO DONATION TRACKER TELNET')
    ],
    'employees': [
        ('help', 'DISPLAY THIS HELP'),
        ('locations', 'GET LOCATIONS FROM THE SERVICE'),
        ('map', 'GET A MAP LINK FROM THE SERVICE'),
        ('getdonations', 'GET DONATIONS FROM THE SERVICE'),
        ('searchdonations', 'SEARCH DONATIONS FROM THE SERVICE'),
        ('logout', 'LOGOUT FROM THE SERVICE'),
        ('end', 'END CONNECTION TO DONATION TRACKER TELNET')
    ],
    'managers': [
        ('help', 'DISPLAY THIS HELP'),
        ('locations', 'GET LOCATIONS FROM THE SERVICE'),
        ('map', 'GET A MAP LINK FROM THE SERVICE'),
        ('getdonations', 'GET DONATIONS FROM THE SERVICE'),
        ('searchdonations', 'SEARCH DONATIONS FROM THE SERVICE'),
        ('logout', 'LOGOUT FROM THE SERVICE'),
        ('end', 'END CONNECTION TO DONATION TRACKER TELNET')
    ],
    'admins': [
        ('help', 'DISPLAY THIS HELP'),
        ('locations', 'GET LOCATIONS FROM THE SERVICE'),
        ('map', 'GET A MAP LINK FROM THE SERVICE'),
        ('getdonations', 'GET DONATIONS FROM THE SERVICE'),
        ('searchdonations', 'SEARCH DONATIONS FROM THE SERVICE'),
        ('logout', 'LOGOUT FROM THE SERVICE'),
        ('end', 'END CONNECTION TO DONATION TRACKER TELNET')
    ]
}

@click.command(context_settings=CONTEXT_SETTINGS)
def helpguests():
    """This command shows all the valid commands and a short description of them"""
    click.echo('Here are all the commands\n')
    click.echo('\n'.join(map(lambda x: '\t' + x[0] + ' ' + x[1], allCmds['guests'])))


@click.command(context_settings=CONTEXT_SETTINGS)
def helpusers():
    """This command shows all the valid commands and a short description of them"""
    click.echo('Here are all the commands\n')
    click.echo('\n'.join(map(lambda x: '\t' + x[0] + ' ' + x[1], allCmds['users'])))

@click.command(context_settings=CONTEXT_SETTINGS)
def helpemployees():
    """This command shows all the valid commands and a short description of them"""
    click.echo('Here are all the commands\n')
    click.echo('\n'.join(map(lambda x: '\t' + x[0] + ' ' + x[1], allCmds['employees'])))

@click.command(context_settings=CONTEXT_SETTINGS)
def helpmanagers():
    """This command shows all the valid commands and a short description of them"""
    click.echo('Here are all the commands\n')
    click.echo('\n'.join(map(lambda x: '\t' + x[0] + ' ' + x[1], allCmds['managers'])))

@click.command(context_settings=CONTEXT_SETTINGS)
def helpadmins():
    """This command shows all the valid commands and a short description of them"""
    click.echo('Here are all the commands\n')
    click.echo('\n'.join(map(lambda x: '\t' + x[0] + ' ' + x[1], allCmds['admins'])))


