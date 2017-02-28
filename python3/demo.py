temp = '0x602050:       0x602070'
temp = list(temp)
num = temp.index(":")
#print "num: ",num
temp2 = temp[num+2:len(temp)]
print "hehehe:",temp2
num = temp2.index("x")
print "num: ",num
temp2 = temp2[num-1:len(temp2)]
print "hehe:",temp2
temp3 = ''
for m in range(0,8):
	try:
        	temp3+=temp2[m]
        except:
        	pass
print temp3

#b = list(a)
#result = [w.replace(' ','') for w in b]
#print b
