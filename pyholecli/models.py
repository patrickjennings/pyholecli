from collections import MutableMapping


class Host:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def __repr__(self):
        return f'<Host host={self.hostname} ip={self.ip}>'

    def __str__(self):
        return f'{self.ip} {self.hostname}'


class Hosts(MutableMapping):
    def __init__(self, hosts):
        self._hosts = hosts

    def __getitem__(self, key):
        return self._hosts[key]

    def __setitem__(self, key, value):
        self._hosts[key] = value

    def __delitem__(self, key):
        del self._hosts[key]

    def __iter__(self):
        return iter(self._hosts)

    def __len__(self):
        return len(self._hosts)

    def __repr__(self):
        return repr(self._hosts)

    def __str__(self):
        return '\n'.join([str(host) for host in self._hosts.values()])

    @classmethod
    def from_hosts_string(cls, hosts_string):
        hosts = {}
        for host in hosts_string.splitlines():
            ip, hostname = host.split(' ')
            hosts[hostname] = Host(hostname, ip)
        return cls(hosts)
