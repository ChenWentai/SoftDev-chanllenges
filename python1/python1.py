import re
import sys
 
def atoi(text):
  try:
    return int(text) 
  except:
    pass

def natural_keys(text):
 for c in re.findall('(\d+)',text):
   return atoi(c)
#  return [atoi(c) for c in re.findall('(\d+)',text)]

def main(data):
 #print "data:",data
 temp = data.split('\n')
# print "temp:",temp
# for i in range(len(temp)):
 # for c in re.findall('(\d+)',temp[i]):
  # print "atoi:",atoi(c)
  
#  print natural_keys(temp[i])
 temp.sort(key=natural_keys,reverse = True)
 temp = filter(None,temp)
# print "temp:",temp
# print ("temp :",temp)

 return (temp)


'''
# print("sorted temp:",temp)
 order1 = list(range(len(temp)))
 temp2 = list(range(len(temp)))

 for i in range(len(temp)):
  temp2[i] = list(range(1))
  temp2[i][0] = temp[i]
  #if isinstance(natural_keys(temp[i]),int)== True:
  try:
   natural_keys(temp[i])+1 
   natural_keys(temp[i])-1
   order1[i] = natural_keys(temp[i])
  except:
   order1[i] = len(temp)
 # print "natural_keys(temp[%d])" %i,order1[i]
 for i in range(len(temp)):
  temp2[i].insert(0,order1[i][0])

 return (temp2)
'''

def head(s,N):
# print "s:",s
 #print len(s)
 for i in range(len(s)):
  if N == 0:
   break
  print (s[i]) 
#  print 'natural keys:',natural_keys(s[i])
  #print natural_keys(s[i])
#  print (natural_keys(s[i])[0])
  if i >= len(s)-1:
   break
  try:
#   print natural_keys(s[i]),natural_keys(s[i+1])
   if natural_keys(s[i]) == natural_keys(s[i+1]):
    continue
  except:
   pass
  if i>=N-1:
   break

data = sys.stdin.read()
s = main(data)
#count = len(sys.argv)
#if count != 2:
 #print("error! one argument  only")
#elif int(sys.argv[1])>int(len(s)):
 #print("error! expire the maximum line numbers")
#else:
head(s,int(sys.argv[1]))
 
	
 


