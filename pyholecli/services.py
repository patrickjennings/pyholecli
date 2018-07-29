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

    def get_host(self, hostname):
        try:
            return self.hosts[hostname]
        except KeyError:
            message = 'Could not find hostname {}'.format(hostname)
            raise HostnameNotFound(message)

    def set_host(self, hostname, ip):
        self.hosts[hostname] = Host(hostname, ip)
        self._write_hosts()

    def remove_hosts(self, hostnames):
        hostnames = [hostnames] if isinstance(hostnames, str) else hostnames
        for hostname in hostnames:
            try:
                del self.hosts[hostname]
            except KeyError:
                message = 'Could not find hostname {}'.format(hostname)
                raise HostnameNotFound(message)
        self._write_hosts()

    def _write_hosts(self):
        hosts_fd = BytesIO(str(self.hosts).encode('utf-8'))
        self._put_file(hosts_fd, self.hosts_file)
        self._run_command('pihole', 'restartdns')


class PiholeCLI(RunnableBaseClass):

    def _run_command(self, *args, **kwargs):
        return super()._run_command('pihole', *args, **kwargs)

    def status(self):
        return self._run_command('status')

    def enable(self, domain):
        return self._run_command('enable')

    def disable(self, domain):
        return self._run_command('disable')

    def query(self, domain):
        return self._run_command('-q', domain)

    def chronometer(self):
        return self._run_command('-c', pty=True)

    def tail(self):
        return self._run_command('-t', pty=True)

    def blacklist(self, domains):
        return self._run_command('-b', domains)

    def get_blacklisted_domains(self):
        return self._run_command('-b', '-l')

    def remove_blacklisted_domains(self, domains):
        return self._run_command('-b', '-d', domains)

    def whitelist(self, domains):
        return self._run_command('-w', domains)

    def get_whitelisted_domains(self):
        return self._run_command('-w', '-l')

    def remove_whitelisted_domains(self, domains):
        return self._run_command('-w', '-d', domains)

    def wildcard_blacklist(self, domains):
        return self._run_command('-wild', domains)

    def get_wildcard_blacklist(self):
        return self._run_command('-wild', '-l')

    def remove_wildcard_blacklist(self, domains):
        return self._run_command('-wild', '-d', domains)
