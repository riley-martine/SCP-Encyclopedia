import os
from setuptools import setup

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
    zip_safe=False)
