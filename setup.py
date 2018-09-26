from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="termextract",
    version="0.0.1",
    description="",
    long_description=long_description,
    license="BSD 2-Clause",
    url="https://github.com/kanjirz50/termextract",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=[
        "numpy",
        "mecab-python3"
    ],
    dependency_links=[],
    python_requires='~=3.3',
)
