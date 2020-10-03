import capteur
import serialConnection
# from gpiozero import LED
import json
import os
import time



class app():
    def __init__(self,arduino,capteur,led=None):
        self.arduino=arduino
        self.capteur=capteur
        self.led=led

        self.main()

    def main(self):
        b={"type":"moteur"}
        self.arduino.send(json.dumps(b))
        pass

    def getVal(self):
        # self.capteur
        pass

if __name__ == '__main__':
    if not os.path.exists('config.json'):
        open('config.json','x')
        raise  FileNotFoundError('You must configure config.json first')
    with open('config.json') as js:
        config=json.load(js)
    
    arduino=serialConnection.Arduino(config["Arduino"]["port"],config["Arduino"]["baudrate"])
    capteur=capteur.Capteur(config["captors"]["MAC"])
    # ledR=LED(config["Led"]["port"])
    print(capteur.valeurs())
    app(arduino,capteur)