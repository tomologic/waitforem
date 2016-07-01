# Always prefer setuptools over distutils
from setuptools import setup
from setuptools_scm import get_version
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
project = 'waitforem'

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=project,
    version=get_version(),
    description='Wait for dependent network services to start',
    long_description=long_description,
    url='https://github.com/tomologic/' + project,
    author='Jonas Tingeborn',
    author_email='username: jonas, domain: tomologic.com',
    license='http://unlicense.org/UNLICENSE',

    classifiers=[
        # Project maturity
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Target audience and category
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Boot',
        'Topic :: System :: Distributed Computing',

        # License
        'License :: OSI Approved :: MIT License',

        # Supported python versions
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    keywords='startup synchronization wait network service socket',
    packages=['waitforem'],

    extras_require={
        'dev': ['setuptools', 'setuptools_scm'],
    },

    # CLI shell script generation stanza
    entry_points={
        'console_scripts': [
            'waitforem=waitforem.__main__:main',
        ],
    },
)
