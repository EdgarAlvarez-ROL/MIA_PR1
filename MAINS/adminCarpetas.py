import os
import shutil
from WR import *

def crearArchivo(path_del_disco,path,size,r,cont,usuario,permisos,uid,gid,bandera_mkfile,newPP,newBLOCKStart):
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
                cont = 0
                while caracteres_escritos < tamano_caracteres:
                        if cont > 9:
                            cont = 0
                        archivo.write(secuencia[cont])
                        caracteres_escritos += 1
                        cont += 1
            print(f"Se ha creado el archivo de texto con {tamano_caracteres} bytes que contiene la secuencia de números del 0 al 9.")
        except Exception as e:
            print(f"Error las carpetas que preceden al archivo no existen {path}: {str(e)}")
        
        
        # SECCION DEL BLOQUE ARCHIVO E INODO
        archivo = 1
        pp = -1
        block = -1
        if bandera_mkfile:
            aa, bb = mkfileInodo(path_del_disco,path,usuario,permisos,archivo,uid,gid,newPP,newBLOCKStart)
        else:
            aa, bb = mkfileInodo(path_del_disco,path,usuario,permisos,archivo,uid,gid,"","")
        pp = aa
        block = bb
        
        return pp, block
        """"""


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

def otro(carpeta):
    # carpeta = carpeta.replace("\\","\\\\")
    print(carpeta)
    for archivo in os.listdir(carpeta):
        print(archivo)


def cat(lista):
    for data in lista:
        path = data[1]

        # print(path)

        with open(path, "r") as archivo2:
                contenido = archivo2.read()
                # print(contenido)
                archivo2.close()
        
        print(contenido)


def remover(path):
    print()

# crearArchivo(r"C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\G\sxaa.txt",13,True,"")
# otro(r"C:\Users\wwwed\OneDrive\Escritorio\pruebas_todoTipo\Organizers")

# lista = [1,0,0,1,5,8,8]
# cat(lista)


# def wr_Inodes(path):
#     try:            
#         with open(path, "rb+") as bfiles:art)
#             bfiles.write(bytes(inode))
#             bfiles.write(bytes(inodetmp))
            
#             print(bytes(inode))
#             print(bytes(inodetmp))

#             bfiles.seek(spr.s_block_start)
#             bfiles.write(bytes(fb))
#             bfiles.write(bytes(fileb))
#     except Exception as e:
#             print(e)


