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

                """ARREGLAR"""
                partition1 = Particion()
                particion_data = b'1PW'+ particion_data
                particion_data = particion_data[:-2]
                print("PARTICON DATA")
                print(particion_data)
                partition1.__setstate__(particion_data)
                

                # print(mbr_data, particion_data)
                print("============================")
                # print(superBloque_data)
                super_Bloque = SuperBloque()
                
                # print(len(superBloque_data))
                # data = struct.unpack("<iiiiiddiiiiiiiiii", superBloque_data)
                superBloque_data = b'\x02\x00\x00\x00)7' + superBloque_data 
                superBloque_data = superBloque_data[:-6]
                # print(superBloque_data)
                data = struct.unpack("<iiiiiddiiiiiiiiii", superBloque_data)
                print(data)
                print("============================")
                # lo que deberia
                # b'\x02\x00\x00\x00)7\x00\x00{\xa5\x00\x00{\xa5\x00\x00)7\x00\x00\x00\x00@\xd2\xfb>\xd9A\x00\x00@\xd2\xfb>\xd9A\x01\x00\x00\x00S\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\x00\x00\xad7\x00\x00(\xdd\x00\x00\xb1\xc3\x15\x00'
                # b'                  \x00\x00{\xa5\x00\x00{\xa5\x00\x00)7\x00\x00\x00\x00@\xd2\xfb>\xd9A\x00\x00@\xd2\xfb>\xd9A\x01\x00\x00\x00S\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\x00\x00\xad7\x00\x00(\xdd\x00\x00\xb1\xc3\x15\x00\x0011000'
                # lo que salio

                # if superBloque_data == b'\x02\x00\x00\x00)7\x00\x00{\xa5\x00\x00{\xa5\x00\x00)7\x00\x00\x00\x00@\xd2\xfb>\xd9A\x00\x00@\xd2\xfb>\xd9A\x01\x00\x00\x00S\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\x00\x00\xad7\x00\x00(\xdd\x00\x00\xb1\xc3\x15\x00':
                    # print("chupala")

                # Data es la info del superbloque
                print("###########################")
                inodos_data = file.read(struct.calcsize("<c2s3i3i16s"))
                # b'\x01\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x80k\x06?\xd9A\x00\x00\x80k\x06?\xd9A\x00\x00\x80k\x06?\xd9A\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x98\x02\x00\x00'
                # b'\x01\x00\x00\x00\x01\x00\x00\x00[\x00\x00\x00\x00\x00\x80k\x06?\xd9A\x00\x00\x80k\x06?\xd9A\x00\x00\x80k\x06?\xd9A\x01\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x98\x02\x00\x00'
                # print(inodos_data)
                print("###########################")
                # 
                file.close()
            
           

            print("\t============ MBR \t============")
            print("\tMBR tamaño:", mbr.mbr_tamano)
            print("\tMBR fecha creación:", mbr.mbr_fecha_creacion)
            print("\tDisco fit:", mbr.disk_fit)
            print("\tMBR disk signature:", mbr.mbr_disk_signature)

            print("\t============ PARTICION 1 ============")
            print("\tMBR Particion 1-NAME: ", partition1.part_start)
            

            print(particion_data)

            
        except Exception as e:
            print("\tERROR: No se pudo leer el disco en la ruta: " + self.path+", debido a: "+str(e))


    

    def replicaa(self, p):
        try:
            sprTemp = structs.Inodos()  # Crear una instancia de SuperBloque
            bytes_inodo= bytes(sprTemp)  # Obtener los bytes de la instancia

            recuperado = bytearray(len(bytes_inodo))  # Crear un bytearray del mismo tamaño

            # p = ""
            # m = Mount()
            # part, p  = m.getmount()

            with open(self.path, "rb") as archivo:
                archivo.seek(p.part_start - 1)
                archivo.readinto(recuperado)
            
            # Desempaquetar los datos del bytearray recuperado
            sprTemp.s_filesystem_type = struct.unpack("<i", recuperado[:4])[0]
            sprTemp.s_inodes_count = struct.unpack("<i", recuperado[4:8])[0]
            sprTemp.s_blocks_count = struct.unpack("<i", recuperado[8:12])[0]
            sprTemp.s_free_blocks_count = struct.unpack("<i", recuperado[12:16])[0]
            sprTemp.s_free_inodes_count = struct.unpack("<i", recuperado[16:20])[0]
            sprTemp.s_mtime = struct.unpack("<d", recuperado[20:28])[0]
            sprTemp.s_umtime = struct.unpack("<d", recuperado[28:36])[0]
            sprTemp.s_mnt_count = struct.unpack("<i", recuperado[36:40])[0]
            sprTemp.s_magic = struct.unpack("<i", recuperado[40:44])[0]
            sprTemp.s_inode_size = struct.unpack("<i", recuperado[44:48])[0]
            sprTemp.s_block_size = struct.unpack("<i", recuperado[48:52])[0]
            sprTemp.s_first_ino = struct.unpack("<i", recuperado[52:56])[0]
            sprTemp.s_first_blo = struct.unpack("<i", recuperado[56:60])[0]
            sprTemp.s_bm_inode_start = struct.unpack("<i", recuperado[60:64])[0]
            sprTemp.s_bm_block_start = struct.unpack("<i", recuperado[64:68])[0]
            sprTemp.s_inode_start = struct.unpack("<i", recuperado[68:72])[0]
            sprTemp.s_block_start = struct.unpack("<i", recuperado[72:76])[0] 
        except Exception as e:
            print(e)
