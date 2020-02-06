from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Kaggle-Categorical-Feature-Encoding-Challenge-II",
    version="0.0.1",
    author="Ryan King",
    author_email="rmking4@ncsu.edu",
    description="A package for Kaggle competitions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/r12king/Kaggle-Categorical-Feature-Encoding-Challenge-II",
    packages=find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)