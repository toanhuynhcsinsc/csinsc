import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csinsc",
    version="1.0.0",
    author="Toan Huynh",
    author_email="toan@csinschools.io",
    description="Tools and libraries used in the CSinSchools course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tba",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Creative Commons Attribution-ShareAlike 4.0 International License",
        "Operating System :: OS Independent",
    ],
)
