import socket 
dollar = {'INR': 67.0, 'yen': 113.41, 'pounds': 0.75}
INR = {'dollar': 0.014, 'yen': 1.58, 'pounds': 0.11}
pounds = {'dollar': 1.26, 'yen': 142, 'INR': 90.0}
yen = {'dollar': 0.0089, 'INR': 0.63, 'pounds': 0.007}
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 
port = 4040
serversocket.bind((host_ip, port))
serversocket.listen(1)
c, addr = serversocket.accept()
print ('got connection from  ' + str(addr))
while True:
	data = c.recv(1024).decode().split()
	print('recevied data =  ' + str(data))

	if not data:
		break
	elif data[1] == 'INR':
		res = float(INR[data[4]] * int(data[2]))
	elif data[1] == 'dollar':
		res = float(dollar[data[4]] * int(data[2]))
	elif data[1] == 'pounds':
		res = float(pounds[data[4]] * int(data[2]))
	elif data[1] == 'yen':
		res = float(yen[data[4]] * int(data[2]))
	c.send(str(data[2] + ' ' +data[1] + ' = ' + str(res) + ' ' + data[4]).encode())
c.close()