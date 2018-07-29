from io import BytesIO
from pyholecli.exceptions import HostnameNotFound
from pyholecli.models import Host, Hosts
from pyholecli.utils import put_file, run_command
from pyholecli import settings


class RunnableBaseClass:
    def __init__(self, connection):
        self._c = connection

    def _run_command(self, *args, **kwargs):
        return run_command(self._c, *args, **kwargs)

    def _put_file(self, local, remote, *args, **kwargs):
        return put_file(self._c, local, remote, *args, **kwargs)


class HostnameUtility(RunnableBaseClass):
    hosts_file = settings.LOCAL_HOSTNAME_FILENAME

    @property
    def hosts(self):
        if not hasattr(self, '_hosts'):
            result = self._run_command('cat', self.hosts_file, hide=True)
            self._hosts = Hosts.from_hosts_string(result.stdout)
        return self._hosts

    def get_hosts(self):
        return self.hosts

    def get_host(self, hostname):
        try:
            return self.hosts[hostname]
        except KeyError:
            message = 'Could not find hostname {}'.format(hostname)
            raise HostnameNotFound(message)

    def set_host(self, hostname, ip):
        self.hosts[hostname] = Host(hostname, ip)
        self._write_hosts()

    def remove_host(self, hostname):
        try:
            del self.hosts[hostname]
            self._write_hosts()
        except KeyError:
            message = 'Could not find hostname {}'.format(hostname)
            raise HostnameNotFound(message)

    def _write_hosts(self):
        hosts_fd = BytesIO(str(self.hosts).encode('utf-8'))
        self._put_file(hosts_fd, self.hosts_file)


class PiholeCLI(RunnableBaseClass):

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
