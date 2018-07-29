from fabric import task
from pyholecli.exceptions import HostnameNotFound
from pyholecli.logging import logger
from pyholecli.services import HostnameUtility, PiholeCLI


@task(help={'hostname': 'Hostname to search for.'})
def hostnames(connection, hostname=None):
    """Print the custom hostnames defined by the pi.hole instance."""
    util = HostnameUtility(connection)
    if hostname:
        try:
            logger.info(util.get_host(hostname))
        except HostnameNotFound as e:
            logger.error(e)
    else:
        logger.info(util.hosts)


@task(help={'hostname': 'Hostname to set.', 'ip': 'IP address of host.'})
def hostname(connection, hostname, ip):
    """Add a custom hostname which the pi.hole will resolve to the given IP address."""
    HostnameUtility(connection).set_host(hostname, ip)
    logger.info('Added Host: %s with IP: %s', hostname, ip)


@task(help={'hostname': 'Hostname to remove.'}, iterable=['hostname'])
def remove_hostname(connection, hostname):
    """Remove a custom hostname."""
    try:
        HostnameUtility(connection).remove_hosts(hostname)
        logger.info('Removed Host: %s', hostname)
    except HostnameNotFound as e:
        logger.error(e)


@task(help={'domain': 'Domain to query.'})
def query(connection, domain):
    """Query the pi.hole instance for a given FQDN."""
    PiholeCLI(connection).query(domain)


@task()
def disable(connection):
    """Disable the pi.hole blacklist."""
    PiholeCLI(connection).disable()


@task()
def enable(connection):
    """Enable the pi.hole blacklist."""
    PiholeCLI(connection).enable()


@task()
def status(connection):
    """Query the status of the pi.hole instance."""
    PiholeCLI(connection).status()


@task()
def chronometer(connection):
    """Continually print the stats using the chronometer."""
    PiholeCLI(connection).chronometer()


@task()
def tail(connection):
    """Tail the pi.hole resolver log file."""
    PiholeCLI(connection).tail()


@task(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def blacklist(connection, domain):
    """Blacklist a given domain."""
    PiholeCLI(connection).blacklist(domain)


@task()
def blacklisted_domains(connection):
    """Get all of the custom blacklisted domains."""
    PiholeCLI(connection).get_blacklisted_domains()


@task(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def remove_blacklisted_domain(connection, domain):
    """Remove a given custom blacklisted domain."""
    PiholeCLI(connection).remove_blacklisted_domains(domain)


@task(help={'domain': 'Domain to whitelist.'}, iterable=['domain'])
def whitelist(connection, domain):
    """Whitelist a given domain."""
    PiholeCLI(connection).whitelist(domain)


@task()
def whitelisted_domains(connection):
    """Get all of the custom whitelisted domains."""
    PiholeCLI(connection).get_whitelisted_domains()


@task(help={'domain': 'Domain to blacklist.'}, iterable=['domain'])
def remove_whitelisted_domain(connection, domain):
    """Remove a given whitelisted domain."""
    PiholeCLI(connection).remove_whitelisted_domains(domain)


@task(help={'domain': 'Domain to wildcard blacklist.'}, iterable=['domain'])
def wildcard_blacklist(connection, domain):
    """Blacklist a given domain and its subdomains."""
    PiholeCLI(connection).wildcard_blacklist(domain)


@task()
def wildcard_blacklists(connection):
    """Print the wildcard blacklist."""
    PiholeCLI(connection).get_wildcard_blacklist()


@task(help={'domain': 'Wildcard blacklist to remove.'}, iterable=['domain'])
def remove_wildcard_blacklist(connection, domain):
    """Remove a given wildcard blacklist."""
    PiholeCLI(connection).remove_wildcard_blacklist(domain)
