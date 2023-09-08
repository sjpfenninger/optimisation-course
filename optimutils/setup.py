from pathlib import Path
from setuptools import setup

requirements = (Path("requirements.txt").read_text().strip().split("\n"),)

setup(
    name="optimutils",
    version="0.1.0",
    description="Optimisation course utilities.",
    url="https://github.com/sjpfenninger/optimisation-course",
    packages=["optimutils"],
    install_requires=requirements,
)
