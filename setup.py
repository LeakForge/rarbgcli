# type: ignore

import subprocess

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read().replace('](', '](https://raw.githubusercontent.com/LeakForge/rarbgcli/main/')
with open('requirements.txt', 'r') as fh:
    rqeuirements = fh.readlines()

version = subprocess.Popen('git describe --abbrev=0 --tags', shell=True, stdout=subprocess.PIPE).stdout.read().decode().strip().lstrip('v')

setuptools.setup(
    name='rarbgcli',
    version=version,
    description='Command line interface for therarbg.com',
    long_description=long_description,
    url='https://github.com/LeakForge/rarbgcli',
    author='LeakForge',
    author_email='rqjoapfpgc@use.startmail.com',
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=rqeuirements,
    keywords='rarbg torrent rarbgcli rarbgapi cli api scraper rarbg-cli rarbg-api rarbg-scraper',
    entry_points={
        'console_scripts': [
            'rarbgcli=rarbgcli.rarbgcli:cli',
            'rarbg=rarbgcli.rarbgcli:cli',
        ]
    },
)
