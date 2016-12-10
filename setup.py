import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as readme:
	README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='drf-nested-field-multipart',
    version='0.0.1',
    license='MIT',
    packages=['drf_nested_field_multipart'],
    include_package_data=True,
    description='Parser for nested params in multipart file upload',
    long_description=README,
    url='https://github.com/ah450/drf-nested-field-multipart',
    author='Ahmed Hisham Ismail',
    author_email= 'ahm3d.hisham@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License'
    ],
)