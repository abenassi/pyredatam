#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open("requirements.txt") as f:
    requirements = [req.strip() for req in f.readlines()]

with open("README_PIP.rst") as f:
    readme = f.read()

test_requirements = [
    "nose",
    "pypandoc"
]

setup(
    name='pyredatam',
    version='0.0.11',
    description="Genera consultas REDATAM en python.",
    long_description=readme,
    author="Agustín Benassi",
    author_email='agusbenassi@gmail.com',
    url='https://github.com/abenassi/pyredatam',
    packages=[
        'pyredatam'
    ],
    package_dir={'pyredatam':
                 'pyredatam'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3+",
    zip_safe=False,
    keywords='pyredatam',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
