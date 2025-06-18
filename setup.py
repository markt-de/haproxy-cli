import os
from distutils.core import setup

_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='haproxy-cli',
      description='A tool to interact with HAProxy',
      author='markt.de',
      author_email='github-oss-noreply@markt.de',
      project_urls={
          'Bug Tracker': 'https://github.com/markt-de/haproxy-cli/issues',
          'Documentation': 'https://github.com/markt-de/haproxy-cli',
          'Source Code': 'https://github.com/markt-de/haproxy-cli',
      },
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['haproxy'],
      scripts=['bin/haproxy-cli'],
      python_requires='>=3.7',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
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
          'Topic :: System :: Networking'])
