from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Lottery analyser",
    version = "0.0.1",
    author = "Veton Sokolji",
    author_email = "veton.sokolji@gmail.com",
    description = ("A powerfull and simple Lottery analyser for Python."),
    license = "MIT",
    keywords = "Lottery game analyser",
    url = "",
    packages=find_packages(),
    install_requires=[""],
    long_description=open("README.txt").read() + "\n\n" + open("CHANGELOG.txt").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
)