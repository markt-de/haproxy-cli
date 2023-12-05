#!/usr/bin/env python

from distutils.core import setup

setup(name='haproxy-cli',
      version='0.6',
      description='A tool to interact with HAProxy',
      author='markt.de',
      author_email='github-oss-noreply@markt.de',
      license='GPL-3',
      project_urls={
          'Bug Tracker': 'https://github.com/markt-de/haproxy-cli/issues',
          'Documentation': 'https://github.com/markt-de/haproxy-cli',
          'Source Code': 'https://github.com/markt-de/haproxy-cli',
      },
      packages=['haproxy'],
      scripts=['bin/haproxy-cli'],
      python_requires='>=3.7',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Topic :: Internet :: Proxy Servers',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Systems Administration',
          'Topic :: System :: Networking'],
      test_suite="tests")
