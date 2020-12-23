def split(word): 
    return [char for char in word]  
f=open("test.txt","r")
lines=f.readlines()
seats=[split(let.strip()) for let in lines]
f.close()

def check(x,y,seats):
    if(seats[x][y]=="."):
        return False     
    elif(x-1<0 and y-1<0):
        if(seats[x+1][y]!="#" and seats[x][y+1]!="#"  and seats[x+1][y+1]!="#"  and seats[x][y+1]!="#"):
            return True
    elif(x==len(seats)-1 and y==len(seats[x])-1):
        if(seats[x-1][y]!="#"  and seats[x][y-1]!="#"  and seats[x-1][y-1]!="#"  and seats[x][y-1]!="#"):
            return True
    elif(x==len(seats)-1):
        if(seats[x-1][y]!="#"  and seats[x][y-1]!="#" and seats[x][y+1]!="#" and seats[x-1][y-1]!="#"  and seats[x][y-1]!="#" and seats[x][y+1]!="#"):
            return True
    elif(y==len(seats[x])-1):
        if(seats[x-1][y]!="#" and seats[x+1][y]!="#" and seats[x][y-1]!="#" and seats[x-1][y-1]!="#"  and seats[x][y-1]!="#"):
            return True
    elif(x-1<0):
        if( seats[x+1][y]!="#" and seats[x][y-1]!="#" and seats[x][y+1]!="#"  and seats[x+1][y+1]!="#" and seats[x][y-1]!="#" and seats[x][y+1]!="#"):
            return True
    elif(y-1<0):
        if(seats[x-1][y]!="#" and seats[x+1][y]!="#"  and seats[x][y+1]!="#"  and seats[x+1][y+1]!="#"  and seats[x][y+1]!="#"):
            return True
    else:
        if(seats[x-1][y]!="#" and seats[x+1][y]!="#" and seats[x][y-1]!="#" and seats[x][y+1]!="#" and seats[x-1][y-1]!="#" and seats[x+1][y+1]!="#" and seats[x][y-1]!="#" and seats[x][y+1]!="#"):
            return True
    return False


def print_seats(seats):
    for c in seats:
        print(c)


print_seats(seats)
i=0

print('\n')

def changePlace(seats):
    i=0
    output=seats.copy()
    while i<len(seats):
        j=0
        while(j<len(seats[i])):
            # print(i)
            # print(j)
            if(check(i,j,seats)):
                output[i][j]="#"
            j=j+1
        i=i+1

    return output

print_seats(seats)
print('\n')
output=changePlace(seats)
print_seats(output)