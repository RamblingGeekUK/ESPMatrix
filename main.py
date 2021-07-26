from machine import Pin, SPI, ADC, I2C
import network
import max7219
import socket
import mrequests as requests
from microdot import Microdot, Response
import max7219


def matrixMessage(msg, slidervalue):
        spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23))
        ss = Pin(19, Pin.OUT)
        
        display = max7219.Matrix8x8(spi, ss, 12)
        display.fill(0)
        display.brightness(slidervalue)
        if not msg:
                # display.pixel(0,0,1)
                # display.pixel(1,1,1)
                # display.hline(0,4,8,1)
                # display.vline(4,0,8,1)
                # display.line(8, 0, 16, 8, 1)
                # display.rect(17,1,6,6,1)
                # display.fill_rect(25,1,6,6,1)                
                display.show(msg,0,0,1)
        else:
                display.text(msg,0,0,1)
                display.show()


if not wlan.isconnected():
     while not wlan.isconnected():
        pass

app = Microdot()

htmldoc = """<!DOCTYPE html>
<html>
    <head>
        <title>Matrix Display</title>
    </head>
    <body>
        <div>
            <h1>Matrix Display</h1>
            <p>Enter your message</p>
        </div>
        <div>
            <form method="post">
                <div class="form-group">
                        <label for="title">Message</label>
                        <input type="text" name="mxmessage"
                                placeholder="" class="form-control"
                                value=""></input>
                </div>
                <div class="slidecontainer">
                        <label for="title">Brightness (<span id="slidervalue"></span>, 0 = dim)</label>
                        <input type="range" name="brightness" min="0" max="15" value="0" class="slider" id="brightness">
                </div>

                <div class="form-group">
                        <button type="submit" class="btn btn-primary">Submit</button>
                </div>
                
                </form>
        </div>
    
        <script>
                var slider = document.getElementById("brightness");
                var output = document.getElementById("slidervalue");
                output.innerHTML = slider.value;

                slider.oninput = function() {
                        output.innerHTML = this.value;
                        matrixMessage(mxmessage,this.value);
                }
        </script>

    </body>
</html>
"""


@app.route("", methods=["GET", "POST"])
def serial_number(request):
    print(request.headers)
    if request.method == 'POST':
            msg = request.form['mxmessage']
            brightness = int(request.form['brightness'])
            if len(msg) == 0:
                print(msg)
                msg = wlan.ifconfig()[0][-3:]
                matrixMessage(msg,brightness)
            else:
                matrixMessage(msg,brightness)
    return Response(body=htmldoc, headers={"Content-Type": "text/html"})

app.run(debug=True)
