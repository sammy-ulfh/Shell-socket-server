#!/usr/bin/env python3

import datetime
import os


class History:

    def __init__(self, connection):

        self.time = datetime.datetime.now()
        self.connection = connection
        self.__file = "/ruta/absoluta/.history"

    def create_file(self):
        with open(self.file, "w") as f:
            f.write('')

    def save_history(self):

        if not os.path.exists(self.file):
            self.create_file()

        with open(self.file, "a") as f:
            f.write(f"\n\n[+] Fecha de la conexión: {self.time}\n[+] Información de la conexión que se ha realizado: {self.connection}\n[+] Comandos ejecutados:\n")

    def save_command(self, command):

        with open(self.file, "a") as f:
            f.write(f"\n\t+) {command}")

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.__file = file
