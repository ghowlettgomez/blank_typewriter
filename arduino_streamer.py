import serial
import json
import requests
import time
import serial

#Is an object that gets data from the source and streams data to the arduino controller which controlls the arduino.
class Streamer(object):

    #initializes the request_queue, the serial connection to the arduino, and the endpoint.
    def __init__(self):
        self.request_queue = []
        self.serial = serial.Serial('/dev/cu.usbmodem411', 9600)
        self.endpoint = 'insert endpoint here'

    #the main functio
    def main(self):
        while(True):
            try:
                r = requests.get(
                     self.endpoint).json()
            except Exception, error:
                print error
                time.sleep(5)
                continue
