import time
from adafruit_circuitplayground.express import cp

cp.pixels.brightness = 0.7

while True: 
    if cp.touch_A3:
        cp.pixels.fill((50, 255, 255))
        cp.play_file("wave.wav")
        time.sleep(0.5)
        cp.pixels.fill((0, 0, 0))
    if cp.touch_A2:
        cp.pixels[0] = (0, 0, 255)
        cp.play_file("slime3.wav")
        time.sleep(0.25)
        cp.pixels[0] = (0, 0, 0)
    if cp.touch_A1:
        cp.pixels[2] = (0, 0, 255)
        cp.play_file("slime2.wav")
        time.sleep(0.25)
        cp.pixels[2] = (0, 0, 0)
    if cp.touch_A6:
        cp.pixels[4] = (0, 0, 255)
        cp.play_file("cut.wav")
        time.sleep(0.25)
        cp.pixels[4] = (0, 0, 0)
    if cp.touch_A5:
        cp.pixels[5] = (0, 0, 255)
        cp.play_file("soap.wav")
        time.sleep(0.25)
        cp.pixels[5] = (0, 0, 0)
    if cp.touch_A4:
        cp.pixels[7] = (0, 0, 255)
        cp.play_file("slime1.wav")
        time.sleep(0.25)
        cp.pixels[7] = (0, 0, 0)
    if cp.touch_A7:
        cp.pixels[9] = (0, 0, 255)
        cp.play_file("eating.wav")
        time.sleep(0.25)
        cp.pixels[9] = (0, 0, 0)



        
