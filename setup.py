import io

from setuptools import setup
from certifi_icpbr import __version__


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
    install_requires=['requests>=1.0.4'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    packages=['certifi_icpbr'],
    package_dir={'certifi_icpbr': 'certifi_icpbr'},
    package_data={'certifi_icpbr': ['*.pem']},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries',
    ],
)
