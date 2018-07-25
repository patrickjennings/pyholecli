from pyholecli.task_decorators import hostnametask, piholetask


@hostnametask(help={'hostname': 'Hostname to search for.'})
def hostnames(util, hostname=None):
    if hostname:
        print(util.get_host(hostname))
    else:
        print(util.get_hosts())


@hostnametask(help={'hostname': 'Hostname to set.', 'ip': 'IP address of host.'})
def add_host(util, hostname, ip):
    util.set_host(hostname, ip)
    print(f'{hostname} added to pi-hole list.')


@piholetask(help={'domain': 'Domain to query.'})
def query(pihole, domain):
    pihole.query(domain)


@piholetask()
def disable(pihole):
    pihole.disable()


@piholetask()
def enable(pihole):
    pihole.enable()


@piholetask()
def status(pihole):
    pihole.status()


@piholetask()
def chronometer(pihole):
    pihole.chronometer()


@piholetask()
def tail(pihole):
    pihole.tail()


@piholetask(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def blacklist(pihole, domain):
    pihole.blacklist(domain)


@piholetask()
def get_blacklisted_domains(pihole):
    pihole.get_blacklisted_domains()


@piholetask(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def remove_blacklisted_domains(pihole, domain):
    pihole.remove_blacklisted_domains(domain)


@piholetask(help={'domain': 'Domain to whitelist.'}, iterable=['domain'])
def whitelist(pihole, domain):
    pihole.whitelist(domain)


@piholetask()
def get_whitelisted_domains(pihole):
    pihole.get_whitelisted_domains()


@piholetask(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def remove_whitelisted_domains(pihole, domain):
    pihole.remove_whitelisted_domains(domain)
