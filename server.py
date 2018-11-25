import socket                # Import socket module
import thread
import os
from cli import help, login, registration, locations, donations, maps
from io import BytesIO

VALID_CMDS = {
    'guests': {
        'help': help.helpguests,
        'login': login.login,
        'register': registration.register,
        'locations': locations.locations,
        'map': maps.maps,
        'end': None
    },
    'users' : {
        'help': help.helpusers,
        'locations': locations.locations,
        'map': maps.maps,
        'getdonations': donations.userget,
        'searchdonations': donations.usersearch,
        'end': None,
        'logout': None
    },
    'employees' : {
        'help': help.helpemployees,
        'locations': locations.locations,
        'map': maps.maps,
        'getdonations': donations.employeeget,
        'searchdonations': donations.employeesearch,
        'adddonation': donations.employeeadd,
        'end': None,
        'logout': None
    },
    'managers' : {
        'help': help.helpmanagers,
        'locations': locations.locations,
        'map': maps.maps,
        'getdonations': donations.managerget,
        'searchdonations': donations.managersearch,
        'adddonation': donations.manageradd,
        'end': None,
        'logout': None
    },
    'admins' : {
        'help': help.helpadmins,
        'locations': locations.locations,
        'map': maps.maps,
        'getdonations': donations.adminget,
        'searchdonations': donations.adminsearch,
        'end': None,
        'logout': None
    }
}

def runCmd(session, cmd, opts):
    if cmd not in VALID_CMDS[session['role']]:
        return "INVALID COMMAND"
    else:
        if 'donation' in cmd:
            sys.argv = [cmd, session['jwt']] + opts
        else:
            sys.argv = [cmd] + opts
        real_stdout = sys.stdout
        real_stderr = sys.stderr
        fake_stdout = BytesIO()
        cur = VALID_CMDS[session['role']][cmd]
        try:
            sys.stdout = fake_stdout
            sys.stderr = fake_stdout
            cur()
        finally:
            sys.stdout = real_stdout
            sys.stderr = real_stderr
            output_string = fake_stdout.getvalue()
            if len(output_string.split('\n')) == 3:
                js = eval(output_string.split('\n')[1])
                try:
                    if js['jwt']:
                        session['jwt'] = js['jwt']
                        session['role'] = js['role']
                        session['fname'] = js['firstname']
                        session['lname'] = js['lastname']
                        output_string = output_string.split('\n')[0] +'\n'
                except:
                    pass
            fake_stdout.close()
            return output_string

        return "COMMAND FAILED"

def newClient(clientsocket, addr):
    SESS = {
        'jwt': None,
        'role': 'guests',
        'fname': None,
        'lname': None
    }
    while True:
        msg = clientsocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        if msg:
            msg = msg.replace('\n', '').replace('\r', '')
            tokens = msg.split(' ')
            cmd = tokens[0].lower()
            if cmd in VALID_CMDS[SESS['role']]:
                if cmd == 'end':
                    clientsocket.send('THANKS FOR USING DONATION TRACKER TELNET\n')
                    break
                elif cmd == 'logout':
                    SESS = {
                        'jwt': None,
                        'role': 'guests',
                        'fname': None,
                        'lname': None
                    }
                    clientsocket.send('SUCCESSFULLY LOGGED OUT\n')
                else:
                    opts = tokens[1:]
                    clientsocket.send(runCmd(SESS, cmd, opts) + '\n')
            else:
                clientsocket.send('INVALID COMMAND, CHECK \'help\' FOR VALID COMMANDS OR \'end\' THE CONNECTION\n')
        else:
            clientsocket.send('INVALID COMMAND, CHECK \'help\' FOR VALID COMMANDS OR \'end\' THE CONNECTION\n')
    clientsocket.close()

s = socket.socket()         # Create a socket object
host = ''                   # Get local machine name
port = os.environ['PORT']   # Reserve a port for your service.

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

while True:
    c, addr = s.accept()     # Establish connection with client.
    thread.start_new_thread(newClient,(c,addr))

s.close()
print 'Goodbye!'
sys.exit(0)
