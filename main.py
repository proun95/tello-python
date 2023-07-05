import socket

HOST = ""
PORT = 9000
LOC_ADDR = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

TELLO_ADDRESS = ("192.168.10.1", 8889)

sock.bind(LOC_ADDR)

STATE = 1

while STATE:
    command = input("Input command:")

    if command == "exit":
        STATE = 0
        continue

    sock.sendto(command.encode(encoding="utf-8"), TELLO_ADDRESS)
