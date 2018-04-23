import sys
import re

if len(sys.argv) < 2:
	print("Error:python file-name")
	quit()

canid_data = ''
canid = []
data = []
log_num = 0

for line in open(sys.argv[1], 'r'):
	tmp = line.split(' ')
	canid_data = tmp[2]
	tmp = canid_data.split('#')
	canid.append(tmp[0])
	data.append(tmp[1])
	log_num += 1

#for i in range(0, log_num):
#	print canid[i], data[i],

canidSum = [0]*2048
for i in range(0,len(canid)):
	#print(canid[i], data[i])
	canidSum[int(canid[i], 16)] = canidSum[int(canid[i], 16)] + 1

Sum = 0
for i in range(0,len(canidSum)):
	Sum += canidSum[i]
	#print i, canidSum[i]
	if canidSum[i] != 0:
		print "%x" % i, canidSum[i]

#print log_num, Sum