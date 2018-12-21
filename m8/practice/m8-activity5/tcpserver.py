import socket 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 
port = 4040
serversocket.bind((host_ip, port))
serversocket.listen(1)
c, addr = serversocket.accept()
print ('got connection from  ' + str(addr))
while True:
	data = c.recv(1024).decode()
	if not data:
		break
	print('recevied data =  ' + data)
	data = str(data).upper()
	c.send(data.encode())
c.close()