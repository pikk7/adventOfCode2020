import re
import os 
import string



dir_path = os.path.dirname(os.path.realpath(__file__))
fo = open(dir_path + '/' + 'input.txt', "r+")
inputs = fo.readlines()
inputs= [item.strip() for item in inputs]
fo.close()


default_inputs=inputs[:]
index_of_change=0
would_be_change=[]
for i,c in enumerate(inputs):
  if(c.startswith("nop") or c.startswith("jmp")):
    would_be_change.append(i)

for c in would_be_change:
  print(c)
  acc=0
  myarray=[]
  inputs=default_inputs[:]
  if(inputs[c].startswith("nop")):
    inputs[c]=inputs[c].replace("nop","jmp")
  if(inputs[c].startswith("jmp")):
    inputs[c]=inputs[c].replace("jmp","nop")
  i=0 
  print(inputs) 
  print(default_inputs)
  while(len(myarray)<len(inputs) and i<len(inputs)):
    data=inputs[i]
    print(data)
    if(i in myarray):
      break
    elif data.startswith("acc"):
      myarray.append(i)
      acc=acc+int(data.split(" ")[1])
      i=i+1
    elif data.startswith("jmp"):
      myarray.append(i)
      i=i+int(data.split(" ")[1])
    else:
      myarray.append(i)
      i=i+1
  if(i==len(inputs)):
    print("fck yeah")
    print(acc)
    break


print("vege")
print(acc)
