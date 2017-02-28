'''import pickle
t1 = ('this is a string', 42, [1,2,3],None)
print "t1:",t1
p1 = pickle.dumps(t1)
print "p1:",p1
t2 = pickle.loads(p1)
print "t2:",t2

'''
import datetime,time
s = '09-08-2016'
date_input = datetime.date.fromtimestamp(time.mktime(time.strptime(s,"%d-%m-%Y")))
n = datetime.datetime.weekday(date_input)
print n
