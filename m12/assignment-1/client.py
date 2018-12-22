import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
port = 4040
clientsocket.connect((host_ip, port))
# m1 = "Hello server!"
# clientsocket.send(m1.encode())

message = input('>>>')
clientsocket.send(message.encode())

data = str(clientsocket.recv(1024).decode()).split(',')

# while True:
	
	# print(data)
if data[1] == 'secretquestion':
	print(data[0])
	message = str(input('>>>'))
	clientsocket.send(message.encode())
m2 = str(clientsocket.recv(1024).decode())
print(m2)
if m2 == 'ATTENDANCE SUCCESS':
	print('ATTENDANCE SUCCESS')

	clientsocket.close()
