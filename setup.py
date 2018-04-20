from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SkipList',
    packages = ['SkipList'],

    version='1.0.0',

    description='A skip list implemetation',
    long_description=long_description,

    url='https://github.com/isaacschaal/SkipList',

    author='Isaac Schaal',
    author_email='isaac@minerva.kgi.edu',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],


    keywords='Skip List Sorting',

    install_requires=['random'],['math']

   
)
