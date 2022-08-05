#!/usr/bin/env python3
from setuptools import setup, find_packages


def main():
    setup(
        name = 'pyhcl',
        version = '1.0.0',
        url = 'https://github.com/liu-congcong/pyhcl/',
        author = 'Liucongcong',
        author_email = 'congcong_liu@icloud.com',
        license = 'MIT',
        description = 'Generate colors from the HCL color space.',
        scripts = ['bin/pyhcl',],
        packages = find_packages(),
        package_data = {'': ['LICENSE',]}
    )


if __name__ == '__main__':
    main()
