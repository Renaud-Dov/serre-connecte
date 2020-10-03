import serial
import time
import sys,os,json

   

class Arduino(serial.Serial):
    def __init__(self,port,baudRate):
        super().__init__(port, baudRate, timeout=1)
        self.flush()

    def send(self,data:str,LED=None):
        if LED is not None:LED.on()
        self.write(str(data+"\n").encode('utf-8'))
        time.sleep(0.5)

        if LED is not None:LED.off()

    
    def get(self):
        return self.readline().decode('utf-8').rstrip()

    def message(self,message,type='Failed'):
        with open('message.log','a') as file:
            file.write('[{} {}]\t{}\n'.format(type,time.ctime(),message))