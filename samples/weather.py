from machine import Pin,I2C,SPI
from time import sleep
import urequests
import ujson
import network
import ssd1306
i2c = I2C(scl=Pin(2), sda=Pin(0), freq=100000)
display = ssd1306.SSD1306_I2C(128,64, i2c)
try:
    display.poweron()
    display.init_display()
    display.text("hi weather",10,20)
    display.text("by cr4fun",10,40)
    # Write display buffer
    display.show()
except Exception as ex:
    display.poweroff()

def connect_wifi(essid,password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        display.fill(0)
        display.text("wifi connecting",5,20)
        display.show()
        wlan.connect(essid,password)
        while not wlan.isconnected():
            pass
        display.fill(0)
        display.text("ip:",10,20)
        display.text(wlan.ifconfig()[0],5,40)
        display.show()

def get_weather():

    url = "http://www.weather.com.cn/data/cityinfo/101010100.html"
    res = urequests.get(url)
    json = ujson.loads(res.text)

    temp1=json["weatherinfo"]["temp1"].replace("\u2103","")
    temp2=json["weatherinfo"]["temp2"].replace("\u2103","")

    # display.fill(0)
    display.text("temp:{0}~{1}".format(temp1,temp2),15,30)

while (True):
    connect_wifi("wifi","12345678")
    display.fill(0)
    display.text("weather",15,10)
    display.text("by cr4fun",15,50)
    get_weather()
    display.show()
    sleep(60)

