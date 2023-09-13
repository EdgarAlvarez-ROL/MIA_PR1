from mkdisk import MkDisk
from rmdisk import RmDisk
from rep import reporte
from fdisk2 import FDisk
from mount import Mount
from mkfs import MKFS

def main():
    disk = MkDisk()
    disk.fit  = "FF"
    disk.path = r'C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk'
    disk.size = 12
    disk.unit = "M"
    disk.create()

    # rm = RmDisk()
    # rm.path = r'C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk'
    # rm.remove()

    partition = FDisk()
    # partition.delete = "FULL"
    partition.size = 3
    partition.type = "P"
    partition.unit = "M"
    partition.path = r"C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk"
    partition.name = "cosa"
    partition.fit = "WF"
    # # partition.add = '100'
    partition.fdisk()

    mount = Mount()
    path = r'C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk'
    name = "cosa" #nombre de la particion a cargar
    mount.mount(path, name)
    mount.listaMount()
    # mount.unmount("441disco")
    # mount.listaMount()

    
    fileSystem = MKFS(mount)
    tks = ["441disco","Full","2fs"]
    fileSystem.mkfs(tks)
    

    repo = reporte()
    repo.path = r'C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk'
    repo.rep()

    # repo = reporte()
    # repo.path = r'\Users\JONATHAN ALVARADO\Desktop\disco.dk'
    # repo.rep()
    # pass

if __name__ == '__main__':
    main()