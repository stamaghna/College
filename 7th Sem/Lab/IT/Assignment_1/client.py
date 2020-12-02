import socket
import threading
import common as co
import pickle
import sys


# Function to return a dictionary based on the request
def parseArgs(args):

	req=[]
	i=0
	while i<(len(args)):

		if(args[i].lower()=='get'):
			if(i==len(args)-1 or args[i+1].lower()=='put'): # Error case
				return 0,req
			else:
				req.append({'method':'get','key':args[i+1]})
				i=i+1

		elif(args[i].lower()=='put'):
			if(i==len(args)-2): # Error case
				return 0,req
			else:
				req.append({'method':'put','key':args[i+1],'value':args[i+2]})
				i=i+2

		elif(args[i].lower()=='getother'):
			if(i==len(args)-2): # Error case
				return 0,req
			else:
				req.append({'method':'getother','key':args[i+2],'username':args[i+1]})
				i=i+2
					
		elif(args[i].lower()=='upgrade'):
			req.append({'method':'upgrade'})
		elif(args[i].lower()=='exit'):
			req.append({'method':'exit'})
		else:
			return 0,req
		i=i+1

	return 1,req

sockClient=co.createConn(port=int(sys.argv[2]),ip=sys.argv[1])

uname=input('Enter a username: ')
sockClient.sendall(uname.encode())

if(len(sys.argv)>3):
	retVal,req=parseArgs(sys.argv[3:])
	if(retVal==0):
		req=[]#test this
		print('Invalid arguments')
		req.append({'method':'exit'})
	req=pickle.dumps(req)
	sockClient.sendall(req)
	if(retVal==0):
		exit(0)
	response=sockClient.recv(1024)
	response=pickle.loads(response)
	print(response)

print('Keywords:')
print('1. get key')
print('2. put key value')
print('3. upgrade')
print('4. getother username key')

while(True):

	request=input('$ ')
	retVal,req=parseArgs(request.split(' '))

	if(retVal==0):
		print('Invalid arguments')
		continue

	req=pickle.dumps(req)
	# Send the dictionary through socket
	sockClient.sendall(req)

	if(request.lower()=='exit'):
		break

	response=sockClient.recv(1024)
	response=pickle.loads(response)

	print(response)