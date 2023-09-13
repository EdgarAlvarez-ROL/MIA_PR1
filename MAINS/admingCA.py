from structs import MBR, Particion, EBR, SuperBloque
import struct
import structs
import pickle
import mount as Mount
import os
import time

ultimo_b_inodo = -1

def leerBloquesFinal(path):
    global ultimo_b_inodo
    """ LECTOR DEL SUPERBLOQUE PARA ENCONTRAR LOS STARST """
    mbr_format = "<iiiiB"
    mbr_size = struct.calcsize(mbr_format)
    # partition_format = "c2s3i3i16s"
    partition_format = "c2s3i3i16s"
    partition_size = struct.calcsize(partition_format)
    data = ""

    info_user_txt = ""

    try:
        
            with open(path, "rb") as file:
                mbr_data = file.read(mbr_size)
                particion_data = file.read(partition_size)
                
                """Block Start"""
                superBloque_data = file.read(struct.calcsize("<iiiiiddiiiiiiiiii"))
                superBloque_data = b'\x02\x00\x00\x00)7' + superBloque_data 
                superBloque_data = superBloque_data[:-6]
            # print(superBloque_data)F
                data = struct.unpack("<iiiiiddiiiiiiiiii", superBloque_data)

                block_start = data[16]
                # print(block_start)

                bloques_carpetas = structs.BloquesCarpetas()
                bytes_carpetas= bytes(bloques_carpetas)  # Obtener los bytes de la instancia
                recuperado = bytearray(len(bytes_carpetas))  # Crear un bytearray del mismo tamaño
                

                # print(len(recuperado))
                file.seek(block_start)
                file.readinto(recuperado)
                # print(recuperado)

                data_hex = bytearray(recuperado)
                # Convierte los datos hexadecimales en una lista de bytes
                byte_list = list(data_hex)

                # Imprime la lista de bytes
                # print(byte_list)

                # Define el formato esperado, que incluye una cadena (12s) y un entero (i)
                formato = "12s i"

                # Calcula el tamaño del struct en bytes para leer una vez a la vez
                tamanio_struct = struct.calcsize(formato)

                posicion = 0

                # print(len(data_hex))
                while posicion < len(data_hex):
                    parte = data_hex[posicion:posicion + tamanio_struct]
                    # print(tamanio_struct)
                    # print(len(parte))
                    if len(parte) < tamanio_struct:
                        break  # Si no quedan suficientes bytes para un registro completo, sal del bucle
                    resultado = struct.unpack(formato, parte)
                    cadena, entero = resultado
                    print(f"Name: {cadena.decode('utf-8')} | Inodo: {entero}")
                    if entero != -1:
                        ultimo_b_inodo = entero
                    posicion += tamanio_struct
                    
                # Este código asume que los datos se organizan en registros alternados de 12 bytes para la cadena y 4 bytes para el entero, 
                # lo que corresponde al formato especificado en formato. Puedes ajustar el formato y el procesamiento según la estructura 
                # real de tus datos. Asegúrate de manejar los casos en los que no haya suficientes bytes para un registro 
                # completo o cuando la lectura llegue al final del bytearray.
                file.close()

    except Exception as e:
        print("\tERROR: No se pudo leer el disco en la ruta: " +path+", debido a: "+str(e))

    
    bloque_final = block_start + 128
    # return (bloque_final)

    # Abre un archivo en modo escritura ('w' para escribir, 'a' para agregar al final)
    with open("MAINS/backs/block_final.txt", 'w') as archivo:
        # Escribe una cadena en el archivo
        archivo.write(str(bloque_final))
        # print("Bloque Final Guardado")

    return bloque_final
    """"""
    

def obtenerPP():
    contenido = ""
    with open("MAINS/backs/pp.txt","r") as pp_archivo:
        contenido = pp_archivo.read()
    return int(contenido)

def mkfile(path, ruta_ingresar_archivo, fisrt, user, permisos, uid, gid):
    global ultimo_b_inodo

    
    name_archivo = os.path.basename(ruta_ingresar_archivo)
    ruta = ruta_ingresar_archivo.replace(name_archivo, "")

    # print(name_archivo)
    # print(ruta)

    carpetas = ruta.split("/")
    del carpetas[0]
    del carpetas[-1]
    # print(carpetas)

    bloque_start = 0
    s_inode_start = 0
    if fisrt:
        bloque_start = leerBloquesFinal(path)
        s_inode_start = escribirUltimoPP(path)
    else:
        bloque_start = leerFinalSecond(path)

    s_inode_start = obtenerPP()
    # print(type(bloque_start))
    bloque_start = int(bloque_start)
    # print(type(bloque_start))


    s_inode_start 


    # INFORMACION PA QUE NO CRASHEE
    mbr_format = "<iiiiB"
    mbr_size = struct.calcsize(mbr_format)
    # partition_format = "c2s3i3i16s"
    partition_format = "c2s3i3i16s"
    partition_size = struct.calcsize(partition_format)
    data = ""
    try:
            
            with open(path, "rb+") as file:
                mbr_data = file.read(mbr_size)
                particion_data = file.read(partition_size)
                
                """Block Start"""
                superBloque_data = file.read(struct.calcsize("<iiiiiddiiiiiiiiii"))
                superBloque_data = b'\x02\x00\x00\x00)7' + superBloque_data 
                superBloque_data = superBloque_data[:-6]
                # print(superBloque_data)F
                data = struct.unpack("<iiiiiddiiiiiiiiii", superBloque_data)
                # block_start = data[16]
                # print(block_start)
                bloques_carpetas = structs.BloquesCarpetas()
                bytes_carpetas= bytes(bloques_carpetas)  # Obtener los bytes de la instancia
                recuperado = bytearray(len(bytes_carpetas))  # Crear un bytearray del mismo tamaño
                
                """ AQUI SE EMPIEZA A ESCRIBIR LA INFO DE LA CARPETA """
                """                                                  """

                

                # CREANDO INODES PARA LAS CARPETAS Y LOS BLOQUES
                block_carpeta = structs.BloquesCarpetas()
                bytes_block_carpeta = bytes(block_carpeta)
                
                block_archivos = structs.BloquesArchivos()
                bytes_block_archivo = bytes(block_archivos)
                block_archivos.b_content = ""

                

                ultimo_b_inodo += 1
                for indice, valor in enumerate(carpetas):
                    print(str(ultimo_b_inodo) + " - "+ (valor))
                    if indice == 4:
                        break
                    if indice == len(carpetas) - 1:
                        print(str(ultimo_b_inodo+1) + " - " + name_archivo)
                        block_carpeta.b_content[0].b_name = name_archivo
                        block_carpeta.b_content[0].b_inodo = ultimo_b_inodo+1
                        
                        # inodo de la carpeta
                        inode = structs.Inodos()
                        inode.i_uid = int(uid)
                        inode.i_gid = int(gid)
                        inode.i_size = 0
                        inode.i_atime = int(time.time())
                        inode.i_ctime = int(time.time())
                        inode.i_mtime = int(time.time())
                        inode.i_type = 0
                        inode.i_perm = int(permisos)

                        for _ in inode.i_block:
                            if _ == -1:
                                inode.i_block[cont] = ultimo_b_inodo + 1 
                        # print(inode.i_block)

                        with open(path, "rb+") as bfiles:
                            bfiles.seek(s_inode_start)
                            bfiles.write(bytes(inode))
                        
                        s_inode_start += 101

                        
                        """Inodo Archivo"""
                        inode.i_type = 1
                        inode.i_size = 0
                        inode.i_block[0] = 0
                        with open(path, "rb+") as bfiles:
                            bfiles.seek(s_inode_start)
                            bfiles.write(bytes(inode))
                        
                        s_inode_start += 101
                        escribirUltimoPP(path)
                            
                        
                    else:

                        # print(ultimo_b_inodo)
                        # print("salir")

                        block_carpeta.b_content[indice].b_name = valor
                        block_carpeta.b_content[indice].b_inodo = ultimo_b_inodo
                        
                        # print(type(ultimo_b_inodo))
                        # print(ultimo_b_inodo)

                        inode = structs.Inodos()
                        inode.i_uid = int(uid)
                        inode.i_gid = int(gid)
                        inode.i_size = 0
                        inode.i_atime = int(time.time())
                        inode.i_ctime = int(time.time())
                        inode.i_mtime = int(time.time())
                        inode.i_type = 0
                        inode.i_perm = int(permisos)
                        
                        cont = 0
                        for _ in inode.i_block:
                            if _ == -1:
                                inode.i_block[cont] = ultimo_b_inodo + 1 

                        # inode.i_block[indice]  = ultimo_b_inodo+1

                        
                        # print(inode.i_block)
                        ultimo_b_inodo += 1

                        with open(path, "rb+") as bfiles:
                            bfiles.seek(s_inode_start)
                            bfiles.write(bytes(inode))

                        s_inode_start += 101
                        """"""
                
                # for _ in block_carpeta.b_content:
                #     print(_.b_name)
                # print(block_archivos.b_content)
                # print("===========")
                # print(inode.i_block)

                file.seek(bloque_start)
                file.write(bytes(block_carpeta))
                file.write(bytes(block_archivos))

    except Exception as e:
        print("\tERROR: No se pudo leer el disco en la ruta: " +path+", debido a: "+str(e))
    
    bloque_final = bloque_start + 128
    # Abre un archivo en modo esc
    # ritura ('w' para escribir, 'a' para agregar al final)
    with open("MAINS/backs/block_final.txt", 'w') as archivo:
        # Escribe una cadena en el archivo
        archivo.write(str(bloque_final))
        # print("Bloque Final Guardado")
    """"""
    
def leerFinalSecond(path):
    contenido = ""
    with open("MAINS/backs/block_final.txt", 'r') as archivo:
        # Escribe una cadena en el archivo
        contenido = archivo.read()
        # print("Bloque Final Guardado")
    return contenido

def escribirUltimoPP(path):
    """ LECTOR DEL SUPERBLOQUE PARA ENCONTRAR LOS STARST """
    mbr_format = "<iiiiB"
    mbr_size = struct.calcsize(mbr_format)
    # partition_format = "c2s3i3i16s"
    partition_format = "c2s3i3i16s"
    partition_size = struct.calcsize(partition_format)
    data = ""
    pp = 0
    try: 
        with open(path, "rb") as file:
            mbr_data = file.read(mbr_size)
            particion_data = file.read(partition_size)
            superBloque_data = file.read(struct.calcsize("<iiiiiddiiiiiiiiii"))
            # print(particion_data)
            mbr = MBR()
            (mbr.mbr_tamano, mbr.mbr_fecha_creacion, mbr.mbr_disk_signature, disk_fit, mbr.mbr_Partition_1, *_) = struct.unpack(mbr_format, mbr_data)
            mbr.disk_fit = chr(disk_fit % 128)
            partition1 = Particion()
            particion_data = b'1PW'+ particion_data
            particion_data = particion_data[:-2]
            # print("PARTICON DATA")
            # print(particion_data)
            partition1.__setstate__(particion_data)
            """==================================="""
            # print(superBloque_data)
            # super_Bloque = SuperBloque()
            superBloque_data = b'\x02\x00\x00\x00)7' + superBloque_data 
            superBloque_data = superBloque_data[:-6]
            # print(superBloque_data)
            data = struct.unpack("<iiiiiddiiiiiiiiii", superBloque_data)
            # print(superBloque_data)
            # print("============================")
            """==================================="""

            
            file.close()
    except Exception as e:
        print("\tERROR: No se pudo leer el disco en la ruta: " +path+", debido a: "+str(e))

    pp = int(data[15])
    inode = structs.Inodos()  # Crear una instancia de SuperBloque
    bytes_inodo= bytes(inode)  # Obtener los bytes de la instancia
    recuperado = bytearray(len(bytes_inodo))  # Crear un bytearray del mismo tamaño

    bandera = 0
    while bandera != -1:
        with open(path, "rb") as archivo:
            print(pp)
            archivo.seek(pp)
            archivo.readinto(recuperado)

            inode.__setstate__(recuperado)
            print(inode.i_perm)
            
            if inode.i_uid == -1:
                bandera = -1
            else:
                pp = pp + len(recuperado) 
        archivo.close()

    with open("MAINS/backs/pp.txt","w") as pp_archivo:
        pp_archivo.write(str(pp))

        """"""  





"""================================== PRUEBAS ================================== """
path = r"C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk"

# bloqueFinal = leerBloquesFinal(path)
# print(bloqueFinal)


mkfile(path,r"/home/user/puta.txt",True,"rol","555","2","2")
# escribirUltimoPP(path)