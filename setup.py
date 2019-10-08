#!/usr/bin/python

from setuptools import setup, find_packages

setup(
	name = "nbycomp-pybrctl",
	version = "0.1.4.6",
	packages = find_packages(),
	author = "Ido Nahshon, Oriol Marí",
	author_email = "udragon@gmail.com, omari@nearbycomputing.com",
	description = "Python brctl wrapper",
	license = "GPLv2",
	keywords = "brctl, bridge-utils",
	url = "https://github.com/nbycomp/pybrctl",
	long_description = open("README.rst").read(),
	classifiers = [
		'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
		'Programming Language :: Python',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3'
	]
)
