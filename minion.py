import socket
import pickle

sum=0

minion_list=[]
while True:
	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((socket.gethostname(),1507))
	
	list_bytes=pickle.dumps(1)
	s.send(list_bytes)

	msg=s.recv(4000)
	if (pickle.loads(msg))==1:
		s.close()
		continue
	minion_list=pickle.loads(msg)
	print(minion_list)

	for i in range(len(minion_list)):
		sum+=int(minion_list[i])

	sum_bytes=pickle.dumps(sum)	
	print(sum)
	s.send(sum_bytes)
	
	break
