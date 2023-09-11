from structs import MBR, Particion, EBR, SuperBloque
import struct
import structs
import pickle
import mount as Mount
import fdisk2

class reporte:
    def __init__(self):
        self.path = ''

    def rep(self):
        if self.path:
            if self.path.startswith("\"") and self.path.endswith("\""):
                self.path = self.path[1:-1]

        try: 
            mbr_format = "<iiiiB"
            mbr_size = struct.calcsize(mbr_format)

            # partition_format = "c2s3i3i16s"
            partition_format = "c2s3i3i16s"
            partition_size = struct.calcsize(partition_format)
            # print(particion_size)
            tamanioSuperBloque = struct.calcsize("<iiiiiddiiiiiiiiii")
            data = ""
            with open(self.path, "rb") as file:
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
                # print("============================")
                # print(superBloque_data)
                super_Bloque = SuperBloque()
                
                # print(len(superBloque_data))
                # data = struct.unpack("<iiiiiddiiiiiiiiii", superBloque_data)
                superBloque_data = b'\x02\x00\x00\x00)7' + superBloque_data 
                superBloque_data = superBloque_data[:-6]
                # print(superBloque_data)
                data = struct.unpack("<iiiiiddiiiiiiiiii", superBloque_data)
                # print(data)
                # print("============================")
                """==================================="""
                # lo que deberia
                # b'\x02\x00\x00\x00)7\x00\x00{\xa5\x00\x00{\xa5\x00\x00)7\x00\x00\x00\x00@\xd2\xfb>\xd9A\x00\x00@\xd2\xfb>\xd9A\x01\x00\x00\x00S\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\x00\x00\xad7\x00\x00(\xdd\x00\x00\xb1\xc3\x15\x00'
                # b'                  \x00\x00{\xa5\x00\x00{\xa5\x00\x00)7\x00\x00\x00\x00@\xd2\xfb>\xd9A\x00\x00@\xd2\xfb>\xd9A\x01\x00\x00\x00S\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\x00\x00\xad7\x00\x00(\xdd\x00\x00\xb1\xc3\x15\x00\x0011000'
                # lo que salio

                # if superBloque_data == b'\x02\x00\x00\x00)7\x00\x00{\xa5\x00\x00{\xa5\x00\x00)7\x00\x00\x00\x00@\xd2\xfb>\xd9A\x00\x00@\xd2\xfb>\xd9A\x01\x00\x00\x00S\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\x00\x00\xad7\x00\x00(\xdd\x00\x00\xb1\xc3\x15\x00':
                    # print("chupala")

                # Data es la info del superbloque
                # print("###########################")
                # b'\x01\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x80k\x06?\xd9A\x00\x00\x80k\x06?\xd9A\x00\x00\x80k\x06?\xd9A\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x98\x02\x00\x00'
                # b'\x01\x00\x00\x00\x01\x00\x00\x00[\x00\x00\x00\x00\x00\x80k\x06?\xd9A\x00\x00\x80k\x06?\xd9A\x00\x00\x80k\x06?\xd9A\x01\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x98\x02\x00\x00'
                # print("###########################")
                # 
                file.close()
            
           

            print("\t============ MBR \t============")
            print("\tMBR tamaño:", mbr.mbr_tamano)
            print("\tMBR fecha creación:", mbr.mbr_fecha_creacion)
            print("\tDisco fit:", mbr.disk_fit)
            print("\tMBR disk signature:", mbr.mbr_disk_signature)

            print("\t============ PARTICION 1 ============")
            print("\tMBR Particion 1-NAME: ", partition1.part_name)
            

            pp = data[15]
            self.replicaa(pp)
        except Exception as e:
            print("\tERROR: No se pudo leer el disco en la ruta: " + self.path+", debido a: "+str(e))


    

    def replicaa(self, p):
        try:
            inode = structs.Inodos()  # Crear una instancia de SuperBloque
            bytes_inodo= bytes(inode)  # Obtener los bytes de la instancia

            recuperado = bytearray(len(bytes_inodo))  # Crear un bytearray del mismo tamaño
            # print(recuperado)
            tamanoInodos = struct.calcsize("<iiiddd15ici") 

            with open(self.path, "rb") as archivo:
                archivo.seek(p)
                archivo.readinto(recuperado)
                # inodos_data = archivo.read(101)
            
            # Desempaquetar los datos del bytearray recuperado
            inode.i_uid   = struct.unpack("<i", recuperado[:4])[0]
            inode.i_gid   = struct.unpack("<i", recuperado[4:8])[0] 
            inode.i_size  = struct.unpack("<i", recuperado[8:12])[0]
            inode.i_atime = struct.unpack("<d", recuperado[12:20])[0]
            inode.i_ctime = struct.unpack("<d", recuperado[20:28])[0]
            inode.i_mtime = struct.unpack("<d", recuperado[28:36])[0]
            inode.i_block = struct.unpack("<15i", recuperado[36:96])
            inode.i_type  = struct.unpack("<c", recuperado[96:97])[0] #recuperado[28:32].decode('utf-8')
            inode.i_perm  = struct.unpack("<i", recuperado[97:101])[0]

            # print(recuperado)
            """<iiiddd15ici"""
            print(inode.i_uid  )
            print(inode.i_gid  )
            print(inode.i_size )
            print(inode.i_atime)
            print(inode.i_ctime)
            print(inode.i_mtime)
            print(inode.i_block)
            print(inode.i_type )
            print(inode.i_perm )
                        
            
            
            
            
            
            
            
            
            
            
            

            
        except Exception as e:
            print(e)
