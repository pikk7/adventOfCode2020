f=open("input.txt","r")
lines=f.readlines()
lines=[num.strip() for num in lines]
f.close()
i=0
while(i<len(lines)):
    lines[i]=lines[i]*300
    i=i+1

def sloop(sloop_j,sloop_i):
    boom=0
    i=0
    j=0
    while(i<len(lines)):
        c=lines[i][j]
        if(c=="#"):
            boom=boom+1
        j=j+sloop_j
        i=i+sloop_i
    return boom

print(sloop(1,1)*sloop(3,1)*sloop(5,1)*sloop(7,1)*sloop(1,2))