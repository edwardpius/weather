from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='weather',
    version='0.1.0',
    description='Weather information for a city',
    long_description=readme,
    author='Edward',
    author_email='e.pius@computer.org',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
