import socket

portServer=11001
host=socket.gethostname()
host_ip=socket.gethostbyname(host)

# Function to create a socket and bind it to a port
def createSocket(port):
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((host_ip, port))
	print('Server ip->',host_ip)
	print('Server port->',port)
	return s

# Function to receive a connection
def allowConn(s):
	s.listen(5)
	c, addr=s.accept()
	return c, addr

# Function to create a socket and connect to it
def createConn(port,ip=host_ip):
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip,port))
	return sock

# Function to send a frame
def send_frame(frame, c):
	# Send the frame to the other process
	c.send(frame.encode())