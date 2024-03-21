import sys
import os

#Parametros del usuario
nombre_archivo = sys.argv[1]
palabra_clave = sys.argv[2]
#Nombre fichero salida
nombre_archivo_salida = f"{nombre_archivo}_filtrado"

#Se abre en modo lectura el fichero original y escritura el de salida
#Se procede a la busqueda de las líneas que incluyan el nombre y se
#escriben en el fichero de salida
with open(nombre_archivo, 'r') as f_entrada, open(nombre_archivo_salida, 'w') as f_salida:
    for linea in f_entrada:
        if palabra_clave in linea:
            f_salida.write(linea)

print("Búsqueda finalizada. Resultados guardados en", nombre_archivo_salida)
