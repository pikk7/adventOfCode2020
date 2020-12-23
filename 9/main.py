import os 
import string

dir_path = os.path.dirname(os.path.realpath(__file__))
fo = open(dir_path + '/' + 'input.txt', "r+")
inputs = fo.readlines()
inputs= [int(item.strip()) for item in inputs]
fo.close()

#first part:

def is_prembeable(index_of_number,array,length):
  """
  CHeck hogy jo e a szam
  """
  i=index_of_number-length
  
  while i<index_of_number:
    j=i+1
    while j<index_of_number:
      if(array[index_of_number]==array[i]+array[j]):
        return True
      j=j+1
    i=i+1

  return False


def bad_number(inputs,index):
  while index<len(inputs):
    c=inputs[index]
    if not(is_prembeable(index,inputs,25)):
      return int(c)
    index+=1

#print(bad_number(inputs,5))

#second part:

def search_numbers(array):
  i=0
  while i<len(array):
    j=0
    while j<len(array):
      #print(sum(array[i:j]))
      if(int(sum(array[i:j]))==badnum):
        return array[i:j]
      j=j+1
    i=i+1
  return -1
  
badnum=bad_number(inputs,25)
upper=(max(search_numbers(inputs)))
lower=(min(search_numbers(inputs)))

print(upper+lower)