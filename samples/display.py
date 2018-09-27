from machine import Pin,I2C,SPI
import ssd1306
i2c = I2C(scl=Pin(2), sda=Pin(0), freq=100000)
display = ssd1306.SSD1306_I2C(128,64, i2c)
try:
    display.poweron()
    display.init_display()
    display.text("esp8266",10,20)
    display.text("coding by cr4fun",10,40)
    # Write display buffer
    display.show()
except Exception as ex:
    display.poweroff()
