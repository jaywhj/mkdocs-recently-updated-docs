from setuptools import setup, find_packages

VERSION = '0.1'

setup(
    name="mkdocs-recently-updated-docs",
    version=VERSION,
    author="Aaron Wang",
    author_email="aaronwqt@gmail.com",
    license="MIT",
    description="A MkDocs plugin to show recently updated documents",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jaywhj/mkdocs-recently-updated-docs",
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.1.0',
        'mkdocs_document_dates>=3.4',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'mkdocs.plugins': [
            'recently-updated = mkdocs_recently_updated_docs.plugin:RecentlyUpdatedPlugin',
        ]
    },
    package_data={
        'mkdocs_recently_updated_docs': [
            'templates/*'
        ],
    },
    python_requires=">=3.7",
)
