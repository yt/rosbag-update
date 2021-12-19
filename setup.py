#!/usr/bin/env python3

from setuptools import setup

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

requires = ["rospkg", "pycryptodomex", "python-gnupg"]


setup(
    name="rosbag-update",
    version="0.1",
    description="Updates topic data types on ROS bags, solves checksum errors",
    author="Tayfun Yurdaer",
    author_email="tayfun@adastec.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["rosbag-update"],
    package_dir={"rosbag-update": "rosbag-update/"},
    install_requires=requires,
    ython_requires=">= 3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Licence :: OSI Approved :: MTI Licence",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
    ],
    entry_points={"console_scripts": ["bagup=bagup.bagup:main"]},
    keywords=["ROS", "rosbag", "update"]
)
