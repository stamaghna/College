import socket
import threading
import common as co
import pickle

# Class to store key value for each client
class KeyValueClient:

	def __init__(self,username):
		self.valstore={}
		self.mode='guest'
		self.username=username

	def _change_mode(self):
		if(self.mode=='manager'):
			return(self.username+' is already a Manager. Cannot upgrade.')
		choice=input('Do you want to change mode(Y/N) ')
		if (choice=='Y' or choice=='y'):
			self.mode='manager'
			return 'Mode changed'
			#print(self.username+' is now a Manager.')
		else:
			return 'Mode not changed'

	def _getValue(self,key):
		if(key not in self.valstore):
			return 'Invalid key'
		return self.valstore[key]

	def _putValue(self,key,value):

		self.valstore[key]=value
		return 'Successful'

	# Function to take action on the requests
	def takeAction(self,req):

		res=[]

		for reqs in req:
			if(reqs['method'].lower()=='get'):
				res.append(self._getValue(reqs['key']))
				print(self.username+': GET operation')

			elif(reqs['method'].lower()=='put'):
				res.append(self._putValue(reqs['key'],reqs['value']))
				print(self.username+': PUT operation')

			elif(reqs['method'].lower()=='upgrade'):
				#self._change_mode()
				print(self.username+': UPGRADE operation')
				res.append(self._change_mode())

			elif(reqs['method'].lower()=='getother'):
				print(self.username+': GETOTHER operation')
				if(self.mode=='guest' and self.username!=reqs['username']):
					res.append('Access Denied')
				elif(self.username==reqs['username'] or self.mode=='manager'):

					if(reqs['username'] in global_dict):
						res.append(global_dict[reqs['username']]._getValue(reqs['key']))
					else:
						res.append('Invalid username')
			elif(reqs['method'].lower()=='exit'):
				#print(self.username+': Exited')
				res.append('End')
		return res
port_no=input('Enter the port number: ')
sockServer=co.createSocket(int(port_no))
global_dict={}

# Function to service a client
def serviceClient(client, clientAddr,uname):

	while True:

		requestC=clientAddr.recv(1024) # Receive the request dictionary
		requestC=pickle.loads(requestC)
		res=client.takeAction(requestC)
		if (res[0]=='End'):
			del global_dict[uname]
			print(uname+': Exited')
			break
		res=pickle.dumps(res)
		clientAddr.sendall(res)

def allow_new_conn():

	while(True):
		# Wait for a connection
		sockServer.listen(10)
		cAddr, addrServer=sockServer.accept()
		
		# Fetch username
		uname=cAddr.recv(1024).decode()
		client=KeyValueClient(uname) # Create client by that username
		global_dict[uname]=client
		print('Connected to a new client: '+uname)
		# Start a new thread for the sender
		sendThread=threading.Thread(target=serviceClient, args=[client,cAddr,uname])
		sendThread.start()
		#sendThread.join()

allow_new_conn()