f=open("input.txt","r")
lines=f.readlines()
lines=[num.strip() for num in lines]
f.close()

def goodPolicy(text):
    # print(text)
    tmp=text.split("-")
    minimum=int(tmp[0])
    maximum=int(tmp[1].split(" ")[0])
    letter=text.split(":")[0][-1]
    renmant=text.split(":")[1].strip()
    # print(tmp)
    # print(minimum)
    # print(maximum)
    # print(letter)
    # print(renmant)
    return minimum<=renmant.count(letter)<=maximum


def goodPolicy2(text):
    # print(text)
    tmp=text.split("-")
    first=int(tmp[0])-1
    second=int(tmp[1].split(" ")[0])-1
    letter=text.split(":")[0][-1]
    renmant=text.split(":")[1].strip()

    if(first>len(renmant)):
        a=False
    else:
        a=(renmant[first]==letter)

    try:
        b=(renmant[second]==letter)
    except:
        b=False
        

    if(a and b):
        return False
    if(a):
        return True
    if(b):
        return True
    return False
    


print(sum(1 for x in lines if goodPolicy2(x)))