from pathlib import Path
from setuptools import setup

requirements = (Path("requirements.txt").read_text().strip().split("\n"),)

setup(
    name="sen1511utils",
    version="0.1.0",
    description="Utilities for the SEN1511 course code.",
    url="https://github.com/sjpfenninger/sen1511",
    packages=["sen1511utils"],
    install_requires=requirements,
)
