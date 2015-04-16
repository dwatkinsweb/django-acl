#!/usr/bin/env python
# coding: utf8

from setuptools import setup, find_packages

setup(
    name='django-acl',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/dwatkinsweb/django-acl',
    license='MIT',
    author='David Watkins',
    author_email='dwatkinsweb@gmail.com',
    description='ACL (Action Control List) permission handling.',
    platforms='any',
    install_requires=[
        'Django==1.6'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock'
    ],
)
