#!/usr/bin/env python

import os
from os.path import isdir, islink, relpath, dirname
import subprocess
import sys
from setuptools import (
    Command,
    setup,
    find_packages,
)

sys.path.insert(0, '.')

__license__ = "MIT"

setup(
    name="rqlite_django",
    version="HEAD",
    url='https://github.com/sum12/rqlite-django/',
    author="sum12",
    maintainer="sum12",
    description='django backend for rqlite',
    license=__license__,
    package_dir={'': '.'},
    packages=find_packages('.'),
    platforms=['Posix'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Database',
    ],
)
