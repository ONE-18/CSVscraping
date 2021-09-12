import csv
from _csv import writer
import requests
import pandas as pd
from glob import glob
from bs4 import BeautifulSoup
from time import sleep
from numpy import *


def write():
    list_of_elem = list()
    nombre = input('Nombre: ')
    list_of_elem.append(nombre)
    url = input('URL: ')
    list_of_elem.append(url)
    marca = input('Marca: ')
    list_of_elem.append(marca)
    clase = input('Clase: ')
    list_of_elem.append(clase)
    precioEsperado = input('Esperar hasta: ')
    list_of_elem.append(precioEsperado)
    # Open file in append mode
    with open('uno.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


def leerTodo():
    read = open('uno.csv')
    lineas = read.readlines()
    for line in lineas:
        print(line)


def search():
    File = open('uno.csv')
    entrada = csv.reader(File)
    linea = int(input('Línea: '))
    cont = -2
    while linea > cont:
        nombre, url, marca, precio = next(entrada)
        cont += 1
    print('Nombre:', nombre)
    print('URL:', url)
    print('Marca', marca)
    print('Precio:', precio)


def delete():
    nombre = input('Nombre: ')
    f = open('uno.csv', 'r')
    lineas = f.readlines()
    f.close()

    f = open('uno.csv', 'w')
    for linea in lineas:
        if linea.split(',')[0] != nombre:
            f.write(linea)
    f.close()


def comprobar():
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
            print('Nombre:', nombre, '\nURL:', url, '\nPrecio esperado:', precio)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

            Raw = soup.find(marca, class_=clase)

            Raw = Raw.text.split()

            if double(Raw[0].split(',')[0]) > double(precio):
                print('Todavía no\nPrecio actual:', Raw[0], '\nPrecio objetivo:', precio)
            else:
                print('AHORA\nPrecio actual:', Raw[0], '\nPrecio objetivo:', precio)


while True:
    inp = input('Añadir(a)\nBuscar(b)\nComprobar(c)\nBorrar(del)\nLeerlo todo(l)\nSalit(exit)\nSeleccionar opción: ')

    if inp == 'a':
        write()
    if inp == 'b':
        search()
    if inp == 'del':
        delete()
    if inp == 'l':
        leerTodo()
    if inp == 'exit':
        break
    if inp == 'c':
        comprobar()
