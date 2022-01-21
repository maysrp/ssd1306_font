from machine import I2C, Pin,RTC,WDT,reset
from ssd1306 import SSD1306_I2C
from font import Font
import time

i2c = I2C(scl=Pin(0), sda=Pin(2))
display= SSD1306_I2C(128, 32, i2c)

f=Font(display)


f.text("sdada",0,0,24)
f.show()