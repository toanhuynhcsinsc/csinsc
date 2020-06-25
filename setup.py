import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csinsc",
    version="1.1.0.3",
    author="Toan Huynh",
    author_email="toan@csinschools.io",
    description="Tools and libraries used in the CSinSchools course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toanh/csinsc",
    packages=setuptools.find_packages(),
    install_requires=[
              'pytz',
              'requests',
              'bs4'
          ],    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
