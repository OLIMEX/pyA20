pyA20
=====

|Build Status|

Description
-----------

The package provide methods for controlling GPIO pins, I2C and SPI
buses. It's written for
`A20-OLinuXino-MICRO <https://www.olimex.com/Products/OLinuXino/A20/A20-OLinuXino-MICRO/open-source-hardware>`__,
but it can be used with other boards. In this case proper operation is
not guaranteed. You can check
`wiki <https://www.olimex.com/wiki/A20-OLinuXino-MICRO>`__ for more
information.

**Notes**:

	* When using GPIO make sure that the desired gpio is not used by another periphery.
	* Using this library requires root access.

GPIO methods
------------

The following methods are available:

* **init()** - Make initialization of the module. Must be called first.
* **getcfg()** - Read current configuration of gpio.
* **setcfg()** - Write configuration to gpio.
* **input()** - Return current value of gpio.
* **output()** - Set output value.
* **pullup()** - Set pull-up/pull-down.

The available constants are:

* **HIGH** - 1
* **LOW** - 0
* **INPUT** - 0
* **OUPTUT** - 1
* **PULLUP** - 1
* **PULLDOWN** - 2

The gpio are named two ways:

* By port name: PH0, PG2, PE10, etc. These can be imported from port module:

.. code:: python

	>>> from pyA20.gpio import port
	>>> dir(port)

* By connector name and pin number: gpio2p12, gpio3p8, lcdp18, uext1p3 and etc:

.. code:: python

	>>> from pyA20.gpio import connector
	>>> dir(connector)

Generally these constants are just an offset in the memory from the base
GPIO address, so they can be assigned to a number type variable.

.. code:: python

	>>> led = port.PH2
	>>> print led
	226

I2C methods
-----------

-  **init()** - Make initialization of the module
-  **open()** - Begin communication with slave device
-  **read()** - Read from slave device
-  **write()** - Write data to slave device
-  **close()** - End communication with slave device

SPI methods
-----------

-  **open()** - Open SPI bus with given configuration
-  **read()** - Read data from slave device without write
-  **write()** - Write data to slave device without read
-  **xfer()** - Do write and after that read
-  **close()** - Close SPI bus

Examples
--------

GPIO
~~~~

The example consist of: \* Initialize gpio module \* Initialize one gpio
as output and another one as input \* Polling input state and write
corresponding output value

.. code:: python

	#!/usr/bin/env python

	from pyA20.gpio import gpio
	from pyA20.gpio import port
	from pyA20.gpio import connector

	gpio.init() #Initialize module. Always called first

	gpio.setcfg(port.PG9, gpio.OUTPUT)  #Configure LED1 as output
	gpio.setcfg(port.PG9, 1)    #This is the same as above

	gpio.setcfg(port.PE11, gpio.INPUT)   #Configure PE11 as input
	gpio.setcfg(port.PE11, 0)   #Same as above

	gpio.pullup(port.PE11, 0)   #Clear pullups
	gpio.pullup(port.PE11, gpio.PULLDOWN)    #Enable pull-down
	gpio.pullup(port.PE11, gpio.PULLUP)  #Enable pull-up

	while True:
		if gpio.input(port.PE11) == 1:
			gpio.output(port.PG9, gpio.LOW)
			gpio.output(port.PG9, 0)
		else:
			gpio.output(port.PG9, gpio.HIGH)
			gpio.output(port.PG9, 1)

I2C
~~~

In this example: \* I2C module is imported \* Bus number 2 is opened \*
Some data is written, then verified

.. code:: python

	#!/usr/bin/env python

	from pyA20.i2c import i2c

	i2c.init("/dev/i2c-2")  #Initialize module to use /dev/i2c-2
	i2c.open(0x55)  #The slave device address is 0x55

	#If we want to write to some register
	i2c.write([0xAA, 0x20]) #Write 0x20 to register 0xAA
	i2c.write([0xAA, 0x10, 0x11, 0x12]) #Do continuous write with start address 0xAA

	#If we want to do write and read
	i2c.write([0xAA])   #Set address at 0xAA register
	value = i2c.read(1) #Read 1 byte with start address 0xAA

	i2c.close() #End communication with slave device

SPI
~~~

In ths example: \* SPI module is imported \* Bus 2 with chip-select 0 is
opened \* Some data is transfered to slave device

.. code:: python

	#!/usr/bin/env python

	from pyA20.spi import spi

	spi.open("/dev/spidev2.0")
	#Open SPI device with default settings
	# mode : 0
	# speed : 100000kHz
	# delay : 0
	# bits-per-word: 8

	#Different ways to open device
	spi.open("/dev/spidev2.0", mode=1)
	spi.open("/dev/spidev2.0", mode=2, delay=0)
	spi.open("/dev/spidev2.0", mode=3, delay=0, bits_per_word=8)
	spi.open("/dev/spidev2.0", mode=0, delay=0, bits_per_word=8, speed=100000)

	spi.write([0x01, 0x02]) #Write 2 bytes to slave device
	spi.read(2) #Read 2 bytes from slave device
	spi.xfer([0x01, 0x02], 2)   #Write 2 byte and then read 2 bytes.

	spi.close() #Close SPI bus

Changelog
---------
-  pyA20 0.2.12 (8 DEC 2017)

	-  Fixed extensions import
	-  Update examples

-  pyA20 0.2.11 (21 NOV 2017)

	-  Fixed mapping on portG
	-  Updated README
	-  Removed processor checking to allow build scripts
	-  Update license

-  pyA20 0.2.0 (02 SEP 2014)

	-  Updated to enable SPI and I2C control
	-  GPIO constant in separate modules
	-  Added example files
	-  Added support for Python3

.. |Build Status| image:: https://travis-ci.org/StefanMavrodiev/pyA20.svg?branch=master
   :target: https://travis-ci.org/StefanMavrodiev/pyA20
