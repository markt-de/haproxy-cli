# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [v0.7.2] - 2025-07-02

### Changed
* Improve build compatibility

## [v0.7.1] - 2025-06-18

### Changed
* Update Python packaging config

## [v0.7.0] - 2025-06-18

### Added
* New API command: setSslCrt

### Fixed
* Fix loading of payload in updateSslCrt/setSslCrt

### Deprecated
* Deprecate API command: updateSslCrt

## [v0.6.1] - 2023-12-05

### Changed
* Include README in Python package

## [v0.6.0] - 2023-12-05

### Added
* New API commands: showServers, set/getServerWeight
* New API output formats: json, bootstrap (OPNsense)

### Changed
* Map commands disableServer and enableServer to `set server state maint|ready`
* Print 'None' if no output is returned by HAProxy
* Decode HAProxy socket output as UTF-8 instead of ASCII

## v0.5.0 - 2015-05-24

### Changed
* Support for Python3

## v0.4.0 - 2015-05-19

### Added
* Add support for specifying sockets as a TCP socket:
* support for -k tcp://1.2.3.4:port
* support for -k unix:///some/path

## v0.3.1 - 2013-11-04

### Fixed
* Fix wrong self accidentally passed to self._getResult.

## v0.3.0 - 2013-10-31

### Added
* Add new commands (frontends, backends)

## v0.2.0 - 2013-05-08

### Added
* Add new commands (get weight, set weight, servers)

### Changed
* Restructure command execution and arguments in haproxyctl

### Fixed
* Fix problems with the buffer size while reading from the socket.

## v0.1.0 - 2013-05-07

Initial release of haproxyctl.

[Unreleased]: https://github.com/markt-de/haproxy-cli/compare/v0.7.2...HEAD
[v0.7.2]: https://github.com/markt-de/haproxy-cli/compare/v0.7.1...v0.7.2
[v0.7.1]: https://github.com/markt-de/haproxy-cli/compare/v0.7.0...v0.7.1
[v0.7.0]: https://github.com/markt-de/haproxy-cli/compare/v0.6.1...v0.7.0
[v0.6.1]: https://github.com/markt-de/haproxy-cli/compare/v0.6.0...v0.6.1
[v0.6.0]: https://github.com/markt-de/haproxy-cli/compare/v0.5.0...v0.6.0
