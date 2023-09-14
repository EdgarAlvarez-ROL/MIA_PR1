from mkdisk import MkDisk
from rmdisk import RmDisk
from rep import reporte
from fdisk2 import FDisk
from mount import Mount
from mkfs import MKFS

def main():
    path = r"/home/rol/Tareas/PR1/MIA_PR1/Discos/disco.dsk"

    # disk = MkDisk()
    # disk.fit  = "FF"
    # disk.path = path
    # disk.size = 12
    # disk.unit = "M"
    # disk.create()

    # # # rm = RmDisk()
    # # # rm.path = path
    # # # rm.remove()

    # partition = FDisk()
    # # partition.delete = "FULL"
    # partition.size = 1
    # partition.type = "E"
    # partition.unit = "M"
    # partition.path = path
    # partition.name = "logica"
    # partition.fit = "WF"
    # # # partition.add = '100'
    # partition.fdisk()

    # mount = Mount()
    # # path = path
    # name = "cosa" #nombre de la particion a cargar
    # mount.mount(path, name)
    # mount.listaMount()
    # # mount.unmount("441disco")
    # # mount.listaMount()

    
    # fileSystem = MKFS(mount)
    # tks = ["441disco","Full","2fs"]
    # fileSystem.mkfs(tks)
    

    repo = reporte()
    repo.path = path
    repo.rep()

    # repo = reporte()
    # repo.path = r'\Users\JONATHAN ALVARADO\Desktop\disco.dk'
    # repo.rep()
    # pass

if __name__ == '__main__':
    main()