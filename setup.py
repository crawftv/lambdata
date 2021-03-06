#!/usr/bin/env python
# Package setup/installation and metadata for lambdata

import setuptools

REQUIRED = ["pandas","scikit-learn","seaborn","numpy"]
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata_crawftv",
    version="0.0.14",
    author="crawftv",
    description="Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/crawftv/lambdata",
    packages =setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
