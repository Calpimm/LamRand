from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='LamRand',
    version='0.1.3',  # Increment the version number
    description='A high-quality random number generator library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Kutay Irmak',
    author_email='kutayirmak@icloud.com',
    url='https://github.com/calpimm/LamRand',
    packages=find_packages(),
    install_requires=required,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)