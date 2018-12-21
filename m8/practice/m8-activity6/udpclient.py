import socket 
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 
port = 4041
transmittingdata = input('>>>')
while True:
	clientsocket.sendto(transmittingdata.encode(), (host_ip, port))
	data , addr = clientsocket.recvfrom(1024)
	print('received data = ' + str(data.decode()))
	transmittingdata = input('>>>')

clientsocket.close()
	