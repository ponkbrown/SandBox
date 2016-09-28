import serial, time

def leeSerial():
    ser = serial.Serial('/dev/ttyUSB1', 9600)
    while True:
        try:
            tarjeta = ser.readline()
            salida = tarjeta.decode('UTF-8').strip()[1:]
            yield salida
        except:
            del ser
            ser = serial.Serial('/dev/ttyUSB1', 9600)
        time.sleep(.5)

if __name__ == '__main__':
    for a in leeSerial():
        print(a)
