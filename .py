import os 

menu = """
1. agregar mascota
2.lista de mascotas registradas
3.imprimir la fecha de registro
4.salir del programa """

ESPECIES =["perro, gato, ave," ]
MATRIZ = []
TITULOS = """
| nombre   | especie  | peso  | costo inicial
"""

def agregarMascota():
    while True:
        try:
            nom = input("ingrese nombre: ")
            especie =input("ingrese la especie de la mascota:")
            peso = int(input)("ingrese peso de la mascota: ")
            costo_inicial = int(input("ingrese el costo inicial"))
            if len(nom) > 0 and especie in ESPECIES and peso > 0:
                impuesto_salud = round (costo_inicial  * 0.05)
                costo_inicial = round (costo_inicial + impuesto_salud)
                MATRIZ.append([nom, especie, peso, costo_inicial, impuesto_salud])
                input("maacota registrada con exito")
                break
        except:
            input("excepcion de menu")

def listarEspecies(especie):
    salida = TITULOS
    for row in MATRIZ:
        salida += f"{row[0]:8s}"
        salida += f"{row[1]:8s}"
        salida += f"{row[2]:8d}"
        salida += f"{row[3]:8d}"
        salida += f"{row[4]:8d}"
        salida += f"{row[5]:8d}"
    return salida
input("desea volver al menu?")




            


       