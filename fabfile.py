# Fabric tasks for interacting with Puppet agents

from fabric.api import *

# Roles are defined in roles.py
import roles

# Puppet agent tasks

# See if agent is running or not
@task
def agent_status():
    with settings(warn_only=True):
        sudo("/sbin/service puppet status")

# Stop agent
@task
def agent_stop():
    sudo("/sbin/service puppet stop")

# Start agent
@task
def agent_start():
    sudo("/sbin/service puppet start")

# Restart agent
@task
def agent_restart():
    sudo("/sbin/service puppet restart")

# Run agent, defaults to the production environment
@task
def agent_run(environment='production'):
    sudo("/usr/local/bin/puppet agent -t --environment=%s" % environment)

# Run agent in noop mode, defaults to the production environment
@task
def agent_noop(environment='production'):
    sudo("/usr/local/bin/puppet agent -t --noop --environment=%s" % environment)

# See what the agent thinks its certame is
@task
def certname():
    sudo("/usr/local/bin/puppet agent --configprint certname")

# See what the agent thinks its Puppet master is
@task
def server():
    sudo("/usr/local/bin/puppet agent --configprint server")

# Run facter and list the role fact
@task
def get_role():
    sudo("/usr/local/bin/facter role")

# Run facter and list the role fact
@task
def set_role(my_role='base'):
    sudo("echo 'role=%s' > /etc/puppetlabs/facter/facts.d/role.txt" % my_role)

# Testing facts
@task
def fact_test():
    role = sudo("/usr/local/bin/facter role")
    if role == "web":
        sudo("/usr/local/bin/puppet agent -t")
