from setuptools import setup, find_packages

setup(
    name='LamRand',
    version='0.1.0',
    description='A high-quality random number generator library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/calpimm/LamRand',
    packages=find_packages(),
    install_requires=[
        'openpyxl',
        'scipy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)