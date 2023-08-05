from setuptools import setup, find_packages, Extension
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'Batch-computing solution for cashflow calculations.'
LONG_DESCRIPTION = 'Prototype batch-computing library for calculating loan amortization tables.'


# Setting up
setup(
    name="logical_rush",
    version=VERSION,
    author="Blasser Analytica (Rodolfo Blasser)",
    author_email="<rodolfoblasser@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    include_package_data=True,
    packages=['logical_rush'],
    keywords=['python', 'panama', 'finance', 'stocks', 'fixed income', 'data', 'batch-computing'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)