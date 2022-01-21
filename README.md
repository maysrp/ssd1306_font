# ssd1306_font
ssd1306 oled font micropython

upload  file to your micropython driver(ESP8266  ESP32 RP2040 )  
* ASC16
* ASC24
* ASC32
* font.py
* ssd1306

```
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from font import Font
import time

i2c = I2C(scl=Pin(0), sda=Pin(2))
display= SSD1306_I2C(128, 32, i2c)

f=Font(display)


f.text("8",0,0,8) #8 pix
f.text("16",8,0,16) #16 pix
f.text("24",24,0,24) #24 pix
f.text("32",48,0,32) #32 pix
f.show()
```
