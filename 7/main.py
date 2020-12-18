import re
import os 
import string

class Bag(object):

  def __init__(self, name,  children):
    self.name=name
    self.parent=[]
    self.children=children
  
  def __eq__(self, other):
    return self.name == other.name

  def __str__(self):
    childrens='\n'
    if(self.children):
      for s in self.children:
        childrens=childrens+s+'\n'
    return self.name+ " gyerekei:"+childrens



def input_slicing(line):
  data=line.split(" bags contain ")
  ex_bag=data[0]
  inner_bags=[]
  for c in data[1].split(", "):
    #print(c)
    inner_bags.append(c)
  bag=Bag(ex_bag,inner_bags)

  return bag

def listToString(s):  
  str1 = "" 
  return (str1.join(s)) 



dir_path = os.path.dirname(os.path.realpath(__file__))
fo = open(dir_path + '/' + 'input.txt', "r+")
inputs = fo.readlines()
inputs= [item.strip() for item in inputs]
fo.close()

bags=[]
for c in inputs:
  bag=input_slicing(c)
  bags.append(bag)
  print(bag)


  
  
print("vege")