from structs import MBR, Particion, EBR
import struct

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
            partition_format = "<iii6s"
            particion_size = struct.calcsize(partition_format)
            print(particion_size)

            with open(self.path, "rb") as file:
                mbr_data = file.read(mbr_size)
                particion_data = file.read(particion_size)
                print(particion_data)
                mbr = MBR()
                (mbr.mbr_tamano, mbr.mbr_fecha_creacion, mbr.mbr_disk_signature, disk_fit, *_) = struct.unpack(mbr_format, mbr_data)
                mbr.disk_fit = chr(disk_fit % 128) 

                partition1 = Particion()
                partition1.__setstate__(particion_data)
       
                partition2 = Particion()
                partition2.__setstate__(particion_data)

            print("\tMBR tamaño:", mbr.mbr_tamano)
            print("\tMBR fecha creación:", mbr.mbr_fecha_creacion)
            print("\tDisco fit:", mbr.disk_fit)
            print("\tMBR disk signature:", mbr.mbr_disk_signature)

            print("\tMBR particion 1: ", partition2.part_fit)

        except Exception as e:
            print("\tERROR: No se pudo leer el disco en la ruta: " + self.path+", debido a: "+str(e))