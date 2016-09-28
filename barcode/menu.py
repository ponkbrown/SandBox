# Parte del programa para escanear codigs de barra
# esta es la parte del menu
# sencillo el script pero que funcione

import collections
from time import sleep

def logo():
    print(chr(27) + "[2J")
    print(r'''
    | |__   __ _ _ __ ___ ___   __| | ___
    | '_ \ / _` | '__/ __/ _ \ / _` |/ _ \
    | |_) | (_| | | | (_| (_) | (_| |  __/
    |_.__/ \__,_|_|  \___\___/ \__,_|\___| v.0.0.0.1

    ''')

def menu():
    global menu_items
    menu_items ={1:'Zazzle', 2:'Otro Zazzle'}
    menu_sistema= {'#' : 'Agregar', 's':'Salir', 'e':'Enviar Reporte'}
    od = collections.OrderedDict(sorted(menu_items.items()))

    while True:
        print('Cliente:\n')
        for a, x in od.items():
            print(str(a)+') '+menu_items[a])
        print('\n')
        for a in menu_sistema:
            print(str(a)+') '+menu_sistema[a])
        select = input()

        if select == ('s' or 'S'):
            select = 's'
            select = menu_sistema[select]
            quit()
        elif select == ('#'):
            select = '#'
            select = menu_sistema[select]
            break
        elif select ==('e' or 'E'):
            select = 'e'
            select = menu_sistema[select]
        else:
            try:
                select = int(select)
                select = menu_items[select]
                break
            except:
                logo()
                print('Selecciona una opcion del menu')
                pass
    return(select)
