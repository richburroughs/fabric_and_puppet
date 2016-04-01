# Import all Fabric APIs
from fabric.api import *

# Define get_roles function, not a Fabric function
def get_roles(*roles):
    return lambda:[y for x in roles for y in env.roledefs[x]]

env.roledefs = {
        'web': ['agent1'],
        'db': ['agent2'],
	'master': ['master'],
        'all': get_roles('web', 'db', 'master')
}
