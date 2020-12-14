f=open("input.txt","r")
lines=f.readlines()
lines=[num.strip() for num in lines]
f.close()


def valid_pp(lines):
    valid=[]
    i=0
    j=0
    for c in lines:
        c=c.split(" ")
        print(c)
        if(c[0]==''):
            i=0
    return valid
print(valid_pp(lines))
