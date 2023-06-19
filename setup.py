"""Builds the package."""
from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()


with open('requirements.txt') as requirements_file:
    requirements = list(requirements_file.readlines())


with open('dev-requirements.txt') as dev_requirements_file:
    dev_requirements = list(dev_requirements_file.readlines())

username = 'Pycryptor10'
email = 'Pycryptor10@gmail.com'

setup(
    name='cryption',
    version='0.4.0',
    url='https://github.com/Pycryptor10/cryption',
    description='Wrapper for Pycrptodome to encrypt/decrypt text',
    keywords='',
    long_description=readme,
    long_description_content_type='text/markdown',  # This is important!
    author=username,
    author_email=email,
    maintainer=username,
    maintainer_email=email,
    platforms='any',
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=requirements,
    tests_require=dev_requirements,
    test_suite='tests',
    license='GPL3',
)
