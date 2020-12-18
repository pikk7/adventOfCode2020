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
    childrens=''
    if(self.children):
      for s in self.children:
        childrens=childrens+s
    return self.name+ " : gyerekei:"+childrens



def input_slicing(line):
  data=line.split(" bags contain ")
  ex_bag=data[0]
  inner_bags=[]
  for c in data[1].split(","):
    inner_bags.append(c)
  bag=Bag(ex_bag,inner_bags)
  #print(ex_bag)
  print(bag)

def listToString(s):  
  str1 = "" 
  return (str1.join(s)) 

if __name__ == "__main__":
  dir_path = os.path.dirname(os.path.realpath(__file__))
  fo = open(dir_path + '/' + 'input.txt', "r+")
  inputs = fo.readlines()
  inputs= [item.strip() for item in inputs]
  fo.close()

  input_slicing(inputs[1])
