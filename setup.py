"""Minimal setup file for tasks project."""

from pathlib import Path

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

with open(Path(__file__).parent / "README.md", encoding="utf-8") as f:
    long_description = f.read()


with open(Path(__file__).parent / "requirements.txt", encoding="utf-8") as f:
    requires = [str(r) for r in parse_requirements(f)]

setup(
    name="collamake",
    version="0.0.1",
    description="collamake is a Python module to create simple collage photos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hasoya/collamake",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Graphics",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license="MIT",
    author="hasoya",
    author_email="20637498+hasoya@users.noreply.github.com",
    packages=find_packages(),
    install_requires=requires,
)
