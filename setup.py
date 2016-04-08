# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
    name='django-waitress',
    version='0.0.1',
    description='Django using waitress.',
    author='odoku',
    author_email='masashi.onogawa@wamw.jp',
    keywords='django,waitress,server',
    url='http://github.com/odoku/django-waitress',

    packages=find_packages(),
    install_requires=[
        'waitress>=0.8.10',
    ],
    extras_require={
        'test': ['pytest==2.9.1'],
    }
)
