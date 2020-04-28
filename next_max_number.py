#L = list(range(255))
#trail=0
number=int(input("Enter the number which u need to find higher number of : "))
binn=0
#while trail <256:
        #binn=list(bin(number))
        #binn=L[trail]
binn=list(bin(binn))
lent=len(binn)
Bin= binn[2:(lent+1)]
lent2=len(Bin)
        
if lent2!= 8:
        bin_amp=['0']*(8-lent2)
        Bin=bin_amp+Bin
first=-1
second=-2
print(Bin)
result=0
for x in Bin:
        if Bin[first] == Bin[second]:
                print(first)
                print(second)
                first-=1
                second-=1
        else :
                temp1=Bin[first]
                temp2=Bin[second]
                Bin[second]=temp1
                Bin[first]=temp2
                break
Bin=str(['0','b']+Bin)
print(Bin)
Bb=''.join(Bin)
result=int(Bb,2)
L[trail]=result
print(f'The next Higher number is : {result}')
        #trail+=1        
#print(L)
