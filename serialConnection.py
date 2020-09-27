import serial
import time
import sys,os,json
from gpiozero import LED
from datetime import datetime

def message(message,type='Failed'):
    with open('message.log','a') as file:
        file.write('[{} {}]\t{}\n'.format(type,datetime.now().strftime("%d/%m/%Y %H:%M:%S"),message))
   

class Arduino(serial.Serial):
    def __init__(self,port,baudRate):
        super().__init__(port, baudRate, timeout=1)
        self.flush()

    def send(self,data:str):
        ledR.on()
        self.write(str(data+"\n").encode('utf-8'))
        time.sleep(0.5)
        ledR.off()

    
    def get(self):
        return self.readline().decode('utf-8').rstrip()

if __name__ == '__main__':
    a=0 #'/dev/ttyACM1'
    arduino=Arduino('/dev/ttyACM0',9600)
    ledR=LED(17)
    while True:
        try:
            a+=1
            b={"type":a}

            arduino.send(json.dumps(b))
            message(a)
            time.sleep(0.5)
        except ValueError as e:
            message(e)
