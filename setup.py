import os
import sys
import site
import setuptools
from distutils.core import setup


# Editable install in user site directory can be allowed with this hack:
# https://github.com/pypa/pip/issues/7953.
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

setup(
    name="CTEC405Library",
    version="1.0.0",
    description="Library functions for CTEC 405",
    author="CTEC 405",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        "scipy",
        "matplotlib",
        "openpyxl",
        "pandas",
        "scikit-learn",
        "XlsxWriter",
        "numpy",
        "python-docx",
        "tensorflow",
        "keras"
    ],
    python_requires=">=3.9",
)
