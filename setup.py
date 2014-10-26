import os
from setuptools import setup, find_packages

setup(
    name="ixrandr",
    version="0.1",
    author="Inemajo",
    author_email="inemajo@fsfe.org",
    description="interactive xrandr",
    long_description=open('README.md').read(),
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Console',
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
    ]
    scripts=["ixrandr"]
)
