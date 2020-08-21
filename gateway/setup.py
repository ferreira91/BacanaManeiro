#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='gateway',
    version='0.0.1',
    description='Gateway',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        'marshmallow==v3.7.0',
        'nameko==v3.0.0-rc8'
    ],
    extras_require={
        'dev': [
            'pytest==5.4.3'
        ]
    },
    zip_safe=True
)
