
import time
from sqlite3 import connect
from ppadb.client import Client as AdbClient

import csv
from dataclasses import field

filename = './listas/prueba_1.csv'

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

#contactos[0], crear_contacto[1], boton_ENTER[2], grupos[3], numero_celular[4], mail[5], guardar[6]
cordinates =('417 940', '723 835', '990 2160', '282 1820', '249 874', '270 1350', '750 2175')

def agregar_contacto(filename, cordinates):

    fields = []
    rows = []

    device, client = connect()
    time.sleep(1)

    #pantalla de inicio
    device.shell('input keyevent 3') #mainmenu
    time.sleep(0.3)
    device.shell('input keyevent 3')
    
    #app contactos  
    device.shell(f'input tap {cordinates[0]}')

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        for row in csvreader:
            nombre = row[0]
            celular = row[2]
            mail = row[3]

            #crear contacto_button
            time.sleep(0.3)
            device.shell(f'input tap {cordinates[1]}')

            #nombre del contacto
            time.sleep(0.3)
            device.shell(f'input text {nombre}')

            #telefono del contacto
            time.sleep(0.3)
            device.shell(f'input tap {cordinates[4]}')

            time.sleep(1)
            device.shell(f'input text {celular}')

            #mail del contacto
            time.sleep(0.3)
            device.shell('input keyevent 4') 

            device.shell(f'input tap {cordinates[5]}')
            device.shell(f'input text {mail}') 

            #guardar contacto
            time.sleep(0.3)
            device.shell('input keyevent 4') 

            device.shell(f'input tap {cordinates[6]}')

            #volver al menu de "contactos"
            time.sleep(0.5)
            device.shell('input keyevent 4')

def guardar():
    if __name__ == '__main__':
        device, client = connect()

        time.sleep(1)
        device.shell('input tap 750 2175')

        #volver para crear contacto nuevo
        time.sleep(0.3)
        device.shell('input keyevent 4') 

        #crear contacto_button
        time.sleep(0.3)
        device.shell('input tap 723 835')

agregar_contacto(filename, cordinates)