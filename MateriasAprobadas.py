class MateriasAprobadas:
    def __init__(self,dni,nombreMateria,fecha,nota,aprobacion):
        self.__dni=dni
        self.__nombreMateria=nombreMateria
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=aprobacion
    
    def getNota(self):
        return self.__nota
    
    def getNombreMateria(self):
        return self.__nombreMateria
    
    def getAprobacion(self):
        return self.__aprobacion
    
    def getDni(self):
        return self.__dni
    
    def getFecha(self):
        return self.__fecha
    
    
   
        