# haproxy-cli

[![CI](https://github.com/markt-de/haproxy-cli/actions/workflows/build.yaml/badge.svg)](https://github.com/markt-de/haproxy-cli/actions/workflows/build.yaml)
[![PyPI version](https://badge.fury.io/py/haproxy-cli.svg)](https://badge.fury.io/py/haproxy-cli)

haproxy-cli - A tool to interact with HAProxy.

#### Table of Contents

1. [Overview](#overview)
1. [Install](#install)
1. [Modes](#modes)
1. [CLI Usage](#cli-usage)
1. [Examples](#examples)
    - [CLI](#cli)
    - [API](#api)
1. [Development](#development)
    - [Contributing](#contributing)


## Overview

haproxy-cli is a tool to manage the various aspects of HAProxy that can be controlled by means of its socket.
It is based on [haproxyctl](https://github.com/neurogeek/haproxyctl/) and is actively used in the OPNsense [HAProxy plugin](https://github.com/opnsense/plugins).

## Install

```
pip install haproxy-cli
```

## Modes

haproxy-cli can be used in 2 modes: CLI mode and Python API mode.
CLI mode, as the name implies, gives you a command, haproxy-cli, that can be used to control HAProxy.

You can use the Python API mode to integrate haproxy-cli directly in your Python project.

Every command in haproxy-cli has at least two methods: getResult and getResultObj.

The method getResult returns a formatted string with the results obtained by executing the given HAProxy command, while getResultObj returns a Python object with the results, making it easy to use this results in some Python code.

## CLI Usage

```
$ haproxy-cli --help

usage: haproxy-cli [-h] [-v] [-c COMMAND] [-l] [-H] [-s SERVER] [-b BACKEND]
                  [-w WEIGHT] [-k SOCKET]

A tool to interact with HAProxy

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Be verbose.
  -c COMMAND, --command COMMAND
                        Type of command. Default info
  -l, --list-commands   Lists available commands.
  -H, --help-command    Shows help for the given command.
  -s SERVER, --server SERVER
                        Attempt action on given server.
  -b BACKEND, --backend BACKEND
                        Set backend to act upon.
  -w WEIGHT, --weight WEIGHT
                        Specify weight for a server.
  -k SOCKET, --socket SOCKET
                        Socket to talk to HAProxy. It accepts
                        unix:///path/to/socket or tcp://1.2.3.4[:port]
                        addresses. If there is no match
                        for protocol, then it assumes a UNIX socket file.
```

## Examples

### CLI

```
$ haproxy-cli -c frontends

$ haproxy-cli -c servers -b example_backend

$ haproxy-cli -c get-weight -b example_backend -s server1

$ haproxy-cli -c set-weight -b example_backend -s server1 -w 99

$ haproxy-cli -k /run/haproxy/admin.sock -c backends
```

### API

```
#!/usr/bin/env python

from haproxy.conn import HaPConn
from haproxy import cmds

try:
    socket_conn = HaPConn('/var/run/haproxy.socket')

    if socket_conn:
        print(socket_conn.sendCmd(cmds.showInfo()))
    else:
        print('Could not open socket')

except Exception as exc:
    print(exc)
```

## Development

### Contributing

Please use the GitHub issues functionality to report any bugs or requests for new features. Feel free to fork and submit pull requests for potential contributions.
