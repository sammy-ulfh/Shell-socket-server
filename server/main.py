#!/usr/bin/env python3

import re
import signal
from server import Server

STATUS = 0

def handler(signum, frame):
    global STATUS
    STATUS = 1

signal.signal(signal.SIGINT, handler)


def port_check(port):

    patron = "[0-9]{0,5}"

    if re.findall(patron, port):
        return True
    else:
        return False

def main():

    print("\n[+] Para finalizar el programa, presione ctrl + d\n")
    print("\n[+] Si ya se inició el servidor, presione ctrl + c\n")

    try:
        host = input("\n[+] Ingrese el host: ")
        while True:
            try:
                port = int(input("\n[+] Ingrese el puerto: "))
                if not port_check(str(port)):
                    print("\n\n[!] El puerto tiene que ser de 1-5 digitos\n")
                    continue
                elif port < 0:
                    print("\n\n[!] El puerto no puede ser un número negativo\n")
                    continue
                break
            except ValueError:
                print("\n\n[!] El puerto tiene que ser un tipo de dato numérico\n")
    except EOFError:
        print("\n\n[!] Saliendo del programa...\n")
        return

    server = Server(host, port)
    server.start_server()



if __name__ == '__main__':
    main()
