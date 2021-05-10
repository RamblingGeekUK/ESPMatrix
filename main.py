import network
from machine import Pin, SPI, ADC, I2C
import SSD1306
from max7219 import Max7219
import socket

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    # print('connecting to network...')
    # oled.fill(0)
    # oled.text('connecting to network...', 0, 10)
    # oled.show()
    while not wlan.isconnected():
        pass
# print('network config:', wlan.ifconfig())
# oled.fill(0)
# oled.text('network config:', 0, 10)
# oled.text(wlan.ifconfig()[0], 0, 20)
# oled.show()

# ESP32 Pin assignment
# i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# oled_width = 128
# oled_height = 32
# oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)

# oled.text('Welcome', 0, 0)
# oled.text('Starting up.....', 0, 20)

#p4 = Pin(4, Pin.OUT)
#p4.on()


# def setup_screen():
#     spi = SPI(1, baudrate=10000000, polarity=1,
#               phase=0, sck=Pin(19), mosi=Pin(23)) # SCK = cs mosi = din
#     cs = Pin(18, Pin.OUT)
#     screen = max7219.Max7219(32, 16, spi, cs)  # Clk PIN (Display)
#     screen.brightness(10)
#     return screen

# screen = setup_screen()
# screen.text('Hi!', 4, 4, 1)
# screen.show()

spi = SPI(1,
          baudrate=10000000,
          polarity=1,
          phase=0,
          sck=Pin(18),
          mosi=Pin(23))
cs = Pin(19, Pin.OUT)
display = Max7219(32, 24, spi, cs)

print('Loaded')
display.brightness(15)
display.rect(0, 0, 32, 24, 1)  # Draws a frame
display.text('abcd', 1, 1, 1)
display.text('EFGH', 0, 8, 1)
display.text('IJKL', 0, 16, 1)
#display.marquee('Hello World!')

display.show()




