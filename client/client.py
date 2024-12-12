#!/usr/bin/env python3

import socket

class Client:

    def __init__(self, host, port):
        self._host = host
        self._port = port

    def start_client(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

            try:
                client.connect((self.host, self.port))
            except ConnectionRefusedError:
                print("\n[!] Error al realizar la conexión, inténtelo de nuevo\n")
                return

            with client:

                print(client.recv(1024).decode())

                while True:

                    command = input("$ ")
                    if not command:
                        continue
                    client.sendall(command.encode())

                    output = client.recv(1024 * 1024).decode()

                    if output.strip() == '-':
                        pass
                    elif output.strip() == "[i] Sesión terminada" or output.strip() == "[!] El servidor ha sido cerrado":
                        print(output)
                        break
                    else:
                        print(output)


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
