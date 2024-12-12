#!/usr/bin/env python3

import re
from client import Client
import signal

def handler(signum, frame):
    print("\n[!] Cerrando el programa...\n")
    exit(0)

signal.signal(signal.SIGINT, handler)

def port_check(port):

    patron = "[0-9]{0,5}"

    if re.findall(patron, port):
        return True
    else:
        return False

def main():

    try:
        host = input("\n[+] Ingrese al host al que se conectará: ")
        while True:
            port = int(input("\n[+] Ingrese el puerto: "))
            if not port_check(str(port)):
                print("\n[!] El puerto debe tener de 1-5 dígitos\n")
                continue
            else:
                break
    except EOFError:
        print("\n[!] Saliendo...\n")
        exit(0)
    except ValueError:
        print("\n[!] El puerto debe ser un tipo de dato numérico\n")

    client = Client(host, port)

    client.start_client()


if __name__ == '__main__':
    main()
