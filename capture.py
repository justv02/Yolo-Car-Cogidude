# Untitled - By: Asus - พฤ. ต.ค. 21 2021

import sensor, image, time,lcd


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
lcd.init(type=2, freq=20000000, color=lcd.BLACK)
clock = time.clock()
mun = 0

while(True):
    clock.tick()
    img = sensor.snapshot()
    #a = img.save("/sd/test.jpg")
    mun = mun+1
    print(clock.fps())
    img.save("/sd/"+str(mun)+".jpg")
    lcd.display(img)
    print(clock.fps())

#a = img.save("/sd/test.jpg")
#import sensor, image, time,lcd
#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time = 2000)
#lcd.init(type=2, freq=20000000, color=lcd.BLACK)
#clock = time.clock()
#mun = 0
#while(True):
    #clock.tick()
    #img = sensor.snapshot()
    ##img = image.Image("/sd/33.jpg")
    #mun = mun+1
    #img.save("/sd/"+str(mun)+".jpg")
    #lcd.display(img)
    #print(clock.fps())
