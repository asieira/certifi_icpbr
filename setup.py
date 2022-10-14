import io
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand
from os.path import join

exec(open(join('certifi_icpbr','version.py')).read())

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


setup(
    name='certifi_icpbr',
    description='Drop-in Replacement to certifi that includes ICP Brasil root certificates',
    long_description=read('README.rst'),
    author='Alexandre Sieira.',
    author_email='alexandre.sieira@gmail.com',
    version=__version__,
    url='https://github.com/asieira/certifi_icpbr/',
    license='Apache Software License',
    install_requires=['requests>=2'],
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},
    packages=['certifi_icpbr'],
    package_dir={'certifi_icpbr': 'certifi_icpbr'},
    package_data={'certifi_icpbr': ['*.pem']},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries',
    ],
)
