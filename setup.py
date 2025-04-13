#! /usr/bin/env python
import os.path as op
from setuptools import setup, find_packages

long_description = """
thaiaddress: A Parser for Thai Address

Parser for Thai address. ไลบรารี่เพื่อแยกแยะชื่อ ที่อยู่ รหัสไปรษณีย์ และเบอร์โทรศัพท์
"""


def get_version():
    """
    Get the version without importing, so as not to invoke dependency
    requirements.
    """
    base, _ = op.split(op.realpath(__file__))
    file = op.join(base, "thaiaddress", "__init__.py")

    for line in open(file, "r"):
        if "__version__" in line:
            return line.split("=")[1].strip().strip("'").strip('"')

requires = [
    "joblib==1.4.2",
    "deepcut==0.7.0.0",
    "spacy==3.8.5",
    "pythainlp==5.1.1",
    "sklearn-crfsuite==0.5.0",
    "numpy==2.1.3",
    "scikit-learn==1.6.1",
    "jsonlines==4.0.0",
    "fuzzywuzzy==0.18.0",
    "python-Levenshtein==0.27.1",
    "pandas==2.2.3",
    "eli5==0.15.0",
    "scipy==1.15.2"
]

test_requires = requires + [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "requests>=2.32.0"
]

if __name__ == "__main__":
    setup(
        name="thaiaddress",
        version=get_version(),
        description="A Python parser for Thai address",
        long_description=long_description,
        long_description_content_type='text/markdown',
        python_requires=">=3.8,<3.13",
        url="https://github.com/425degree-developers/thaiaddress",
        download_url="https://github.com/425degree-developers/thaiaddress.git",
        author="Titipat Achakulvisut",
        author_email="my.titipat@gmail.com",
        license="Apache Software License 2.0 (c) 2020 Titipat Achakulvisut, 425 Degree Co., Bangkok, Thailand",
        install_requires=requires,
        test_requires=test_requires,
        packages=find_packages(),
        include_package_data=True,
        keywords=[
            "Parser",
            "Address",
            "Thai Address",
            "Thai Natural Language Processing",
            "Natural Language Processing",
        ],
        classifiers=[
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Unix",
            "Operating System :: MacOS",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
        ],
        platforms="any",
        project_urls={
            "Source": "https://github.com/425degree-developers/thaiaddress",
            "Documentation": "https://github.com/425degree-developers/thaiaddress",
            "Bug Reports": "https://github.com/425degree-developers/thaiaddress/issues",
        },
    )
