#!/usr/bin/env python
import os
import setuptools


here = os.path.abspath(os.path.dirname(__file__))

about = {}
#with open(os.path.join(here, 'exrates', '__version__.py'), 'r', 'utf-8') as f:
with open(f"{os.path.abspath(os.path.dirname(__file__))}/exrates/__version__.py") as f:
    exec(f.read(), about)

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type="text/markdown",
    url=about['__url__'],
    license=about['__license__'],
    packages=setuptools.find_packages(),
    python_requires='>=3',
    install_requires=['requests'],
    scripts=['exrates/exrates'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)