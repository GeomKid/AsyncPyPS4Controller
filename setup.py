from pathlib import Path

import tomli
from setuptools import find_packages, setup

with open("pyproject.toml", "rb") as f:
    pyproject = tomli.load(f)

setup(
    name="AsynchronousPS4Controller",
    author="Tan Chin Peng",
    author_email="huntiktan188@gmail.com",
    description=pyproject["tool"]["poetry"]["description"],
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/GeomKid/AsyncPyPS4Controller",
    version=pyproject["tool"]["poetry"]["version"],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=(Path(__file__).parent / "requirements.txt").read_text().splitlines(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
