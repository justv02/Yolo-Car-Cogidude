#CorgiDude board : https://www.aiiotshop.com/p/58
#refer to http://blog.sipeed.com/p/677.html
import pyautogui

import sensor,image,lcd,time
import KPU as kpu

import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm


lcd.init()
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)
sensor.run(1)

sensor.skip_frames(time = 2000)
lcd.init(type=2, freq=20000000, color=lcd.BLACK)
clock = time.clock()
mun = 0


fm.register(18, fm.fpioa.GPIO0)
output = GPIO(GPIO.GPIO0, GPIO.OUT)
output.value(0)

clock = time.clock()
classes = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
task = kpu.load(0x500000)
anchor = (1.08, 1.19, 3.42, 4.41, 6.63, 11.38, 9.42, 5.11, 16.62, 10.52)
a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
while(True):
    clock.tick()
    img = sensor.snapshot()
    objects = kpu.run_yolo2(task, img)
    print(clock.fps())
    output.value(0)
    if objects:
        for obj in objects:
            img.draw_rectangle(obj.rect(),color=(0,255,0),thickness=5)
            img.draw_string(obj.x()+10, obj.y(), classes[obj.classid()], color=(255,0,0),scale=3)
            img.draw_string(obj.x()+10, obj.y()+38, '%.3f'%obj.value(), color=(0,0,255),scale=2)
            output.value(1)
            clock.tick()
            img1 = pyautogui.screenshot()
            #a = img.save("/sd/test.jpg")
            mun = mun+1
            print(clock.fps())
            img1.save("/sd/"+str(mun)+".jpg")
            print(clock.fps())


    img = img.resize(240,240)
    lcd.display(img)
kpu.deinit(task)

