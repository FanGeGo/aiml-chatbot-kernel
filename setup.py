"""
Install the package containing AIML Chatbot kernel for Jupyter.
To actually use the kernel in Jupyter it needs to be installed into Jupyter 
afterwards.
"""

from __future__ import print_function
import os
import os.path
import sys

from setuptools import setup


PKGNAME = 'aimlbotkernel'

pkg = __import__( PKGNAME ) 
with open('README.rst') as f:
    readme = f.read()

setup_args = dict(
    name=PKGNAME,
    version=pkg.__version__,
    description='A Chatbot kernel for Jupyter based on pyAIML',
    long_description=readme,
    license='3-clause BSD license',
    download_url = 'https://github.com/peterldowns/mypackage/tarball/v'+pkg.__version__,
    url="https://github.com/paulovn/aiml-chatbot-kernel",
    author='Paulo Villegas',
    author_email='paulo.vllgs@gmail.com',

    packages=[ PKGNAME ],
    install_requires=[ "setuptools",
                       "ipykernel >= 4.0", 
                       "jupyter_client >= 4.0",
                       "aiml" ],

    entry_points = { 'console_scripts': [
        'jupyter-aimlbotkernel = aimlbotkernel.__main__:main',
    ]},
    package_data = { PKGNAME : [ 'resources/logo-*x*.png', 
                                 'resources/*.css' ] },
    include_package_data = True,

    keywords = ['AIML', 'chatbot','Jupyter','kernel'],
    classifiers = [
        'Framework :: IPython',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)

if __name__ == '__main__':
    setup( **setup_args )

