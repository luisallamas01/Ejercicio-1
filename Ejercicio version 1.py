class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
      self.__lista_pacientes = []
    #   self.__lista_pacientes = {}
      self.__numero_pacientes = len(self.__lista_pacientes)
      
    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)
        return True
    def verDatospacientes( self, c):
        for i in self.__lista_pacientes:
            if c == i.verCedula():
                return i
            
       # self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + "pacientes")
        return self.__numero_pacientes
               
def main():
    sis=Sistema()
    while True:
        op= int(input('''Ingrese:  
                            1.Ingresar paciente.
                            2.Ver paciente
                            3.Salir:  '''))
        if op == 1:
            print("A continuación se solicitan los datos: ")
            nombre= input("Ingrese nombre: ")
            ce= int(input("Ingrese cédula: "))
            ge= input("Ingrese género: ")
            se= input("Ingrese el servicio: ")
            pac= Paciente()
            pac.asignarCedula(ce)
            pac.asignarGenero(ge)
            pac.asignarNombre(nombre)
            pac.asignarServicio(se)
            sis.ingresarPaciente(pac)
            if sis.ingresarPaciente(pac) == True:
                print("El paciente se ha ingresado con éxito")
            else:
                print("Ha ocurrido un error")
            #print(pac)
        elif op ==2:
            cedula = int(input("Ingrese la cedula a buscar: "))
            p= sis.verDatospacientes(cedula)
            print("Nombre: " + p.verNombre())
            print("Cedula: " + str(p.verCedula()))
            print("Genero: " + p.verGenero())
            print("Servicio: " + p.verServicio())
        elif op != 3 :
            print("Opción no válida")
            continue
        elif op== 3:
            break
print('hi')
main()


