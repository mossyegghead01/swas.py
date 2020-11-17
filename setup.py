from setuptools import setup, find_packages

setup(
    name='swas.py',
    packages=find_packages(include=['swas']),
    version='0.0.3',
    description='a joke library made for a discord user',
    author='mossy the made guy',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
