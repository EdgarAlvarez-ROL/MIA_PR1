import os
import pickle

class Profesor:
    def __init__(self, tipo_p, id_p, cui_p, nombre_p, curso_p):
        self.tipo_p     = tipo_p 
        self.id_p       = id_p 
        self.cui_p      = cui_p 
        self.nombre_p   = nombre_p 
        self.curso_p    = curso_p 
        

class Estudiante:
    def __init__(self, tipo_e, id_e, cui_e, nombre_e, carnet_e):
        self.tipo_e     = tipo_e
        self.id_e       = id_e
        self.cui_e      = cui_e
        self.nombre_e   = nombre_e
        self.carnet_e   = carnet_e


def guardar(data, path):
    with open(path, 'ab') as file:
        pickle.dump(data, file)

def es_vacio(path):
    return os.path.getsize(path) == 0
    print("")

def leer_archivo(path):
    with open(path, 'rb') as file:
        try:
            while True:
                data = pickle.load(file)              

                if isinstance(data, Profesor):
                    print("-------------------------------------")
                    print("Tipo Profesor: ", data.tipo_p)
                    print("ID Profesor: ", data.id_p)
                    print("CUI Profesor: ", data.cui_p)
                    print("Nombre Profesor: ", data.nombre_p)
                    print("Curso Profesor: ", data.curso_p)
                    print("-------------------------------------\n")
                if isinstance(data, Estudiante):
                    print("-------------------------------------")
                    print("Tipo Estudiante: ", data.tipo_e)
                    print("ID Estudiante: ", data.id_e)
                    print("CUI Estudiante: ", data.cui_e)
                    print("Nombre Estudiante: ", data.nombre_e)
                    print("Carnet Estudiante: ", data.carnet_e)
      
                    print("-------------------------------------\n")
        except EOFError:
            pass

def main():
    # AQUI INICIA EL PROGRAMA
    path = "registros_profesor_estudiante.bin"

    # Validacion si el archivo ya existe
    if not os.path.exists(path):
        # Si no existe lo cera
        open(path, 'wb').close()

    while True:
        print("MENU PRINCIPAL")
        print("1. Registro de Profesores")
        print("2. Registro de Estudiantes")
        print("3. Ver Registros")
        print("4. Salir")

        opcion = input("Ingrese su opcion: ")

        if opcion == '1':
            print("Se ingreso al registro de Profesores")
            tipo_p = input("Ingrese el tipo de Profesor: ")
            id_p = input("Ingrese el ID del profesor: ")
            cui_p = input("Ingrese el CUI del Profesor: ")
            nombre_p = input("Ingrese el Nombre del Profesor: ")
            curso_p = input("Ingrese el Curso del Profesor: ")

            profesor = Profesor(tipo_p, id_p, cui_p, nombre_p, curso_p)
            guardar(profesor, path)

        if opcion == '2':
            print("Se ingreso al registro de Estudiantes")
            tipo_e = input("Ingrese el tipo de Estudiante: ")
            id_e = input("Ingrese el ID del Estudiante: ")
            cui_e = input("Ingrese el CUI del Estudiante: ")
            nombre_e = input("Ingrese el Nombre del Estudiante: ")
            carnet_e = input("Ingrese el Curso del Estudiante: ")
            
            estudiante =Estudiante(tipo_e, id_e,cui_e, nombre_e, carnet_e)
            guardar(estudiante, path)

        if opcion == '3':
            print("Se ingreso a la opcion de ver Registros")
            if es_vacio(path):
                print("NO existen registros \n")
            else:
                leer_archivo(path)
        if opcion == '4':
            print("SALIENDO")
            break




if __name__ == "__main__":
    main()