from fabric import task
from pyholecli.services import HostnameUtility, PiholeCLIWrapper


@task(help={'hostname': 'Hostname to search for.'})
def hostnames(c, hostname=None):
    util = HostnameUtility(c)
    if hostname:
        print(util.get_host(hostname))
    else:
        print(util.get_hosts())


@task(help={'hostname': 'Hostname to set.', 'ip': 'IP address of host.'})
def add_host(c, hostname, ip):
    util = HostnameUtility(c)
    util.set_host(hostname, ip)
    print(f'{hostname} added to pi-hole list.')


@task(help={'domain': 'Domain to query.'})
def query(c, domain):
    PiholeCLIWrapper(c).query(domain)


@task()
def disable(c):
    PiholeCLIWrapper(c).disable()


@task()
def enable(c):
    PiholeCLIWrapper(c).enable()


@task()
def status(c):
    PiholeCLIWrapper(c).status()


@task()
def chronometer(c):
    PiholeCLIWrapper(c).chronometer()


@task()
def tail(c):
    PiholeCLIWrapper(c).tail()


@task(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def blacklist(c, domain):
    PiholeCLIWrapper(c).blacklist(domain)


@task()
def get_blacklisted_domains(c):
    PiholeCLIWrapper(c).get_blacklisted_domains()


@task(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def remove_blacklisted_domains(c, domain):
    PiholeCLIWrapper(c).remove_blacklisted_domains(domain)


@task(help={'domain': 'Domain to whitelist.'}, iterable=['domain'])
def whitelist(c, domain):
    PiholeCLIWrapper(c).whitelist(domain)


@task()
def get_whitelisted_domains(c):
    PiholeCLIWrapper(c).get_whitelisted_domains()


@task(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def remove_whitelisted_domains(c, domain):
    PiholeCLIWrapper(c).remove_whitelisted_domains(domain)
