#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent.absolute()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="eth-mev-models",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="""eth-mev-models: Pydantic models related to the Ethereum MEV RPC namespace""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="antazoey",
    author_email="admin@antazoey.me",
    url="https://github.com/antazoey/eth-mev-models",
    include_package_data=True,
    install_requires=[
        "pydantic>=2.10.4,<3",
    ],
    python_requires=">=3.10,<4",
    extras_require={
        "test": [
            "pytest>=6.0",
            "pytest-timeout>=2.2.0,<3",
            "pytest-mock",
        ],
        "lint": [
            "mypy>=1.15.0,<2",
            "ruff>=0.11.7",
            "mypy>=1.15.0,<2",
        ],
        "release": [
            "setuptools>=75.6.0",
            "wheel",
            "twine",
        ],
    },
    py_modules=["eth_mev_models"],
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"eth_mev_models": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
