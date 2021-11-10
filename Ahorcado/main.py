
from PIL import Image
import random
import time


def __init__(self, *args):
    pass
        
def vida():
    vida.vidas = 5
    vida.adivinadas = []
    print('_'*len(vida.palabra))
    

def listas():

    listas.Chinitas = ["chaeyoung", "lisa", "son chaeyoung", "yeji", "ryujin", "jennie", "jisoo", "nayeon", "dahyun", "chaeryeong"]

    listas.Bandas = ["blackpink", "twice", "itzy"]

def categoria():

        print("¿Desea jugar con integrantes o con bandas de K-pop en general?")
        time.sleep(2)

        categoria.opc = input ("Ingrese A para integrantes \n B para bandas: ")

        while 1:
            if categoria.opc.lower()=="a":
                print("Usted a seleccionado \"Integrantes\".")
                vida.palabra = random.choice(listas.Chinitas)
                break

            elif categoria.opc.lower()=="b":
                print("Usted a seleccionado \"Bandas\".")
                vida.palabra = random.choice(listas.Bandas)
                break

            else:
                print("Por favor seleccione una categoria valida.")
                time.sleep(1)
                categoria.opc = input ("Ingrese A para integrantes \n B para bandas: ")
            


def reglas():
        print("Bienvenido al juego del ahorcado")
        time.sleep(2)
        print("El objetivo del juego es adivinar el nombre de la artista o banda letra por letra")
        print("Tienes 5 vidas, pierdes una cada vez que te equivocas")
        time.sleep(2)

def logistica():
    while 1:
     
        while 1:
            adivinada = input("Adivina una letra: ")
            if(len(adivinada)!=1 and adivinada.isnumeric()):
                print("Eso no es una letra intenta con una sola letra")
            else:
                if adivinada.lower() in vida.adivinadas:
                    print("Ya habias intentado con esa letra intenta con otra por favor")
                else:
                    vida.adivinadas.append(adivinada)
 
                    if adivinada.lower() in vida.palabra:
                        print("Felicidades adivinaste una letra")
                        break
                    else:
                        vida.vidas -= 1
                        print("Te has equivocado y perdido una vida")
                        print("Te quedan " + str(vida.vidas) + " vidas")
                        break
 
        if vida.vidas==0:
            print("Has perdido")
            time.sleep(2)
            if categoria.opc.lower()=="a":
                print("La integrante secreta era: " + vida.palabra)
                break
            else:
                print("La banda secreta era: " + vida.palabra)
                break         
 
 
        estatus_actual = ""
 
        faltantes = 0
        for letra in vida.palabra:
 
 
            if letra in vida.adivinadas:
                estatus_actual += letra
 
            else:
                estatus_actual = estatus_actual + "_"
                faltantes += 1
 
        ## Imprimir palabra con algunas letras
        print(estatus_actual)
 
 
        if faltantes == 0:
            print("Felicidades la descifraste")
            if categoria.opc.lower()=="a":
                print("La integrante secreta es: " + vida.palabra)
                time.sleep(3)
                break
            else:
                print("La banda secreta es: " + vida.palabra)
                time.sleep(3)
                break         
                
def juego():
        listas()
        reglas()
        categoria()
        vida()
        logistica()

if __name__ == "__main__":
        juego()
