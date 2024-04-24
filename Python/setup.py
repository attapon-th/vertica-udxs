#!/usr/bin/env python
import os
from setuptools import setup, find_packages


__version__ = "0.1.0"
setup(
    name="pyudx",
    version=__version__,
    author="attapon.th",
    maintainer="attapon.th",
    maintainer_email="attapon.4work@gmial.com",
    url="https://github.com/attapon-th/vertica-pylib",
    long_description="",
    long_description_content_type="text/markdown",
    install_requires=[
        "pycryptodome>=3.17.0",
    ],
    packages=find_packages(),
)
