#!/usr/bin/env python2

import socket
import subprocess
import os
from history import History

class Server:

    def __init__(self, host, port):
        self._host = host
        self._port = port

    def client_connection(self, client, addr):

        with client:

            x = 0 

            d = os.getcwd()
            client.sendall(f"\n\n[+] Bienvenido a tu terminal bash\n".encode())

            history = History(addr)
            history.save_history()

            while True:
                from main import STATUS
                if STATUS == 1:
                    client.sendall(f"\n[!] El servidor ha sido cerrado\n".encode())
                    break
                elif x == 1:
                    client.sendall("\n[i] Sesión terminada\n".encode())
                    print("\n[!] Conexión cerrada\n")
                    break

                data = client.recv(1024)
                with subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=d) as process:

                    command = data.decode().strip()

                    if command.split(' ')[0] == "cd":
                        try:
                            os.chdir(command.split()[1])
                            d = os.getcwd()
                            client.sendall("-\n".encode())
                        except:
                            client.sendall(f"\n[!] Ingrese una ruta válida\n".encode())
                    elif command == "exit":
                        x = 1
                        continue
                    else:
                        stdout, stderr = process.communicate(input=f"{command}\n")

                        if stdout and stderr:
                            client.sendall(f"\nOutput:\n\n{stdout}\n\nErrores:\n\n{stderr}\n".encode())
                        elif stdout:
                            client.sendall(stdout.encode())
                        elif stderr:
                            client.sendall(stderr.encode())
                        else:
                            client.sendall("-\n".encode())

                    history.save_command(command)


    def start_server(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
           try:
               s.bind((self.host, self.port))
           except OSError:
               print("\n[!] Host incorrecto o puerto no accesible\n")
               return

           s.listen(1)
           s.settimeout(2)
           print(f"\n[+] Servidor en escucha en ({self.host, self.port})\n")

           while True:
               from main import STATUS
               if STATUS == 1:
                   print("\n[!] Cerrando el servidor...\n")
                   break

               try:
                    client, addr = s.accept()
                    print(f"\n[+] Conexión establecida {addr}")

                    self.client_connection(client, addr) # Client connectionexcept
               except TimeoutError:
                   continue
               except:
                   print("\n[!] Conexión cerrada\n")
                   continue

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status
