from machine import Pin,I2C,SPI
import ssd1306
import gfx

i2c = I2C(scl=Pin(2), sda=Pin(0), freq=100000)
oled = ssd1306.SSD1306_I2C(128,64, i2c)
#oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x27)
graphics = gfx.GFX(128, 64, oled.pixel)
try:
    oled.poweron()
    oled.init_display()
    oled.fill(0)
    oled.pixel(30, 30, 1)
    #oled.invert(True)
    #oled.text("oled",10,20)
    #graphics.line(0, 0, 127, 63, 1)
    #graphics.rect(0, 0, 120, 160, 1)
    #graphics.circle(30, 30, 20, 1)
    #graphics.fill_circle(50, 30, 15, 1)
    #graphics.triangle(30, 30, 40, 50, 60, 30,1)
    #graphics.fill_triangle(30, 30, 40, 50, 60, 30,1)
    #graphics.fill_rect(0, 0, 120, 160, 1)

    oled.show()
except Exception as ex:
    print (ex)
    oled.poweroff()
