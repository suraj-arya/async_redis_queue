#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    "aioredis"
]

setup(
    name='async_redis_queue',
    version='0.1.0',
    description="An asynchronous Redis Queue implemented using asyncio",
    author="Suraj Arya",
    author_email='suraj.p.arya@gmail.com',
    url='https://github.com/suraj-arya/async_redis_q',
    packages=[
        'async_redis_queue',
    ],
    package_dir={'async_redis_queue':
                 'async_redis_queue'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='async_redis_queue',
)
