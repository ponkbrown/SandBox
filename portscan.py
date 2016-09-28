#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

#Limpiar la pantalla
subprocess.call('clear', shell=True)

# Preguntar por el host

remoteServer = input('Host para escanear: ')
remoteServerIP = socket.gethostbyname(remoteServer)

# Imprime un banner de escaneo
print('=' * 60)
print("Espera mientras se escanea el host", remoteServer)
print('=' * 60)

# La hora a la que empezo el scan
t1 = datetime.now()

# Usando la funcion range especificar los puertos a escanear (del 1 al 1024)
# Tambien lidea con algunos errores

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Puerto {}:  Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Saliendo (Ctrl+C)")
    sys.exit()

except socket.gaierror:
    print("No se encontro el Host. saliendo...")
    sys.exit()

except socket.error:
    print("No se puede conectar al host. saliend...")

# Revisa el tiempo otra vez
t2 = datetime.now()

# Calcula la diferencia de tiempo
total = t2 - t1

#Imprimimos la informacion
print("Terminado, tiempo total:", total)
