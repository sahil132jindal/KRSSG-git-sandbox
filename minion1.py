import socket
import pickle
import time
sum=0

minion_list=[]

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1506))
	
list_bytes=pickle.dumps(0)
s.send(list_bytes)

msg=s.recv(4000)
	
minion_list=pickle.loads(msg)
print(minion_list)

for i in range(len(minion_list)):
	sum+=int(minion_list[i])

sum_bytes=pickle.dumps(sum)	
print(sum)
time.sleep(1)
s.send(sum_bytes)
s.close()
	
