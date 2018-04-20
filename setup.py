from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))



setup(
    name='SkipList',
    packages=find_packages(exclude=['random', 'math']),


    version='1.0.0',

    description='A skip list implemetation',

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



   
)
