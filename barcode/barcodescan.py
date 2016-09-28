# Escaneador de codigos de barra, nomas los escanea y los anexa a una base de datos
# con su respectiva fecha y es todo
from sql_insert import dbinsert
from menu import menu, logo
from datetime import date

def scan(cliente):
    print(chr(27) +"[2J")
    print('Escaneando para: '+cliente)
    print('Fecha'+str(date.today())+'\n')
    seguir = 'Yes'
    codigos = []
    while seguir:
        print("'S' para salir")
        scan = input()
        if scan.upper() == 'S':
            seguir = None
        else:
            dbinsert(cliente,scan)
            codigos.append(str(scan))

    return (codigos)

def main():
    logo()
    item = menu()
    if item == 'Agregar':
        print('Agregar')
        exit
    else:
       codigos = scan(item)
       print(chr(27) +"[2J")
       print('Se escanearon los codigos: \n'+str(codigos))
       print ('='*80)
       print ('Codigos escaneados  Total:' + str(len(codigos))+'\n\n')
       input()

while True:
    main()
