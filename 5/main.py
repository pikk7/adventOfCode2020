import re
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

fo = open(dir_path + '/' + 'input.txt', "r+")
inputs = fo.readlines()
inputs= [item.strip() for item in inputs]
fo.close()

test0="FBFBBFFRLR"
test1='BFFFBBFRRR'
test2='FFFBBBFRRR'
test3='BBFFBBFRLL'

tests=[test0,test1,test2,test3]

def row(row_data):
  # row_data=text[0:7]
  bit_num=row_data.replace("F","0").replace("B","1")
  return int(bit_num,2)

def column(row_data):
  bit_num=row_data.replace("L","0").replace("R","1")
  return int(bit_num,2)

def set_ID(row_data2,column_data2):
  return row_data2*8+column_data2

def ids(inputs):
  ids=[]
  for x in inputs:
    ids.append(set_ID(row(x[0:7]),column(x[7:10])))
  return ids

def maximum_id(inputs):
  id_array=ids(inputs)
  return max(id_array)

for x in tests:
  row_data=x[0:7]
  column_data=x[7:10]
  print(row(row_data))
  print(column(column_data))
  print(set_ID(row(row_data),column(column_data)))

ids_where=ids(inputs)

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))
seats=range(32,849)


print(Diff(ids_where,seats))