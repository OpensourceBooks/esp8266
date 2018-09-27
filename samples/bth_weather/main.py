from time import sleep
from machine import Pin,I2C,SPI
import ssd1306
import urequests
import ujson
import network
import machine
import dht


#i2c = I2C(scl=Pin(14), sda=Pin(2), freq=100000)
#display = ssd1306.SSD1306_I2C(128,64, i2c)
spi = SPI(baudrate=10000000, polarity=1, phase=0, sck=Pin(14,Pin.OUT), mosi=Pin(13,Pin.OUT), miso=Pin(12))
display = ssd1306.SSD1306_SPI(128, 64, spi, Pin(5),Pin(4), Pin(16))

try:
    display.poweron()
    display.init_display()
    display.text("hi~",10,30)
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
    #print('network config:', wlan.ifconfig())
    

def set_ap(essid,password):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=essid)
    ap.config(password=password)


def get_bth_value():
    url = "https://blockchain.info/ticker"
    res = urequests.get(url)
    json = ujson.loads(res.text)
    cny = json["CNY"]
    value = float(cny["last"])
    # display.fill(0)
    display.text("{0} CNY/bth".format(value),5,20)
    # display.show()

def get_weather():

    url = "http://www.weather.com.cn/data/cityinfo/101010100.html"
    res = urequests.get(url)
    json = ujson.loads(res.text)

    temp1=json["weatherinfo"]["temp1"].replace("\u2103","")
    temp2=json["weatherinfo"]["temp2"].replace("\u2103","")

    # display.fill(0)
    display.text("temp:{0}~{1}".format(temp1,temp2),5,30)
    # display.show()

def get_dht():
    d = dht.DHT11(machine.Pin(12))
    measure = d.measure()
    temperature = d.temperature()
    humidity = d.humidity()
    display.text("local_temp:{0}".format(temperature),5,40)
    display.text("local_humi:{0}%".format(humidity),5,50)

while (True):
    connect_wifi("wifi","12345678")
    display.fill(0)
    display.text("dashboard",25,5)
    get_bth_value()
    get_weather()
    get_dht()
    display.show()
    sleep(60)




