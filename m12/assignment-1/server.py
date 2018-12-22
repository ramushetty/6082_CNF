import socket
import csv
def Main(): 
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	port = 4040
	serversocket.bind((host_ip,port))
	serversocket.listen(5)
	print('server listening.......')
	
	while True:
		conn, addr = serversocket.accept()
		print('Got connection from ', addr)
		data = conn.recv(1024)
		print('Server received', repr(data))
		rollnumber = int(data.decode())
		attendance(rollnumber, conn)
def attendance(rollnumber, conn):
	with open('data.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter = ',')
		for row in readCSV:
			if(str(rollnumber) == row[0]):
				# print(row[0],row[1],row[2])
				
				m3 = str(str(row[1]) + "," + "secretquestion")
				conn.send(m3.encode())
				data = conn.recv(1024)
				if(data == row[2]):
					mess = 'ATTENDANCE SUCCESS '
					conn.send(mess.encode())
					break
	conn.close()
	# serversocket.close()



if __name__ == '__main__':
    Main()