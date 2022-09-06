from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
import framebuf

i2c = I2C(scl=Pin(0), sda=Pin(2))
display = SSD1306_I2C(128, 32, i2c)

file = open('ASC16', 'rb')
file.seek(ord('A') * 16)
font_code = file.read(16)
fb = framebuf.FrameBuffer(bytearray(font_code), 8, 16, framebuf.MONO_HLSB)
display.blit(fb, 0, 0)
display.show()
