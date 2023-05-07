import numpy as np
from Alumnos import Alumno
import csv

class ManejadorAlumnos:
    def __init__(self):
        self.__alumnos=np.array([],dtype=Alumno)
    
    def cargaAlumnos(self):
        with open("alumnos.csv")as archivo:
            reader=csv.reader(archivo,delimiter=";")
            for fila in reader:
                alumno=Alumno(fila[0],fila[1],fila[2],fila[3],int(fila[4]))
                self.__alumnos=np.append(self.__alumnos,alumno)
          
    def ordena(self):
        return self.__alumnos.sort()
    
    def muestra(self):
        for alumno in self.__alumnos:
            print(alumno)
    
    
    
    
   