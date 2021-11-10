#Obtener nombre de file

archivo = input('Ingrese el nombre del archivo: ')

# main.py

part = archivo.split('.')

print(part)

print(part[-1],end='.')