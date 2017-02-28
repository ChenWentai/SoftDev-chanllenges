def puzzle():
    find=False
    path=[]
    map=[[1,1,0,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]]
    w=4
    h=4
    for i in range(h):
        for j in range(w):
            if map[i][j] ==1:
                print "#",           
            else:
                print "O",           
        print 

    path.append((0,0))        
    while not find:
        print '----------------------'       
        for i in range(h):
            for j in range(w):
                if (i,j) in path:                    
                    print "#",
                else:
                    print "O",
            print 
        print '----------------------'
        loc=path.pop()               
        path.append(loc)             
        x,y=loc
        cannot_go=0                  
        if x-1<0:
            cannot_go=1                         
        else:
            if (x-1,y) not in path:          
                if map[x-1][y]==1:          
                    path.append(((x-1,y)))           
                    if(x-1,y)==(h-1,w-1):          
                        find=True                  
                    continue                     
                
        if y+1>=w:
            cannot_go=1
        else:
            if (x,y+1) not in path:
                if map[x][y+1]==1:          
                    path.append(((x,y+1))) 
                    if(x,y+1)==(h-1,w-1):
                        find=True
                    continue
        if x+1>=h:
            cannot_go=1
        else:
            if (x+1,y) not in path:
                if map[x+1][y]==1:
                    path.append(((x+1,y)))
                    if(x+1,y)==(h-1,w-1):
                        find=True
                    continue
        if y-1<0:
            cannot_go=1
        else:
            if (x,y-1) not in path:
                if map[x][y-1]==1:
                    path.append(((x,y-1)))
                    if(x,y-1)==(h-1,w-1):
                        find=True
                    continue
        if cannot_go:
            a=path.pop()           
            map[x][y]=0         

    
    for i in range(h):
        for j in range(w):
            if (i,j) in path:
                print "#",
            else:
                print "O",
#    print len(path)
puzzle()
