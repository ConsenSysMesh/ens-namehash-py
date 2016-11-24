#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages


DIR = os.path.dirname(os.path.abspath(__file__))


long_description = open(os.path.join(DIR, 'README.md')).read()


setup(
    name='ens-namehash',
    version="1.0.0",
    description="""Implementation of the namehash algorithm from EIP137""",
    long_description=long_description,
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/ConsenSys/ens-namehash-py',
    include_package_data=True,
    py_modules=['namehash'],
    install_requires=[
        "pysha3>=0.3,<1.0",
    ],
    license="MIT",
    zip_safe=False,
    keywords='ethereum ens namehash',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
