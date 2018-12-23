import socket,random
import threading 
from _thread import *

def Main():

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    port = 4040
    serversocket.bind((host_ip, port))
    serversocket.listen(100)
    while True:
        c, addr = serversocket.accept()
        print("Connected Server" , str(addr))
        rnum = int(random.randint(0, 50))
        print(rnum)
        print(start_new_thread(clientsThread, (c, rnum)))

def clientsThread(c, rnum):
    count = int(0)
    value = int(0)
    while True:
        data = c.recv(1024)
        if not data:
            break
        if data.decode() == 'Q':
            return
        value = int(data.decode())

        print("Guess" + str(data.decode()))
        if (value == rnum):
            count += 1
            message = "Correct Answer   = " + str(count)
            c.send(str(message).encode())
        elif (value < rnum):
            count += 1
            message = "Number is smaller than the guess"
            c.send(str(message).encode())
        elif (value > rnum):
            count += 1
            message = "Number is bigger than the guess"
            c.send(str(message).encode())

    c.close()



if __name__ == '__main__':
    Main()