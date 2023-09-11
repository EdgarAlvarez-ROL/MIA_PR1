from structs import MBR, Particion, EBR, SuperBloque
import struct
import structs
import pickle
import mount as Mount
import fdisk2
import os
import datetime
import time


def mkfileInodo(path,usuario,permiso):
    mbr_format = "<iiiiB"
    mbr_size = struct.calcsize(mbr_format)
    # partition_format = "c2s3i3i16s"
    partition_format = "c2s3i3i16s"
    partition_size = struct.calcsize(partition_format)
    data = ""
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


        pp = data[15]
        startpp = pp

        block_start = data[16]
        startbs = block_start


        """ INODES """
        # print(startpp)
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
        """"""

        """INGRESO DE EL NUEVO INODE"""
        carpeta = r"C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\TXTS"  # Reemplaza esto con la ruta de la carpeta que deseas medir
        tamano_bytes = obtener_tamano_carpeta(carpeta)

        inodeNuevo = structs.Inodos()
        inodeNuevo.i_uid   = 1
        inodeNuevo.i_gid   = 1
        inodeNuevo.i_size  = tamano_bytes
        inodeNuevo.i_atime = int(time.time())
        inodeNuevo.i_ctime = int(time.time())
        inodeNuevo.i_mtime = int(time.time())
        inodeNuevo.i_block[0] = 1
        inodeNuevo.i_type  = 0
        inodeNuevo.i_perm  = permiso

        # inodeBlanco = structs.Inodos()
        # INGRESO DEL INODO DE CARPETA  LA PARTICION
        # pp = pp - 101
        # print(f"entramos a escribir {pp}")
        # print(path)

        # with open(path, "rb+") as bfiles:
        #         bfiles.seek(pp)
        #         bfiles.write( bytes(inodeNuevo))
        #         # bfiles.write(bytes(inodeBlanco))
        #         print("cerrmaso")
        #         bfiles.close()
        
        # print("")
        # bandera = 0
        # while bandera != -1:
        #     with open(path, "rb") as archivo:
        #         print(startpp)

        #         archivo.seek(startpp)
        #         archivo.readinto(recuperado)

        #         inode.__setstate__(recuperado)
        #         print(inode.i_perm)
        #         print(inode.i_size)
                
        #         if inode.i_uid == -1:
        #             bandera = -1
        #         else:
        #             startpp = startpp + len(recuperado) 
        #     archivo.close()
        """"""
        """ CONTAR BLOQUES CARPETA Y RETORNAR SU FINAL """
        cc = leerBloquesCarpetas(block_start)
        # print(c)
        """"""
        
        """Lector Bloque ARCHIVOS """
        bloque_archivo = structs.BloquesCarpetas()
        bytes_archivos= bytes(bloque_archivo)  # Obtener los bytes de la instancia
        recuperado = bytearray(len(bytes_archivos))  # Crear un bytearray del mismo tamaño
        
        try:            
            with open(path, "rb") as bfiles3:
                bfiles3.seek(block_start+len(recuperado))
                bfiles3.readinto(recuperado)
                bloque_archivo.b_content[0].b_name = recuperado[:64].decode('utf-8').rstrip('\0')
                print("safasdfa")
                print(bloque_archivo.b_content[0].b_name)
                print("safasdfa")
                
        except Exception as e:
            print(e)
        """"""

        # cc, recu_bloc_carpetas = leerBloquesCarpetas(block_start)
        

    except Exception as e:
        print("\tERROR: No se pudo leer el disco en la ruta: " +path+", debido a: "+str(e))



def obtener_tamano_carpeta(carpeta):
    total_tamano = 0
    for dirpath, dirnames, filenames in os.walk(carpeta):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_tamano += os.path.getsize(filepath)
    return total_tamano


def leerBloquesCarpetas(block_start):
    """ LEER LAS LISTA DE BLOQUES DE CARPETAS Y ARCHIVOS"""
    bloques_carpetas = structs.BloquesCarpetas()
    bytes_carpetas= bytes(bloques_carpetas)  # Obtener los bytes de la instancia
    recuperado = bytearray(len(bytes_carpetas))  # Crear un bytearray del mismo tamaño
    # recuperado = len(bytes(structs.BloquesCarpetas())) 
    contador_content = 0
    init_recu = 0
    # print(len(recuperado))
    bandera = 0
    try:
        while bandera != -1:
            with open(path, "rb") as bfiles:
                if init_recu >= len(recuperado):
                    bandera = -1
                bfiles.seek(block_start)
                bfiles.readinto(recuperado)

                bloques_carpetas.b_content[contador_content].b_name = recuperado[init_recu:init_recu+16].decode('utf-8').rstrip('\0')
                init_recu += 16
                bloques_carpetas.b_content[contador_content].b_inodo = struct.unpack("<i", recuperado[init_recu-4:init_recu])[0]

                
                print(bloques_carpetas.b_content[contador_content].b_name)
                print(bloques_carpetas.b_content[contador_content].b_inodo)
                contador_content += 1
                # bandera = -1
                bfiles.close()
    except Exception as e:
        str(e)
        print(f"Bloques Carpeta total: {contador_content}")
        # print(contador_content)
        return contador_content
    """"""


path = r'C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk'
mkfileInodo(path,"rol",444)