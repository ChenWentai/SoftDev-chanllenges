import socket
import sys
import re
import cPickle as pickle
import datetime,time
# creat a socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# open a connection to a certain port
s.connect(('',9999))

#data = open('SECRET','r')
#data = sys.stdin.read();
secret = "4817e3c42ffccf68576cf69d19bdb72e"

print secret

print s.recv(1000)

print s.recv(1000)

s.send("Tiger"+"\n")
print s.recv(1000)

s.send(secret+'\n')
print s.recv(1000)


s.send("1000"+"\n")
print s.recv(1000)


#Game1 guessing number
#temp = ""
small = 0
big = 10000
while True:
 guess = (small+big)/2
 s.send(str(guess)+'\n')
# time.sleep(0.1)
 temp = s.recv(10000)
 if "smaller" in temp:
  big = guess
  print temp
 elif "bigger" in temp:
  small = guess
  print temp
 else:
  print temp
  break



#Game 2 recognize number

temp = s.recv(1000)
print temp
 # predefine symbolic number
zero = ["  ###  ",
        " #   # ",
        "# #   #",
        "#  #  #",
        "#   # #",
        " #   # ",
        "  ###  "]

one =  ["   #   ",
	"  ##   ",
	" # #   ",
	"   #   ",
	"   #   ",
	"   #   ",
	" ##### "]

two =  [" ##### ",
	"#     #",
	"      #",
	" ##### ",
	"#      ",
	"#      ",
	"#######"]

three= [" ##### ",
	"#     #",
	"      #",
	" ##### ",
	"      #",
	"#     #",
	" ##### "]

four = ["#      ",
	"#    # ",
	"#    # ",
	"#######",
	"     # ",
	"     # ",
	"     # "]

five = ["#######",
	"#      ",
	"#      ",
	" ##### ",
	"      #",
	"#     #",
	" ##### "]

six =  [" ##### ",
	"#     #",
	"#      ",
	"###### ",
	"#     #",
	"#     #",
	" ##### "]

seven= ["#######",
	"#    # ",
	"    #  ",
	"   #   ",
	"  #    ",
	"  #    ",
	"  #    "]

eight= [" ##### ",
	"#     #",
	"#     #",
	" ##### ",
	"#     #",
	"#     #",
	" ##### "]

nine = [" ##### ",
	"#     #",
	"#     #",
	" ######",
	"      #",
	"#     #",
	" ##### "]
num = [[zero],[one],[two],[three],[four],[five],[six],[seven],[eight],[nine]]#for the code following: if sys_num[i] in num[j].
temp = temp.split('\n')
# delete the words"what number was that?"
temp1 = [""]*7
for i in range(len(temp1)):
 temp1[i] = temp[i]
# print temp1[i]
 #print "length of temp:",len(temp1[i])


sym_num = [["" for i in range(7)] for j in range(3)]

for i in range(3):
 for j in range(7):
  for k in range(7):
   try:
    sym_num[i][j] += temp[j][k+16*i]
   except:
    sym_num[i][j] += " "

result = ""

#for i in range(len(sym_num)):
 #print "symnum",i,sym_num[i]
#for i in range(len(num)):
 #print "num_2:",i,num[i]

for i in range(len(sym_num)):
 for j in range(len(num)):
  if sym_num[i] in num[j]:
#   print j
   result += str(j) 

print "the number was:",result

s.send(str(result)+'\n')
temp = s.recv(1000)  
print temp

#Game3 Pickle Stuff
temp = s.recv(1000) 
print temp
# extract the real txt
temp1 = temp.split('\n')
temp2 = ""
for i in range(8):
 temp2 += temp1 [i+1]
 temp2 += '\n'
print "temp1:",temp1
print "temp2:",temp2
t1 = pickle.loads(temp2)
print "t1:",t1
result = ""
t2 = str(t1)
for i in xrange(len(t2)-6,len(t2),1):
 result += t2[i]
print result
s.send(result+'\n')
temp = s.recv(1000)
print temp

#Game4
temp = s.recv(1000)
print temp
temp = temp.replace('.',' ')

temp = temp.replace('16','2016')
temp = temp.replace('Aug','08') 

temp = temp.replace('Sep','09') 

temp = temp.replace('Oct','10')

temp = temp.replace('Nov','11')

#temp = temp.replace('16','2016')
result = []*10
for i in range(len(temp)):
 if temp[i].isdigit():
   result.append(temp[i])
print temp
print result

for i in xrange(1,len(result)-3,2):
 result[i] += '-'
print "result:",result

date_str = ''.join(result)
print "date_str:",date_str

date_input = datetime.date.fromtimestamp(time.mktime(time.strptime(date_str,"%d-%m-%Y")))
n = datetime.datetime.weekday(date_input)
print n
weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print weekday[n]
result = weekday[n]
s.send(result+'\n')
result = s.recv(1000)
print result

result = result.split('\n')
s.close()
print result[2]

