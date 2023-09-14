import os

class RmDisk:
    def __init__(self):
        self.path = ''

    def remove(self):

        if self.path:
            if self.path.startswith("\"") and self.path.endswith("\""):
                self.path = self.path[1:-1]
            
            try:
                if os.path.isfile(self.path):
                    if not self.path.endswith(".dsk"):
                        print("\t==== El archivo no tiene la extension correcta ====")
                    
                    confirmacion = input("\t---- Esta seguro que desea eliminar el disco Y/N: ")

                    if confirmacion == 'Y' or confirmacion == 'y' or confirmacion == '1':
                        # os.remove(self.path)
                        # 
                        # Verificar si el archivo existe
                        if os.path.exists(self.path):
                            # El archivo existe, intentar eliminarlo
                            try:
                                os.remove(self.path)
                                print(f"El archivo {self.path} ha sido eliminado.")
                            except OSError as e:
                                print(f"Error al eliminar el archivo {self.path}: {e}")
                        else:
                            # El archivo no existe
                            print(f"El archivo {self.path} no existe y no se puede eliminar.")
                        # 
                        print("\t==== Disco eliminado correctamente ====")
                    else:
                        print("\t==== El Disco no se borro [no se preocupe, todo bien ;) ] ====")

                else:
                    print("\t==== El disco ingresado NO existe ====")
            
            except Exception as e:
                print("\t==== Error al intentar eliminar el Disco ====")