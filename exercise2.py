import os
import shutil as sh

direc = os.getcwd()
lsdir = os.listdir(direc)
extensions = []
ext_final = []

def create_directory(a):
    ext = a.replace(".", "")
    folder = os.getcwd()+ "/" + ext + "/"
    lsdir = os.listdir(os.getcwd())
    for i in lsdir:
        if os.path.isdir(ext):
            if os.path.isfile(i) and ext in i:
                if i != "exercise2.py":
                    sh.move(i, folder + i)
        else:
            os.mkdir(ext)
            


for i in lsdir:
    archivo, ext = os.path.splitext(i)
    extensions.append(ext)

extensions = list(set(extensions))

for i in extensions:
    if i == "":
        extensions.pop(extensions.index(i))

#RECORDATORIO: MODIFICAR PARA PASAR UNA LISTA COMO PARÁMETRO
for i in extensions:
    create_directory(i)