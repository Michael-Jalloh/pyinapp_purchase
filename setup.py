from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
long_description = ""
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name= "pyinapp_purchase",
    packages= ["google_purchase"],
    version= "0.0.5",
    license= "MIT",
    description= "pyinapp_purchase is an open-source Python library designed to simplify and securely validate in-app purchase tokens server side.",
    author= "Michael Jalloh",
    long_description=long_description,
    long_description_content_type= "text/markdown",
    author_email= "michaeljalloh19@gmail.com",
    url= "https://github.com/Michael-Jalloh/pyinapp_purchase",
    keywords= ["inapp purchase","inapp","purchase","google inapp purchase"],
    install_requires=[
        "PyJWT",
        "requests",
        "cryptography"
    ],
    classifiers= [
        "Development Status :: 3 - Alpha",      
        "Intended Audience :: Developers",      
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    platforms=["any"],
    project_urls={
        "issues": "https://github.com/Michael-Jalloh/pyinapp_purchase/issues",
        "source": "https://github.com/Michael-Jalloh/pyinapp_purchase"
    },
    package_dir={"google_purchase": "src/google_purchase"},
)