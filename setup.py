#!/usr/bin/env python3
import setuptools
from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pymediareport',
    version='0.0.1',
    description="""
    Report the quality of your media collection. Use a defined set of metrics to identify videos matching this criteria.
    """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Eric Sarjeant',
    author_email='eric@sarjeant.us',
    maintainer='Eric Sarjeant',
    maintainer_email='eric@sarjeant.us',
    url='https://github.com/esarjeant/pymediareport',
    packages=['pymediareport'],
    keywords='pymediareport, mpeg, mp4, m4v',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries'
    ])
