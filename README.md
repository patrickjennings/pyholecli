Still in development.

# Description
Control Pi-hole installation from anywhere.

# Setup
Create a ssh key and install on your pi-hole installation.

Use ssh-agent and ssh-add to add ssh identity during use of the cli.

# Functionality
```bash
Usage: pyholecli-runner.py [--core-opts] <subcommand> [--subcommand-opts] ...

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

  add-host
  blacklist
  chronometer
  disable
  enable
  get-blacklisted-domains
  get-whitelisted-domains
  hostnames
  query
  remove-blacklisted-domains
  remove-whitelisted-domains
  status
  tail
  whitelist
```
