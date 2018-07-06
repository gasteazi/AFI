
__author__ = 'Alejandro Maestre'

import hashlib


class FirmasHash():
    """ Esté módulo permite generar firmas hash de cualquier tipo de archivo independientemente de su tamaño así como
    guardarlas en un archivo de texto"""

    def __init__(self):

        print("1 - MD5")
        print("2 - sh1")
        print("3 - sh256")
        print("4 - sh512")
        print("5 - Salir")

        self.opcion = input("> ")

        if self.opcion == "1":
            archivo = input("nombre de archivo: ")
            FirmasHash.md5(archivo)
            FirmasHash()

        elif self.opcion == "2":
            archivo = input("nombre de archivo: ")
            FirmasHash.sh1(archivo)
            FirmasHash()
        elif self.opcion == "3":
            archivo = input("nombre de archivo: ")
            FirmasHash.sha256(archivo)
            FirmasHash()
        elif self.opcion == "4":
            archivo = input("nombre de archivo: ")
            FirmasHash.sha512(archivo)
            FirmasHash()
        elif self.opcion == "5":
            exit()
        else:
            print("Elige una opción válida")
            FirmasHash()

    def md5(self):
        BLOCKSIZE = 65536
        hasher = hashlib.md5()
        with open(self, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        print("MD5: ")
        print(hasher.hexdigest())
        archivo = open("firmashash.txt", "a")
        archivo.write("MD5: " + hasher.hexdigest() + "\n")
        archivo.close()

    def sh1(self):
        BLOCKSIZE = 65536
        hasher = hashlib.sha1()
        with open(self, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        print("SHA1: ")
        print(hasher.hexdigest())
        archivo = open("firmashash.txt", "a")
        archivo.write("sh1: " + hasher.hexdigest() + "\n")
        archivo.close()

    def sha256(self):
        BLOCKSIZE = 65536
        hasher = hashlib.sha256()
        with open(entrada, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)

        print("SHA256: ")
        print(hasher.hexdigest())
        archivo = open("firmashash.txt", "a")
        archivo.write("SHA256: " + hasher.hexdigest() + "\n")
        archivo.close()

    def sha512(self):
        BLOCKSIZE = 65536
        hasher = hashlib.sha512()
        with open(self, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)

        print("SHA512: ")
        print(hasher.hexdigest())
        archivo = open("firmashash.txt", "a")
        archivo.write("SHA512: " + hasher.hexdigest() + "\n")
        archivo.close()



entrada = FirmasHash()