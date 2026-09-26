from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name ="FLIPKART RECOMMANDER",
    version="0.2",
    author="dmt",
    packages=find_packages(),
    install_requires=requirements
)