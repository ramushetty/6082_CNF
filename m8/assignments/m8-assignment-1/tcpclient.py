import socket 
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 
port = 4040
clientsocket.connect((host_ip, port))
transmittingdata = input('>>>')
while True:
	clientsocket.send(transmittingdata.encode())
	data = clientsocket.recv(1024).decode()
	print(data)
	transmittingdata = input('>>>')

clientsocket.close()
	