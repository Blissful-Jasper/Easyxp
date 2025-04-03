from setuptools import find_packages, setup
import os

# 
readme_path = "README.md"
long_description = open(readme_path).read() if os.path.exists(readme_path) else ""

setup(
    name="Easyxp",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "matplotlib>=3.4",
        "numpy>=1.21",
    ],
    python_requires=">=3.6",  # 指定最低 Python 版本
    author="Xianpu JI",
    author_email="xianpuji@hhu.edu.cn",
    description="Simple add quiver legend toolkit for matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Blissful-Jasper/pysimple",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False,  
)
