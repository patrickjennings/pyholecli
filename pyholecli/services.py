from pyholecli.models import Host, Hosts
from pyholecli.utils import run_command
from pyholecli import settings


class RunnableBaseClass:
    def __init__(self, connection):
        self._c = connection

    def _run_command(self, *args, **kwargs):
        return run_command(self._c, *args, **kwargs)


class HostnameUtility(RunnableBaseClass):
    hosts_file = settings.LOCAL_HOSTNAME_FILENAME

    def get_hosts(self):
        result = self._run_command('cat', self.hosts_file, hide=True)
        return Hosts.from_hosts_string(result.stdout)

    def get_host(self, hostname):
        hosts = self.get_hosts()
        return hosts[hostname]

    def set_host(self, hostname, ip):
        hosts = self.get_hosts()
        hosts[hostname] = Host(hostname, ip)


class PiholeCLIWrapper(RunnableBaseClass):

    def status(self):
        return self._run_command('pihole', 'status')

    def enable(self, domain):
        return self._run_command('pihole', 'enable')

    def disable(self, domain):
        return self._run_command('pihole', 'disable')

    def query(self, domain):
        return self._run_command('pihole', '-q', domain)

    def chronometer(self):
        return self._run_command('pihole', '-c', pty=True)

    def tail(self):
        return self._run_command('pihole', '-t', pty=True)

    def blacklist(self, *domains):
        return self._run_command('pihole', '-b', *domains)

    def get_blacklisted_domains(self):
        return self._run_command('pihole', '-b', '-l')

    def remove_blacklisted_domains(self, *domains):
        return self._run_command('pihole', '-b', '-d', *domains)

    def whitelist(self, *domains):
        return self._run_command('pihole', '-w', *domains)

    def get_whitelisted_domains(self):
        return self._run_command('pihole', '-w', '-l')

    def remove_whitelisted_domains(self, *domains):
        return self._run_command('pihole', '-w', '-d', *domains)
