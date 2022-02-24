from logic import *



filename = './listas/prueba_1.csv'
#contactos[0], crear_contacto[1], boton_ENTER[2], grupos[3], numero_celular[4], mail[5], guardar[6]
cordinates =('417 940', '723 835', '990 2160', '282 1820', '249 874', '270 1350', '750 2175')

if __name__ == '__main__':
    agregar_contacto(filename, cordinates)