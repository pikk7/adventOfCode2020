f=open("input.txt","r")
lines=f.readlines()
lines=[int(num.strip()) for num in lines]

def ans1(lines):
    for a in lines:
        for b in lines:
            if(a+b==2020):
                return (a*b)
def ans2(lines):
    for a in lines:
        for b in lines:
            for c in lines:
                if(a+b+c==2020):
                    return (a*b*c)

print(ans1(lines))
print(ans2(lines))