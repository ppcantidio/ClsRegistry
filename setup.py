from setuptools import find_packages, setup

setup(
    name="pyregistry",
    version="1.0.0",
    author="Pedro Cantidio",
    author_email="ppcantidio@gmail.com",
    description="A simple class to facilitate the implementation of the Registry Pattern",
    long_description="PyRegistry is a Python library that provides a class for registering and managing classes in a registry, making it easier to implement the Registry Pattern in your projects.",
    long_description_content_type="text/plain",
    url="https://github.com/ppcantidio/pyregistry.py",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
