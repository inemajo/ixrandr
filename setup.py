import os
from setuptools import setup, find_packages

extras = []
if os.path.exists('/etc/bash_completion.d'):
    extras += [('/etc/bash_completion.d', ['extra/bash-completion/ixrandr'])]
elif os.path.exists('/usr/share/bash-completion/'):
    extras += [('/usr/share/bash-completion/', ['extra/bash-completion/ixrandr'])]

if os.path.exists('/usr/share/zsh/site-functions/'):
    extras += [('/usr/share/zsh/site-functions/', ['extra/zsh-completion/_ixrandr'])]
print(extras)    
setup(
    name="ixrandr",
    version="0.2",
    author="Inemajo",
    author_email="inemajo@fsfe.org",
    description="interactive xrandr",
    long_description=open('README.md').read(),
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Console',
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ],
    scripts = ['ixrandr'],
    data_files=extras
)
