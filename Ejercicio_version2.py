def validarnum(x):
    while True:
      try:
        a= int(input(x))
        return a
      except ValueError:
        print("Solo se permiten números, intente de nuevo")

def validaren(x):
  while True:
    try:
      a= input(x)
      print(any(char.isdigit() for char in a))
      if any(char.isdigit() for char in a) == False:
        return a
      else:
        print("Solo se permiten carácteres alfanuméricos, intente de nuevo")
        continue
    except:
      print("Solo se permiten carácteres alfanuméricos, intente de nuevo")
      continue



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

    def getPacientes(self):
      return self.__lista_pacientes

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
        op= int(input('Ingrese:\n 1. Ingresar paciente.\n 2. Ver paciente.\n 3. Numero de pacientes.\n 4. Salir:\n'))
        if op == 1:
            print("Ingrese los siguentes datos: ")
            nombre= validaren("Nombre: ")
            ce= validarnum('Cedula: ')
            ge= validaren('Género: ')
            se= validaren("Servicio: ")
            pac= Paciente()
            pac.asignarCedula(ce)
            pac.asignarGenero(ge)
            pac.asignarNombre(nombre)
            pac.asignarServicio(se)
            ingreso_paciente = sis.ingresarPaciente(pac)
            if ingreso_paciente:
                print("El paciente se ha ingresado con éxito")
            else:
                print("Ha ocurrido un error")
            #print(pac)
        elif op ==2:
            cedula = int(input("Ingrese la cedula a buscar: "))
            p= sis.verDatospacientes(cedula)
            #print(sis)
            print("Nombre: " + p.verNombre())
            print("Cedula: " + str(p.verCedula()))
            print("Genero: " + p.verGenero())
            print("Servicio: " + p.verServicio())

        elif op== 3:
          sis.verNumeroPacientes()
        elif op != 4 :
            print("Opción no válida")
            continue
        elif op== 4:
            break

main()