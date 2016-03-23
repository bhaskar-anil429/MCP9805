# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MCP9805
# This code is designed to work with the MCP9805_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Temperature?sku=MCP9805_I2CS#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# MCP9805 address, 0x18(24)
# Select configuration register, 0x01(1)
#		0x0000(00)	Continuous conversion mode, Power-up
config = [0x00, 0x00]
bus.write_i2c_block_data(0x18, 0x01, config)
# MCP9805 address, 0x18(24)
# Select resolution rgister, 0x08(8)
#		0x03(03)	Resolution = +0.0625/C
#bus.write_byte_data(0x18, 0x08, 0x03)

time.sleep(0.5)

# MCP9805 address, 0x18(24)
# Read data back from 0x05(5), 2 bytes
# cTemp MSB, cTemp LSB
data = bus.read_i2c_block_data(0x18, 0x05, 2)

# Convert the data to 13-bits
cTemp = ((data[0] & 0x1F) * 256) + data[1]
if cTemp > 4095 :
	cTemp -= 8192
cTemp = cTemp * 0.0625
fTemp = cTemp * 1.8 + 32

# Output data to screen
print "Temperature in Celsius is    : %.2f C" %cTemp
print "Temperature in Fahrenheit is : %.2f F" %fTemp
