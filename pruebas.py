import os

def crearArchivo(path,size,r,cont):
    # Tamaño en caracteres deseado
    tamano_caracteres = size  # Cambia este valor al tamaño deseado en caracteres

    # Secuencia de números del 0 al 9 en forma de cadena
    secuencia = "0123456789"
    contenido = ""

    if r:
        crear_carpetas_si_no_existen(path)
    
    if cont != "":
        with open(cont, "r") as archivo2:
            contenido = archivo2.read()
            # print(contenido)
            archivo2.close()

        with open(path, "w") as archivo:
            archivo.write(contenido)
            archivo.close()
    else:
        try:
            # Abre un archivo de texto en modo escritura
            with open(path, "w") as archivo:
                caracteres_escritos = 0

                while caracteres_escritos < tamano_caracteres:
                    for digito in secuencia:
                        archivo.write(digito)
                        caracteres_escritos += 1
            print(f"Se ha creado un archivo de texto con {tamano_caracteres} caracteres que contiene la secuencia de números del 0 al 9 en orden.")
        except Exception as e:
            print(f"Error las carpetas que preceden al archivo no existen {path}: {str(e)}")



def crear_carpetas_si_no_existen(path):
    # path = path.replace("\\","/")
    nombre_archivo = os.path.basename(path)
    # print(nombre_archivo)
    path = path.replace(nombre_archivo, "")
    # print(path[:-1])
    try:
        # Intentar crear las carpetas si no existen
        os.makedirs(path)
        print(f"Carpetas creadas en: {path[:-1]}")
    except FileExistsError:
        print(f"Las carpetas ya existen en: {path}")
    except Exception as e:
        print(f"Error al crear carpetas en {path}: {str(e)}")

# # Ingresa la ruta que deseas y llama a la función
# ruta_deseada = "Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\GSS\EXE\IN.txt"
# crear_carpetas_si_no_existen(ruta_deseada)


# crearArchivo("Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\GSS\SUPORT\PAS.txt",52,True,"cont")