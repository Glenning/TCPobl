from socket import *
import threading
import random

def handleClient(connectionSocket,addr):
    print(addr[0])
    keep_communacating = True

    while keep_communacating:
        sentence = connectionSocket.recv(1024).decode()
        response = "error, send a proper message"
        if sentence.strip()== "close":
            keep_communacating = False
            response ="closing the connection"

        elif sentence.startswith("random"):
            response = "input number"
            connectionSocket.send(response.encode()) 

            input_numbers= connectionSocket.recv(1024).decode().strip()
            num1, num2 = map(int, input_numbers.split())         

            random_num = random.randint(num1, num2)
            response = str(random_num) 
        elif sentence.startswith("add"):
            response = "input numbers to find sum"
            connectionSocket.send(response.encode())

            input_numbers = connectionSocket.recv(1024).decode().strip()
            num1, num2 = map(int, input_numbers.split())  

            add_num = num1 + num2
            response =str(add_num)
        elif sentence.startswith("subtract"):
            response = "input numbers to substract"
            connectionSocket.send(response.encode())

            input_numbers = connectionSocket.recv(1024).decode().strip()
            num1, num2 = map(int, input_numbers.split())  

            sub_num = num1 - num2
            response =str(sub_num)
        connectionSocket.send(response.encode())

    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('From server: ')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
