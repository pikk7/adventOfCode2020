import re
import os 
import string
dir_path = os.path.dirname(os.path.realpath(__file__))

fo = open(dir_path + '/' + 'input.txt', "r+")
inputs = fo.readlines()
inputs= [item.strip() for item in inputs]
fo.close()




def listToString(s):  
  str1 = "" 
  return (str1.join(s)) 

j=0
i=0
flat_list=[]
while(i<len(inputs)):
  if(inputs[i]==""):
    flat_list.append(inputs[j:i])
    j=i+1
  i=i+1
flat_list.append(inputs[j:i])

def feladat_ketto(inputs):
  Output = set(inputs[0]) 
  for l in inputs[1:]: 
      Output &= set(l) 
    
  Output = list(Output) 
    
  return len(Output) 

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))  

# print(sum(1 for x in flat_list if text_check(listToString(x))))

# print(inputs)
# print(flat_list)
abc=string.ascii_lowercase
def first_part():
  szum=0
  for x in flat_list:
    szum=szum+(26-len(Diff(abc,listToString(x))))
  print(szum)

#first_part()

def second_part():
  szum=0
  for x in flat_list:
    szum=szum+feladat_ketto(x)
  print(szum)

second_part()