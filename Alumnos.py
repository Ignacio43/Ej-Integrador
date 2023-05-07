

class Alumno:
    def __init__(self,dni,apellido,nombre,carrera,anioCursa):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__carrera=carrera
        self.__anioCursa=anioCursa
        
    def getAnioCursa(self):
        return self.__anioCursa
    
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def __lt__(self, otro_alumno):
        if self.anio_cursa == otro_alumno.anio_cursa:
            return (self.apellido, self.nombre) < (otro_alumno.apellido, otro_alumno.nombre)
        else:
            return self.anio_cursa < otro_alumno.anio_cursa