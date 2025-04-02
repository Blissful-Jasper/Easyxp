# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s

@email : xianpuji@hhu.edu.cn
"""

from setuptools import setup, find_packages

setup(
    name="pysimple",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "matplotlib>=3.4",
        "numpy>=1.21",
        "python>=3.8.20"
    ],
    author="Xianpu JI",
    author_email="xianpuji@hhu.edu.cn",
    description="Simple add quiver legend toolkit for matplotlib",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pyquiverleg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)