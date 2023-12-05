# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## v0.5.0 - 2015-05-24

### Changed
* Support for Python3

## v0.4.0 - 2015-05-19

### Added
* Added support for specifying sockets as a TCP socket:
* support for -k tcp://1.2.3.4:port
* support for -k unix:///some/path

## v0.3.1 - 2013-11-04

### Fixed
* Fixed wrong self accidentally passed to self._getResult.

## v0.3.0 - 2013-10-31

### Added
* Added new commands (frontends, backends)

## v0.2.0 - 2013-05-08

### Added
* Added new commands (get weight, set weight, servers)

### Changed
* Restructured command execution and arguments in haproxyctl

### Fixed
* Fixed problems with the buffer size while reading from the socket.

## v0.1.0 - 2013-05-07

Initial release of haproxyctl.
