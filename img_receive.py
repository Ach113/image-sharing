import socket, os, sys

host = '192.168.100.11'
port = 5000
fname = 'received.jpg'

print('Current IP: ', socket.gethostbyname(socket.gethostname()))

# creating socket object
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.bind((host, port))

# listening for connections
so.listen(5)
# accepting the connection
conn, addr = so.accept()
print("Connection from: ", str(addr)) # printing the address of connection
while True:
	# receiving the data
	data = conn.recv(1024)
	if str(data.decode()).startswith('IMAGE'):
		if os.path.exists(fname):
			print('< image already present >\n')
			break
		f = open('received.jpg', 'wb')
		f_size = int(str(data.decode())[7:])
		print('< downloading file size: ' + str(f_size) + ' bytes >\n')
		while data:
			data = conn.recv(1024)
			while data:
				#print('Downloading...')
				f.write(data)
				data = conn.recv(1024)
			print('< Download finished >\n')
			f.close()
			break
	else:
		echo = str(data.decode()).upper()
		conn.send(echo.encode())

