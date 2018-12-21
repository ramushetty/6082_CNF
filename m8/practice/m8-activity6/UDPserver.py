import socket 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 
port = 4041
serversocket.bind((host_ip, port))
while True:
	data, addr = serversocket.recvfrom(1024)
	print ('got connection from  ' + str(addr))

	if not data:
		break
	print('recevied data =  ' + data.decode())
	data = str(data.decode()).upper()
	serversocket.sendto(data.encode(), addr)
serversocket.close()