import struct


class Usuario:
    def __init__(self):
        self.u_usuario = ""
        self.u_password = ""
        self.u_id = ""
        self.u_permisos = ""
        self.u_bloques = ""
        self.u_inodos = ""
    
    def getPermisos(self, user):
        if self.u_usuario == user:
            return self.u_permisos
        else:
            return "Error Permisos Usuario"



class Inodos:
    def __init__(self):
        self.i_uid = -1
        self.i_gid = -1
        self.i_size = -1
        self.i_atime = 0
        self.i_ctime = 0
        self.i_mtime = 0
        self.i_block = [-1] * 15
        self.i_type = 0
        self.i_perm = -1

    def __bytes__(self):
        return (struct.pack("<i", self.i_uid) +
                struct.pack("<i", self.i_gid) +
                struct.pack("<i", self.i_size) +
                struct.pack("<d", self.i_atime) +
                struct.pack("<d", self.i_ctime) +
                struct.pack("<d", self.i_mtime) +
                struct.pack("<15i", *self.i_block) +
                struct.pack("<B", self.i_type) +  # Use "<B" format for a single byte
                struct.pack("<i", self.i_perm))
    
class SuperBloque:
    def __init__(self):
        self.s_filesystem_type = 0
        self.s_inodes_count = 0
        self.s_blocks_count = 0
        self.s_free_blocks_count = 0
        self.s_free_inodes_count = 0
        self.s_mtime = 0
        self.s_umtime = 0
        self.s_mnt_count = 0
        self.s_magic = 0xEF53
        self.s_inode_size = 0
        self.s_block_size = 0
        self.s_first_ino = 0
        self.s_first_blo = 0
        self.s_bm_inode_start = 0
        self.s_bm_block_start = 0
        self.s_inode_start = 0
        self.s_block_start = 0

    def __bytes__(self):
        return (struct.pack("<i", self.s_filesystem_type) +
                struct.pack("<i", self.s_inodes_count) +
                struct.pack("<i", self.s_blocks_count) +
                struct.pack("<i", self.s_free_blocks_count) +
                struct.pack("<i", self.s_free_inodes_count) +
                struct.pack("<d", self.s_mtime) +
                struct.pack("<d", self.s_umtime) +
                struct.pack("<i", self.s_mnt_count) +
                struct.pack("<i", self.s_magic) +
                struct.pack("<i", self.s_inode_size) +
                struct.pack("<i", self.s_block_size) +
                struct.pack("<i", self.s_first_ino) +
                struct.pack("<i", self.s_first_blo) +
                struct.pack("<i", self.s_bm_inode_start) +
                struct.pack("<i", self.s_bm_block_start) +
                struct.pack("<i", self.s_inode_start) +
                struct.pack("<i", self.s_block_start))
    
class Content:
    def __init__(self):
        self.b_name = '\x00' * 12
        self.b_inodo = -1

    def __bytes__(self):
        return (self.b_name.ljust(12, '\0').encode('utf-8') +
                struct.pack("<i", self.b_inodo))
    
class BloquesCarpetas:
    def __init__(self):
        self.b_content = [Content() for _ in range(4)]

    def __bytes__(self):
        return b"".join(bytes(c) for c in self.b_content)

class BloquesArchivos:
    def __init__(self):
        self.b_content = '\x00' * 64

    def __bytes__(self):
        return self.b_content.ljust(64, '\0').encode('utf-8')
    
class BloquesApuntadores:
    def __init__(self):
        self.b_pointers = [-1] * 16

    def __bytes__(self):
        return struct.pack("<16i", *self.b_pointers)
    
class Journaling:
    def __init__(self):
        self.estado = -1
        self.operation = ''
        self.type = -1
        self.path = ''
        self.date = 0
        self.content = ''
        self.id_propietario = ''
        self.size = 0

    def __bytes__(self):
        return (struct.pack("<i", self.estado) +
                self.operation.encode('utf-8').ljust(10, b'\x00') +
                struct.pack("<c", bytes([self.type])) +
                self.path.encode('utf-8').ljust(100, b'\x00') +
                struct.pack("<d", self.date) +
                self.content.encode('utf-8').ljust(60, b'\x00') +
                struct.pack("<c", bytes([self.id_propietario])) +
                struct.pack("<i", self.size))

