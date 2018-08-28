import socket, os

host = '192.168.100.11'
port = 5000

s = socket.socket()
s.settimeout(10)
s.connect((host, port))

print('< connected with %s >\n' % (host))

path = 'send.jpg'
stat = os.stat(path)
size = stat.st_size

# reading the image as bytes and sending them to server
message = input('@: ')
while message != 'q':
	if message.startswith('IMAGE'):
		flag = 'IMAGE ' + str(size)
		s.send(flag.encode())
		with open(path, 'rb') as f:
			b = f.read(1024)
			# sending bytes
			while b:
				s.sendall(b)
				b = f.read(1024)
			f.close()
			print('< sending complete >\n')
			# shutting down the sending 
			s.shutdown(socket.SHUT_WR)
	else:
		s.send(message.encode())
		text = s.recv(1024)
		print('--> ', str(text.decode()))
		message = input('@: ')
s.close()
