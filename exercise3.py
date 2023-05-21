import barcode
import csv
from barcode.writer import   ImageWriter

def gen_code(nombre, id):
    codigo = barcode.get('ean13', id, writer = ImageWriter())
    nombre_archivo = f"{nombre}.png"
    codigo.save(nombre_archivo)

def abrir_csv(archivo):
    with open(archivo, 'r') as file:
        lector = csv.reader(file, delimiter=',')
        for fila in lector:
            nombre = fila[0]
            id = fila[1]
            id = id.lstrip()
            i = len(id)
            for i in range(12-1):
                id = '0' + id
            print(len(id))
            gen_code(nombre, id)

abrir_csv("/home/chema/Documentos/CFGS-DAM/COMPUTER SYSTEMS/THIRD TERM/THIRD-TERM-ASSESABLE-ACTIVITY/alumnos.csv")
