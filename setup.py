from setuptools import setup, find_packages


setup(
    name='pyconcepticon',
    version='0.3.1',
    description='programmatic access to concepticon-data',
    long_description='',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
    ],
    author='',
    author_email='forkel@shh.mpg.de',
    url='',
    keywords='data linguistics',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'clldutils>=1.0.1',
        'clld',
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'concepticon=pyconcepticon.cli:main',
        ]
    },
    tests_require=[],
    test_suite="pyconcepticon")
