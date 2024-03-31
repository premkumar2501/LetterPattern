for i in range(8):
    for j in range(19):
        if j==0 or ((i==0 or i==3) and (j==1 or j==2)) or ((i==1 or i==2) and j==3):
            print('P',end=' ')
        elif j==4 or ((i==0 or i==3) and (j==5 or j==6)) or (i==4 and j==6) or ((i==1 or i==2 or 4<i<8) and j==7):
            print('R',end=' ')
        elif j==8 or ((i==0 or i==3 or i==7) and (j==9 or j==10 or j==11)):
            print('E',end=' ')
        elif j==12 or j==18 or (i==1 and (j==13 or j==17)) or (i==2 and (j==14 or j==16)) or (i==3 and j==15):
            print('M',end=' ')            
        else:
            print(' ',end=' ')
    print()
