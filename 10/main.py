import os 
import string

dir_path = os.path.dirname(os.path.realpath(__file__))
fo = open(dir_path + '/' + 'input.txt', "r+")
inputs = fo.readlines()
inputs= [int(item.strip()) for item in inputs]
fo.close()
inputs.append(max(inputs)+3)
inputs.append(0)
inputs.sort()

#first part:
def first(inputs):
  joilt_1=1
  joilt_3=1

  #print(inputs)

  i=1
  while i<len(inputs):
    if(inputs[i]-inputs[i-1]==1):
      joilt_1+=1
    elif (inputs[i]-inputs[i-1]==3):
      joilt_3+=1
    i+=1

  print(joilt_1*joilt_3)

#first(inputs)


#second part:


def prod(list_of_number):
  szum=1
  for c in list_of_number:
    szum=szum*c
  return szum



def tribonacci(i):
    tribonacciNumbers = [1,1,2]
    index = 0
    while index < i:
        tribonacciNumbers.append(sum(tribonacciNumbers[index:]))
        index += 1
    return tribonacciNumbers[i]


print(inputs)
differences = [inputs[a+1]-inputs[a] for a in range(len(inputs)-1)]
print(differences)
diffString = ''.join([str(num) for num in differences])
print(diffString)
diffStrings = diffString.split('3')
print(diffStrings)
print(prod([tribonacci(len(string)) for string in diffStrings]))
