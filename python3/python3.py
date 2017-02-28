import sys

import string
#read map,store in 'grid'

name = sys.argv[1]
grid = open(name,'r').read()
#print grid
#print type(grid)
grid = string.split(grid,'\n')
grid = filter(None,grid)
for i in range(len(grid)):
	grid[i] = list(grid[i])
#	print grid[i]
#	print '\n'
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if i>0 and grid[i-1][j] == 'O' and grid[i][j] !='O':
			grid[i][j] = 'P'
temp = grid
for i in range(len(grid)/2):
	str1=grid[i]
	grid[i]=grid[len(grid)-i-1]
	grid[len(grid)-i-1]=str1
	
grid = map(list,zip(*grid))
#print "NIMA"
row = len(grid[i])
#for i in range(len(grid)):
#	print grid[i]
#	print '\n'

#change characters

for i in range(len(grid)):
	grid[i] = [w.replace('#','0')for w in grid[i]]# empty cell
	grid[i] = [w.replace('O','1')for w in grid[i]]# obstacle
	grid[i] = [w.replace('P','1')for w in grid[i]]# obstacle
	grid[i] = [w.replace('E','2')for w in grid[i]]# end point
	grid[i] = [w.replace('S','4')for w in grid[i]]# starting point
colomn = len(grid)
row = len(grid[i])
#print "changed:"
#for i in range(len(grid)):
##	print grid[i]
#	print '\n'
#transaction of maze to suite natural sequence
class Cell(object):
	def __init__(self,x,y,state):
		self.x = x
		self.y = y
		self.parent = None
		self.state = state
		self.position = (x,y)
		self.adja = []
		self.nextmove = ''
test = Cell(-1,-1,'-1')	
#print the maze
#for i in range(colomn):
#	for j in range(row):
#		print grid[i][j],
#	print
#creat map
for i in range(colomn):
	for j in range(row):
		grid[i][j] = Cell(i,j,grid[i][j])

#assign adjacent
for i in range(colomn):
	for j in range(row):
		#right
		if j<row-1:
			grid[i][j].adja.append(grid[i][j+1]) 
		else:
		
			grid[i][j].adja.append(test) 
			
		#up
		if i>0:
			grid[i][j].adja.append(grid[i-1][j])
		else:
			grid[i][j].adja.append(test) 
		#left
		
		if j>0:
			grid[i][j].adja.append(grid[i][j-1])
		else:
			grid[i][j].adja.append(test) 
		
		#down
		if i<colomn-1:
			grid[i][j].adja.append(grid[i+1][j])
		 
		else:
			grid[i][j].adja.append(test) 

		
# print cell information
#for i in range(colomn):
#	for j in range(row):
#		print i,j,'state:',grid[i][j].state
#		for k in range(4):
#			print 'adja:',grid[i][j].adja[k].position,'\n'
		


# Main class search
class search(object):
	def __init__(self,maze):
		self.maze = maze
		colomn = len(self.maze)
		row = len(self.maze[0])
		self.start = maze[0][0]
		
	def findstart(self):
		for i in range(colomn):
			for j in range(row):
				if self.maze[i][j].state == '4':	
					self.start = self.maze[i][j]
					self.start.state = '3'
					return self.start
	def process(self):
		direction = ['U','L','D','R']	
		path = []
		self.findstart()
		path.append(self.start)	
#		print "path:",path
		current = self.start
#		print "current state:",current.state
		find = False
		while not find:
#			print '----------------------'	
			current = path.pop()
			path.append(current)
			cannot_go=[]
			cannot = True
			for i in range(4):

				if current.adja[i].state == '-1' or current.adja[i].state == '1' or current.adja[i].state == '3':
					cannot_go.append(1)
#					print 'wocao'
#					print current.adja[i].state
				else:
#					print 'henwen'
#					print current.adja[i].state
					path.append(current.adja[i])
					current.nextmove = direction[i]
					cannot_go.append(0)
					current.state = '3'
					
							
					if current.adja[i].state == '2':
						find = True	
#						print "Bingo!"
					break
			for i in range(len(cannot_go)):
				if cannot_go[i] == 0:
					cannot = False
					break
#			print "path:",path
#			print "cannot_go[]:",cannot_go			
			if cannot:
				a = path.pop()
				current.state = '3'
			
#			for i in range(colomn):
#				for j in range(row):
#					if self.maze[i][j] in path:
#						print "#",
#					else:
#						print "O",
#				print
		result = ''
		for i in range(len(path)):
			 result+=path[i].nextmove
		print result
		
a = search(grid)
a.process()		
		

























		
#grid = [['0','1','1','0','0'],
#	['0','0','0','1','2'],
#	['0','1','0','0','0'],
#	['0','0','0','1','0']]
#print "maze:",maze
#for i in range(len(grid)):
#	for j in range(len(grid[i])):
#		maze[i][j] = grid[j][i]
#for i in range(len(grid)):
#	print grid[i],'\n'
#	print maze[i],'\n'
'''
row = len(grid)	
colomn = len(grid[0])
def search(x,y):
	if grid[x][y] == '2':
		print 'found at %d,%d' % (x,y)

		result = (x,y)
		print result
		return True

	elif grid [x][y] == '1':
		print 'unreachable at %d,%d' % (x,y)
		return False
	elif grid[x][y] == '3':
		print 'visited at %d,%d' % (x,y)
		return False
	print 'visiting %d,%d' % (x,y)
	
	#mark as visited
	grid[x][y] = '3'
	#explore neighbors 
	#if ((x<row-1 and search(x+1,y))
	 #   or (y > 0 and search(x,y-1))
	  #  or (x>0 and search(x-1,y))
	   # or (y<colomn-1 and search(x,y+1))):
	if ((x<row-1 and search(x+1,y))):
		print 'R'
		return False
	elif (y > 0 and search(x,y-1)):
		print 'D'
		return False
	elif ((x>0 and search(x-1,y))):
		print 'L'
		return False
	elif (y<colomn-1 and search(x,y+1)):
		print 'U'
		return False
search (0,0)
'''
#for i in range(len(grid)):
#
#	print grid[i],'\n'




#print 'underground.map'
#class Maze:
#	def __init__(self,mazeFileName):
#		rowsInMazw = 0
#		columnsInMaze = 0
#		mazeFile = open(mazwFileName,'r')
