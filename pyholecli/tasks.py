from pyholecli.task_decorators import hostnametask, piholetask


@hostnametask(help={'hostname': 'Hostname to search for.'})
def hostnames(util, hostname=None):
    """Print the custom hostnames defined by the pi.hole instance."""
    if hostname:
        print(util.get_host(hostname))
    else:
        print(util.get_hosts())


@hostnametask(help={'hostname': 'Hostname to set.', 'ip': 'IP address of host.'})
def add_host(util, hostname, ip):
    """Add a custom hostname which the pi.hole will resolve to the given IP address."""
    util.set_host(hostname, ip)
    print(f'{hostname} added to pi-hole list.')


@piholetask(help={'domain': 'Domain to query.'})
def query(pihole, domain):
    """Query the pi.hole instance for a given FQDN."""
    pihole.query(domain)


@piholetask()
def disable(pihole):
    """Disable the pi.hole blacklist."""
    pihole.disable()


@piholetask()
def enable(pihole):
    """Enable the pi.hole blacklist."""
    pihole.enable()


@piholetask()
def status(pihole):
    """Query the status of the pi.hole instance."""
    pihole.status()


@piholetask()
def chronometer(pihole):
    """Continually print the stats using the chronometer."""
    pihole.chronometer()


@piholetask()
def tail(pihole):
    """Tail the pi.hole resolver log file."""
    pihole.tail()


@piholetask(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def blacklist(pihole, domain):
    """Blacklist a given domain."""
    pihole.blacklist(domain)


@piholetask()
def get_blacklisted_domains(pihole):
    """Get all of the custom blacklisted domains."""
    pihole.get_blacklisted_domains()


@piholetask(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def remove_blacklisted_domains(pihole, domain):
    """Remove a given custom blacklisted domain."""
    pihole.remove_blacklisted_domains(domain)


@piholetask(help={'domain': 'Domain to whitelist.'}, iterable=['domain'])
def whitelist(pihole, domain):
    """Whitelist a given domain."""
    pihole.whitelist(domain)


@piholetask()
def get_whitelisted_domains(pihole):
    """Get all of the custom whitelisted domains."""
    pihole.get_whitelisted_domains()


@piholetask(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def remove_whitelisted_domains(pihole, domain):
    """Remove a given whitelisted domain."""
    pihole.remove_whitelisted_domains(domain)
