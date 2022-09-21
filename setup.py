#!/usr/bin/env python3

from importlib.metadata import entry_points
from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent.absolute()
version = (here / "meta_manager" / "VERSION").read_text().strip()
readme = here / "README.md"
if readme.exists():
    long_description = readme.read_text()
pkgs = find_packages(exclude=["contrib", "docs", "tests"])

setup(
    name="meta-manager",
    version="0.1.0",
    description="A CLI tool for managing metadata of arbitrary files",
    url="https://github.com/notadoktor/meta-manager",
    author="notadoktor",
    packages=pkgs,
    python_requires=">=3.8",
    package_data={"meta_manager": ["VERSION"]},
    entry_points={"console_scripts": "mm = meta_manager.__main__:app"},
    dependency_links=[],
    install_requires=[
        "certifi==2022.9.14; python_version >= '3.6'",
        "charset-normalizer==2.1.1; python_version >= '3.6'",
        "click==8.1.3; python_version >= '3.7'",
        "idna==3.4; python_version >= '3.5'",
        "pydantic==1.10.2",
        "pyyaml==6.0",
        "requests==2.28.1",
        "toml==0.10.2",
        "typer==0.6.1",
        "typing-extensions==4.3.0; python_version >= '3.7'",
        "urllib3==1.26.12; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5' and python_version < '4'",
    ],
    extras_require={
        "dev": [
            "asttokens==2.0.8",
            "attrs==22.1.0; python_version >= '3.5'",
            "backcall==0.2.0",
            "black==22.8.0",
            "cached-property==1.5.2",
            "cerberus==1.3.4",
            "certifi==2022.9.14; python_version >= '3.6'",
            "chardet==5.0.0; python_version >= '3.6'",
            "charset-normalizer==2.1.1; python_version >= '3.6'",
            "click==8.1.3; python_version >= '3.7'",
            "colorama==0.4.5; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "decorator==5.1.1; python_version >= '3.5'",
            "distlib==0.3.6",
            "executing==1.0.0",
            "fancycompleter==0.9.1",
            "idna==3.4; python_version >= '3.5'",
            "ipython==8.5.0",
            "jedi==0.18.1; python_version >= '3.6'",
            "matplotlib-inline==0.1.6; python_version >= '3.5'",
            "mypy-extensions==0.4.3",
            "orderedmultidict==1.0.1",
            "packaging==20.9; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "parso==0.8.3; python_version >= '3.6'",
            "pathspec==0.10.1; python_version >= '3.7'",
            "pdbpp==0.10.3",
            "pep517==0.13.0; python_version >= '3.6'",
            "pexpect==4.8.0; sys_platform != 'win32'",
            "pickleshare==0.7.5",
            "pip==22.2.2; python_version >= '3.7'",
            "pip-shims==0.7.3; python_version >= '3.6'",
            "pipenv-setup[black]==3.2.0",
            "pipfile==0.0.2",
            "platformdirs==2.5.2; python_version >= '3.7'",
            "plette[validation]==0.3.1; python_version >= '3.7'",
            "prompt-toolkit==3.0.31; python_full_version >= '3.6.2'",
            "ptyprocess==0.7.0",
            "pure-eval==0.2.2",
            "pygments==2.13.0; python_version >= '3.6'",
            "pyparsing==2.4.7; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pyrepl==0.9.0",
            "python-dateutil==2.8.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "requests==2.28.1",
            "requirementslib==1.6.9; python_version >= '3.7'",
            "setuptools==65.3.0; python_version >= '3.7'",
            "six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "stack-data==0.5.0",
            "toml==0.10.2",
            "tomli==2.0.1; python_full_version < '3.11.0a7'",
            "tomlkit==0.11.4; python_version >= '3.6' and python_version < '4'",
            "traitlets==5.4.0; python_version >= '3.7'",
            "urllib3==1.26.12; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5' and python_version < '4'",
            "vistir==0.6.1; python_version not in '3.0, 3.1, 3.2, 3.3' and python_version >= '3.7'",
            "wcwidth==0.2.5",
            "wheel==0.37.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "wmctrl==0.4",
        ]
    },
)
