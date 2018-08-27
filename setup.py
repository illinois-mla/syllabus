from setuptools import setup

setup(
    name='mls',
    version='0.1',
    description='Material for UIiUC course "Data Analysis and Machine Learning Applications"',
    url='http://github.com/illinois-mla',
    author='David Kirkby, with modifications from Mark Neubauer',
    author_email='msn@illinois.edu',
    license='BSD3',
    packages=['mls'],
    install_requires=['setuptools-git'],
    include_package_data=True,
    zip_safe=False)
