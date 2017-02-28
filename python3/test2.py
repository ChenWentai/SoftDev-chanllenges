a = open('underground.map','r')
b=a.read()
print type(b)

for i in range(len(b)):
 if b[i] == '1' or b[i] == '2':
	print 'ok'
	print b[i]
 else:
	print 'wocao'
	print b[i]

