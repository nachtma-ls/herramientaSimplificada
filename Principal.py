import argparse
import os

parser = argparse.ArgumentParser(description="NachOS\nes un programa que permite conocer información básica del sistema operativo")
parser.add_argument('-a','--autor',help="Muestra el nombre del autor del programa %(prog)s", action="store_true")
parser.add_argument('-n','--nombre',help="Muestra el nombre del sistema operativo en el que esta ejecutando el programa", action="store_true")
parser.add_argument('-u','--usuario',help="Muestra el nombre del usuario activo del SO", action="store_true")
parser.add_argument('-l','--limpiar',help="Limpia la consola del sistema Windows", action="store_true")

def Autor():
    print(">>Autor: ISC con EDPI. Nachtma L.")

def NombreSO():
    print(">>",end=" ")
    print(os.name)

def NombreUS():
    print(">>",end=" ")
    print(os.getlogin())

def LimpiarCLI():
    os.system('cls')

if __name__ =="__main__":
    args = parser.parse_args()
    if args.autor:
        Autor()
    elif args.nombre:
        NombreSO()
    elif args.usuario:
        NombreUS()
    elif args.limpiar:
        LimpiarCLI()
    else:
        print("No existe esa opción")
