from distutils.core import setup
from distutils.core import Extension

import pyA20
import sys

modules = [
    Extension('pyA20.gpio.gpio', sources=['pyA20/gpio/gpio_lib.c', 'pyA20/gpio/gpio.c']),
    Extension('pyA20.gpio.connector', sources=['pyA20/gpio/connector/connector.c']),
    Extension('pyA20.gpio.port', sources=['pyA20/gpio/port/port.c']),
    Extension('pyA20.i2c.i2c', sources=['pyA20/i2c/i2c_lib.c', 'pyA20/i2c/i2c.c']),
    Extension('pyA20.spi.spi', sources=['pyA20/spi/spi_lib.c', 'pyA20/spi/spi.c']),
]

setup(
    name = 'pyA20',
    version = pyA20.__version__,
    author = pyA20.__author__,
    author_email = pyA20.__email__,
    url = 'https://www.olimex.com/',
    license = pyA20.__license__,
    package_dir = {
        'pyA20' : 'pyA20',
        'pyA20.gpio' : 'pyA20/gpio',
        'pyA20.i2c' : 'pyA20/i2c',
        'pyA20.spi' : 'pyA20/spi',
    },
    packages=['pyA20', 'pyA20.gpio', 'pyA20.i2c', 'pyA20.spi'],
    description='Control GPIO, I2C and SPI on A20-OLinuXino-MICRO',
    long_description=open('README.rst').read(),
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python',
                 'Topic :: Home Automation',
                 'Topic :: Software Development :: Embedded Systems'
                 ],
    ext_modules=modules,
)
