import os
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name="SCP-Encyclopedia",
    version='0.1',
    description="Downloader for SCP foundation articles",
    url="https://github.com/riley-martine/SCP-Encyclopedia",
    author="Riley Martine",
    author_email="riley.martine.0+SCP@gmail.com",
    license="MIT",
    packages=["SCP-Encyclopedia"],
    install_requires=[
        "bs4",
    ],
    include_package_data=True,
    zip_safe=False)
