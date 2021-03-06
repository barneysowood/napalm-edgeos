"""setup.py file."""

from setuptools import setup, find_packages

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines()
            if (len(r) > 0 and not r.startswith("#"))]

__author__ = 'Barney Sowood <barney@sowood.co.uk>'


setup(
    name="napalm-edgeos",
    version="0.2.0",
    packages=find_packages(),
    author="Barney Sowood",
    author_email="barney@sowood.co.uk",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/barneysowood/napalm-edgeos",
    include_package_data=True,
    install_requires=reqs,
)
