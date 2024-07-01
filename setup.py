from setuptools import setup, find_packages

setup(
    name='LamRand',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openpyxl',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'lamrand=lamrand.lamrand:main',
        ],
    },
)