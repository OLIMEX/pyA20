#!/usr/bin/env python3
"""Read from the EEPROM chip on A20-OLinuXino-MICRO

On the board there is small chip U3. This is 16kb eeprom memory AT24C16BN.
The i2c address can be different, but on this specific board is 0x50.

The text will be big mess if python3 is used.
"""

from pyA20.i2c import i2c

__author__ = "Stefan Mavrodiev"
__copyright__ = "Copyright 2014, Olimex LTD"
__credits__ = ["Stefan Mavrodiev"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "support@olimex.com"

eeprom_address = 0x50

"""Initialize i2c bus"""
i2c.init("/dev/i2c-1")
i2c.open(eeprom_address)

"""Set address pointer to the first"""
i2c.write([0x00])

print("Dump eeprom:")
print("="*24)

print("    ", end=' ')
for i in range(16):
    print(" %x" % i, end=' ')

print("\t", end=' ')
for i in range(16):
    print("%x" % i, end=' ')
print("")

"""Print data"""
for i in range(128):
    page = i2c.read(16)
    print("%03x:" % (i*0x10), end=' ')
    for j in range(0, 16):
        print("%02x" % page[j], end=' ')

    """Print characters"""
    print("\t", end=' ')
    for j in range(16):
        if 126 >= page[j] >= 32:
            print(chr(page[j]), end=' ')
        else:
            print('.', end=' ')
    print("")

i2c.close()
