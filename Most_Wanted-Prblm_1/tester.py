pol=[0,3,4,6,8]
c=5
m=10


def simulation(pol,c,m):
    pol=sorted(pol)
    limit_right =0
    limit_left=m-1
    pol_left = [x for x in pol if x<c]
    pol_right = [x for x in pol if x>c]
    while True:
        criminal=True
        # print(pol_left)
        # print(pol_right)
        
        if not criminal or len(pol_left)+len(pol_right)==0:
            break
        while len(pol_right)+len(pol_left)>0 : 
            print(pol_left+pol_right,'------',c)
            if not(c-1 in pol_left):
                for i in range(0,len(pol_left)):
                    pol_left[i]+=1
                    
            elif c-1 in pol_left:
                dist=False
                pos_1=0
                pos_2=0
                for i in range(0,len(pol_left)-1):
                    if pol_left[i+1]-pol_left[i]>=3:
                        pos_2=i+1
                        dist=True
                        break
                if dist:
                    for i in range(0,pos_2):
                        pol_left[i]+=1
                    for i in range(pos_2,len(pol_left)):
                        pol_left[i]-=1
                elif not(0 in pol_left):
                    for i in range(0,len(pol_left)):
                        pol_left[i]-=1
                else:
                    pol_left.remove(c-1)
                    for i in range(0,len(pol_left)):
                        pol_left[i]+=1
#caso de right 
 
            if not(c+1 in pol_right):
                for i in range(0,len(pol_right)):
                    pol_right[i]-=1
                    
            elif c+1 in pol_right:
                dist=False
                # pos_1=0
                pos_2=0
                for i in range(0,len(pol_right)-1):
                    if pol_right[i+1]-pol_right[i]>=3:
                        #pos_1=i
                        pos_2=i+1
                        dist=True
                        break
                if dist:
                    for i in range(0,pos_2):
                        pol_right[i]+=1
                    for i in range(pos_2,len(pol_right)):
                        pol_right[i]-=1
                elif not(m-1 in pol_right):
                    for i in range(0,len(pol_right)):
                        pol_right[i]+=1
                else:
                    pol_right.remove(c+1)
                    for i in range(0,len(pol_right)):
                        pol_right[i]-=1               
            

            if len(pol_left) >= 0 and len(pol_right)>0:
                if c-pol_left[-1]>=pol_right[0]-c:
                    if c - pol_left[-1]==1:
                        criminal=False
                        break
                    if not(c+1 in pol_right):
                        c+=1
                    else:
                        c-=1
                else:
                    if not(c-1 in pol_left):
                        c-=1
                    elif not(c+1 in pol_right):
                        c+=1
                    else:
                        criminal=False
                        break
            elif len(pol_left)==0:
                if not(c+1 in pol_right):
                    c+=1
                elif c-1>=0:
                    c-=1
                else:
                    criminal=False
                    break
            else:
                if not(c-1 in pol_left):
                    c-=1
                elif c+1<=m-1:
                    c+=1
                else:
                    criminal=False
                    break   
                        

                      

simulation(pol,c,m)
