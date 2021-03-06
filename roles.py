# Import all Fabric APIs
from fabric.api import *

# Define get_roles function, not a Fabric function
def get_roles(*roles):
    return lambda:[y for x in roles for y in env.roledefs[x]]

env.roledefs = {
        'web': ['agent1', 'agent2', 'agent3'],
        'db': ['agent4'],
        'haproxy': ['agent5'],
        'puppet': ['master'],
        'all': get_roles('web', 'db', 'haproxy', 'puppet')
}
