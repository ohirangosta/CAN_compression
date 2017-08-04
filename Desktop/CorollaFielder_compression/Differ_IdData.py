 # -*- coding:cp932 -*-

def sxor(s1,s2):    
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(str(format(int(a, 16) ^ int(b, 16), '04b')) for a,b in zip(s1,s2))

filename = r'Levorg_DataField.txt'

MovingData = ""
MovingDataLog = [[]]
OutputData = ""
OutputDataLog = [[]]

Nr = 1
for line in open(filename, 'rb'):
  MovingData = line[:-1].split(' ')
  MovingDataLog.append(MovingData)
  #print MovingDataLog[Nr][0]
  Nr += 1

#print MovingDataLog[1][0]

FlagALLCANID = [0]*2048 #New:0, Pre:1
for i in range(0, len(FlagALLCANID)):
  FlagALLCANID[i] = 0

AbsoluteCANData = dict() # key:=CAN ID
Nr = 1
TotalRawDatabit = 0
TotalComDatabit = 0
OutputData_RunLength = ""

for i in range(0, len(MovingDataLog)-1):
  if FlagALLCANID[int(MovingDataLog[Nr][0], 16)] == 0:
    FlagALLCANID[int(MovingDataLog[Nr][0], 16)] = 1
    AbsoluteCANData.setdefault(MovingDataLog[Nr][0], MovingDataLog[Nr][1])
    OutputData = MovingDataLog[Nr][1]
    OutputData_RunLength = OutputData
  else :
    RunLength_Sum = 0
    OutputData_RunLength = ""
    AbstData = AbsoluteCANData[MovingDataLog[Nr][0]]
    AbsoluteCANData[MovingDataLog[Nr][0]] = MovingDataLog[Nr][1]
    DiffData = MovingDataLog[Nr][1]
    OutputData = sxor(AbstData, DiffData)
    #print MovingDataLog[Nr][0], list(map(hex, map(ord, OutputData)))
    for j in range(0, len(OutputData)):
      if OutputData[j] == '0':
        RunLength_Sum += 1
      else :
        #print RunLength_Sum
        #print OutputData_RunLength, str(format(RunLength_Sum, '06b'))
        OutputData_RunLength += str(format(RunLength_Sum, '06b'))
        #print OutputData_RunLength, RunLength_Sum
        RunLength_Sum = 0
    print MovingDataLog[Nr][0], OutputData_RunLength, AbstData, DiffData, len(OutputData_RunLength)
  #print len(MovingDataLog[Nr][1])/2*8, len(OutputData_RunLength)
  TotalRawDatabit += len(MovingDataLog[Nr][1])/2*8
  TotalComDatabit += len(OutputData_RunLength)
  OutputDataLog.append(OutputData)
  Nr += 1


print "Raw:%d[bit]" % TotalRawDatabit, "Compression:%d[bit]" % TotalComDatabit
print "data can be compressed from %d bits into %d bits (%f%%)" % \
  (TotalRawDatabit, TotalComDatabit, float(TotalComDatabit) / TotalRawDatabit * 100)
#for Nr in range(0, len(OutputDataLog)):
  #print OutputDataLog[Nr]