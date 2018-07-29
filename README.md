# Description
Control a Pi-hole installation from anywhere.

* Manage blacklisted and whitelisted domains.
* Create and remove custom domains for your internal services.
* Tail the query log.
* Remotely view the chronometer for realtime statistics.

# Install
```bash
pip install pyholecli
```

# Setup
Create a SSH key and install on your Pi-hole installation as the root user.
This key will be used to connect remotely to the instance.

You can use standard methods to declare the ssh key to be used by pyholecli.

## ssh-agent
```bash
eval `ssh-agent`
ssh-add ~/.ssh/keys/pi_hole
```

## ssh_config
```bash
# ~/.ssh/config
Host pi.hole
    User root
    IdentityFile ~/.ssh/keys/pi_hole
```

## Pass as an Argument
```bash
pyholecli -i ~/.ssh/keys/pi_hole status
```

# Examples
Get help about a specific command.
```
pyholecli --help <command>
```

Get the status of the Pi-hole services.
```
pyholecli status
  [✓] DNS service is running
  [✓] Pi-hole blocking is Enabled
```

Add a custom hostname to be resolved by Pi.hole.
```
pyholecli hostname -h testing.local -i 192.168.1.100
```

Remove multiple custom hostnames.
```
pyholecli remove-hostnames -h redis.localhost -h psql.localhost
```

# Functionality
```
Usage: pyholecli [--core-opts] <subcommand> [--subcommand-opts] ...

Core options:

  --complete                        Print tab-completion candidates for given parse remainder.
  --hide=STRING                     Set default value of run()'s 'hide' kwarg.
  --prompt-for-login-password       Request an upfront SSH-auth password prompt.
  --prompt-for-passphrase           Request an upfront SSH key passphrase prompt.
  --prompt-for-sudo-password        Prompt user at start of session for the sudo.password config value.
  --write-pyc                       Enable creation of .pyc files.
  -d, --debug                       Enable debug output.
  -D INT, --list-depth=INT          When listing tasks, only show the first INT levels.
  -e, --echo                        Echo executed commands before running.
  -f STRING, --config=STRING        Runtime configuration file to use.
  -F STRING, --list-format=STRING   Change the display format used when listing tasks. Should be one of: flat (default), nested, json.
  -h [STRING], --help[=STRING]      Show core or per-task help and exit.
  -H STRING, --hosts=STRING         Comma-separated host name(s) to execute tasks against.
  -i, --identity                    Path to runtime SSH identity (key) file. May be given multiple times.
  -l [STRING], --list[=STRING]      List available tasks, optionally limited to a namespace.
  -p, --pty                         Use a pty when executing shell commands.
  -S STRING, --ssh-config=STRING    Path to runtime SSH config file.
  -V, --version                     Show version and exit.
  -w, --warn-only                   Warn, instead of failing, when shell commands fail.

Subcommands:

  blacklist                   Blacklist a given domain.
  blacklisted-domains         Get all of the custom blacklisted domains.
  chronometer                 Continually print the stats using the chronometer.
  disable                     Disable the pi.hole blacklist.
  enable                      Enable the pi.hole blacklist.
  hostname                    Add a custom hostname which the pi.hole will resolve to the given IP address.
  hostnames                   Print the custom hostnames defined by the pi.hole instance.
  query                       Query the pi.hole instance for a given FQDN.
  remove-blacklisted-domain   Remove a given custom blacklisted domain.
  remove-hostname             Remove a custom hostname.
  remove-whitelisted-domain   Remove a given whitelisted domain.
  remove-wildcard-blacklist   Remove a given wildcard blacklist.
  status                      Query the status of the pi.hole instance.
  tail                        Tail the pi.hole resolver log file.
  whitelist                   Whitelist a given domain.
  whitelisted-domains         Get all of the custom whitelisted domains.
  wildcard-blacklist          Blacklist a given domain and its subdomains.
  wildcard-blacklists         Print the wildcard blacklist.
```
