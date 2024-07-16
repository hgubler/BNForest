from setuptools import setup, find_packages
import subprocess
import sys

def install_build_dependencies():
    """Install build dependencies from requirements-build.txt."""
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + requirements)

def main():
    """Run the setup script after installing build dependencies."""
    install_build_dependencies()
    setup(
        name='BNForest',
        version='0.1.0',
        author='Your Name',
        author_email='your.email@example.com',
        description='A package for Bayesian Network Forest Sampling',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/yourusername/BNForest',
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        install_requires=[
            'qosa-indices @ git+https://gitlab.com/qosa_index/qosa.git'
        ],
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.6',
    )

if __name__ == "__main__":
    main()