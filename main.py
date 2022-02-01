from NeuroPy import NeuroPy
from time import sleep

neuroPy=NeuroPy("/dev/tty.MindWaveMobile-SerialPo") 
sleep(1)
neuroPy.start()
print("Started")
sleep(1)

while True:
    print ("Meditation ", neuroPy.meditation)
    print ("Attention ", neuroPy.attention)
    sleep(0.5)