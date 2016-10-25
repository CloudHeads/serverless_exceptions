#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='serverless_exceptions',
    version='0.2.0',
    description="Exceptions for AWS Lambda in AWS Api Gateway to forward HTTP Exceptions with ththe Serverless Framework",
    long_description=readme + '\n\n' + history,
    author="Christoph Schabert",
    author_email='christoph@cloudheads.io',
    url='https://github.com/CloudHeads/serverless_exceptions',
    packages=[
        'serverless_exceptions',
    ],
    package_dir={'serverless_exceptions':
                 'serverless_exceptions'},
    entry_points={
        'console_scripts': [
            'serverless_exceptions=serverless_exceptions.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='serverless_exceptions',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
