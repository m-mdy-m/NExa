from setuptools import setup, find_packages

setup(
    name='NExa',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.28.2',
        'termcolor>=2.3.0',
    ],
    entry_points={
        'console_scripts': [
            'nexa=bin.__init__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
    ],
)
