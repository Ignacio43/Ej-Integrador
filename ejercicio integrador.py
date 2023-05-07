import numpy as np
from manejadoralumnos import ManejadorAlumnos
from manejadormaterias import ManejadorMaterias


if __name__=='__main__':
   notas_aprobadas=[]
   Notas=[]
   menu=int(input("1.dar promedios sin aplazos y con aplazos    \n2. Estudiantes que aprobaron con nota mayor o igual que 7 de forma promocional  \n3. Listado Ordenado de alumnos  \n4. salir"))
   lista=ManejadorAlumnos()
   lista.cargaAlumnos()
   while menu != 0:
        if menu==1:
            dni=input("ingrese dni del alumno")
            notas=MateriasAprobadas()
            p=notas.notas1(dni)
            for x in p:
                if x>=7:
                    notas_aprobadas.append(x)
                Notas.append(x)
            promedio_aplazo= float(Notas/(len(p)))
            prom_sin_aplazo= float(notas_aprobadas/len(notas_aprobadas))
            print(f"promedio de notas sin aplazos {prom_sin_aplazo}\n")
            print(f"promedio de notas con aplazos {prom_aplazo} \n ")
        elif menu ==2:
            lista1=MateriasAprobadas()
            lista1.CargaMaterias()
            lista1.aprobadoPorPromocion(lista)
        elif menu==3:
            lista.ordena()
            lista.muestra()
        menu=int(input("1.dar promedios sin aplazos y con aplazos    \n2. Estudiantes que aprobaron con nota mayor o igual que 7 de forma promocional  \n3. Listado Ordenado de alumnos  \n4. salir"))
        