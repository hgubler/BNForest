from setuptools import setup, find_packages

setup(
    name='BNForest',
    version='0.1.0',
    author='Hannes Gubler',
    author_email='hannes.gubler@epfl.ch',
    description='A package for generating synthetic data using a Bayesian Network with Random Forests for conditional distributions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hgubler/BNForest',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'networkx',
        'numba',
        'openturns',
        'qosa @ git+https://gitlab.com/qosa_index/qosa.git'
    ],
    setup_requires=['numba', 'numpy', 'pandas', 'scikit-learn', 'networkx', 'openturns'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)