# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import platform
from setuptools import setup, find_packages

PACKAGE_NAME = 'iristemp'
PACKAGE_VERSION = '0.1'

INSTALL_REQUIRES = [
'mattapi==0.99.03'
#'mattapi-targets==0.77'
]

TESTS_REQUIRE = [
]

DEV_REQUIRES = [
]

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='Whatever',
    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing'
    ],
    keywords=['automation', 'testing'],
    author='Matt Wobensmith',
    author_email='mwobensmith@mozilla.com',
    url='https://github.com/mwobensmith/iristemp',
    download_url='https://github.com/mwobensith/iristemp/latest.tar.gz',
    license='MPL2',
    packages=find_packages(),
    python_requires='>=3.7.3',
    include_package_data=True,  # See MANIFEST.in
    zip_safe=False,
    use_2to3=False,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require={'dev': DEV_REQUIRES},  # For `pip install -e .[dev]`
    entry_points={
        'console_scripts': [
            'test = mattapi.scripts.test:foo',
            'lite = mattapi.scripts.test:main',
            'iris = mattapi.scripts.__main__:main',
            'api = mattapi.scripts.some_test:my_test'
        ]
    }
)
