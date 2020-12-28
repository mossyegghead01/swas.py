from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='swas.py',
    packages=find_packages(include=['swas']),
    version='0.0.5',
    description='a joke library made for a discord user',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mossyegghead01/swas.py",
    author='mossy the made guy',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
