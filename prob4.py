def foo():
    print('In foo')

def bar():
    print('In bar')

def baz():
    print('In baz')

commands = {
    'foo': foo,
    'bar': bar,
    'baz': baz
}

# command = input('What command would you like to run? ')
command = input('Enter a command:')

if command in commands:
    commands[command]()
else:
    print('ERROR: {} is not a valid command.')
