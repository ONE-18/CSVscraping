import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
from numpy import *

f = open('uno.csv', 'r')
lineas = f.readlines()
nombreb = input('Nombre: ')
for linea in lineas:
    linea = linea.split(',')
    nombre = linea[0]
    url = linea[1]
    marca = linea[2]
    clase = linea[3]
    precio = linea[4]
    if linea[0] == nombreb:
        print('Nombre:', nombre, '\nURL:', url, '\nPrecio esperado:', precio, '\nMarca:', marca, '\nClase:', clase)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        Raw = soup.find(marca, class_=clase)
        print(Raw)
        # Raw = Raw.text.split()

        if double(Raw[0].split(',')[0]) > double(precio):
            print('Todavía no\nPrecio actual:', Raw[0], '\nPrecio objetivo:', precio)
        else:
            print('AHORA\nPrecio actual:', Raw[0], '\nPrecio objetivo:', precio)

#  read.drop(read.index[[4]], inplace=True)
'''csvarchivo = open('uno.csv')  # Abrir archivo csv
entrada = csv.reader(csvarchivo)  # Leer todos los registros
reg = next(entrada)  # Leer registro (lista)
print(reg)  # Mostrar registro
url, nombre, precio = next(entrada)
print(url, nombre, precio)  # Mostrar campos
del url, nombre, precio, entrada  # Borrar objetos
csvarchivo.close()  # Cerrar archivo
del csvarchivo  # Borrar objeto'''
