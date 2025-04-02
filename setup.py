# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s

@email : xianpuji@hhu.edu.cn
"""

from setuptools import  find_packages, setup
import os
import sys
import re



setup(
    name="Easyxp",
    version = '0.0.1',
    packages=find_packages(),
    install_requires=[
        "matplotlib>=3.4",
        "numpy>=1.21",
    ],
    author="Xianpu JI",
    author_email="xianpuji@hhu.edu.cn",
    description="Simple add quiver legend toolkit for matplotlib",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Blissful-Jasper/pysimple",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data = True,
)