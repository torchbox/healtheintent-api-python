import os
from codecs import open
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ['healtheintent_apis']

# Essential dependencies
requires = [
    "requests"
]

# Testing dependencies
testing_extras = [
    "coverage",
]

# Documention dependencies
documentation_extras = [
    "pyenchant>=2.0",
    "Sphinx>=1.7.4",
    "sphinxcontrib-spelling>=1.4",
    "sphinx_rtd_theme>=0.3",
]

# Development dependencies
development_extras = [
    "ipdb",
    "werkzeug",
]

# Packaging dependencies
packaging_extras = testing_extras + [
    'setuptools',
    'wheel',
    'twine',
]

about = {}
with open(os.path.join(here, 'healtheintent_apis', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/x-rst',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_dir={'healtheintent_apis': 'healtheintent_apis'},
    include_package_data=True,
    install_requires=requires,
    license=about['__license__'],
    zip_safe=False,
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
    python_requires='>=3.5,<3.8',
    extras_require={
        'testing': testing_extras,
        'development': development_extras,
        'docs': documentation_extras,
        'packaging': packaging_extras,
    },
)
