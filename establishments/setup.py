#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='establishments',
    version='0.0.1',
    description='Establishments',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        'nameko==v3.0.0-rc8',
        'nameko-sqlalchemy==1.5.0'
    ],
    extras_require={
        'dev': [
            'pytest==5.4.3'
        ]
    },
    zip_safe=True
)
