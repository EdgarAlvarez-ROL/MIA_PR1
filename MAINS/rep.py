from structs import MBR, Particion, EBR, SuperBloque
import struct
import structs
import pickle

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
            with open(self.path, "rb") as file:
                mbr_data = file.read(mbr_size)
                particion_data = file.read(partition_size)
                superBloque_data = file.read(struct.calcsize("<iiiiiddiiiiiiiiii"))
                # print(particion_data)
                mbr = MBR()
                (mbr.mbr_tamano, mbr.mbr_fecha_creacion, mbr.mbr_disk_signature, disk_fit, mbr.mbr_Partition_1, *_) = struct.unpack(mbr_format, mbr_data)
                mbr.disk_fit = chr(disk_fit % 128) 


                partition1 = Particion()
                partition1.__setstate__(particion_data)
                # print(mbr_data, particion_data)
                print("=============")
                # print(superBloque_data)
                super_Bloque = SuperBloque()
                
                # print(len(superBloque_data))
                # data = struct.unpack("<iiiiiddiiiiiiiiii", superBloque_data)
                superBloque_data = b'\x02\x00\x00\x00)7' + superBloque_data 
                superBloque_data = superBloque_data[:-6]
                # print(superBloque_data)
                data = struct.unpack("<iiiiiddiiiiiiiiii", superBloque_data)
                print(data)
                print("=============")
                # lo que deberia
                # b'\x02\x00\x00\x00)7\x00\x00{\xa5\x00\x00{\xa5\x00\x00)7\x00\x00\x00\x00@\xd2\xfb>\xd9A\x00\x00@\xd2\xfb>\xd9A\x01\x00\x00\x00S\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\x00\x00\xad7\x00\x00(\xdd\x00\x00\xb1\xc3\x15\x00'
                # b'                  \x00\x00{\xa5\x00\x00{\xa5\x00\x00)7\x00\x00\x00\x00@\xd2\xfb>\xd9A\x00\x00@\xd2\xfb>\xd9A\x01\x00\x00\x00S\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\x00\x00\xad7\x00\x00(\xdd\x00\x00\xb1\xc3\x15\x00\x0011000'
                # lo que salio

                # if superBloque_data == b'\x02\x00\x00\x00)7\x00\x00{\xa5\x00\x00{\xa5\x00\x00)7\x00\x00\x00\x00@\xd2\xfb>\xd9A\x00\x00@\xd2\xfb>\xd9A\x01\x00\x00\x00S\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\x00\x00\xad7\x00\x00(\xdd\x00\x00\xb1\xc3\x15\x00':
                    # print("chupala")
                
                file.close()
       
            print("\tMBR tamaño:", mbr.mbr_tamano)
            print("\tMBR fecha creación:", mbr.mbr_fecha_creacion)
            print("\tDisco fit:", mbr.disk_fit)
            print("\tMBR disk signature:", mbr.mbr_disk_signature)

            print("\tMBR Particion 1-NAME: ", partition1.part_name)

            
            # self.diskco()
        except Exception as e:
            print("\tERROR: No se pudo leer el disco en la ruta: " + self.path+", debido a: "+str(e))

