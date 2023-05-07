import csv
from MateriasAprobadas import MateriasAprobadas

class ManejadorMaterias:
    def __init__(self):
        self.__list=[]
        
    def cargaMaterias(self):
        with open("materiasAprobadas.csv")as archivo:
            reader=csv.reader(archivo,delimiter=";")
            for fila in reader:
                materia=MateriasAprobadas(fila[0],fila[1],fila[2],fila[3])
                self.__list.append(materia)
                
    def notas1(self,dni):
        dni=input("ingrese dni del alumno a buscar \n")
        notas=[]
        for x in self.__list:
            if x.getDni() == dni:
                notas.append(x.getNota())
        return notas
            
            
    def aprobadoPorPromocion(self,lista):
        i=0
        materia=input("ingrese el nombre de la materia ")
        print("DNI      Apellido y Nombre     Fecha      Nota      Año Cursa")
        for x in self.__lista:
            i=0
            while lista[i].getDNI() != x.getDni() and i<len(lista):
                i=i+1
            if lista[i].getDNI() == x.getDni()
                if x.getNota()>=7 and x.getAprobacion()== 'P' and x.getNombreMateria()==materia:
                    print(f"{x.getDni()}    {lista[i].getNombre()} {lista[i].getApellido()}      {x.getFecha()}     {x.getNota()}         {lista[i].getAnioCursa()} ")
        
        
    

        