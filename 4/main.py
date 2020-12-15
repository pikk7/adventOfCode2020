import re
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

fo = open(dir_path + '/' + 'input.txt', "r+")
inputs = fo.readlines()
inputs= [item.strip() for item in inputs]
fo.close()


def text_check(text):
  #print(text)
  byr=False
  iyr=False
  eyr=False
  hgt=False
  hcl=False
  ecl=False
  pid=False
  regex='^#([a-f0-9]{6})$'
  if 'byr' in text:
    try:
      tmp=int(text.split('byr:')[1][:4])
      if(1920<=tmp<=2002):
        byr=True
    except:
        byr=False
  if 'iyr' in text:
    try:
      tmp=int(text.split('iyr:')[1][:4])
      if(2010<=tmp<=2020):
        iyr=True
    except:
        iyr=False
  if 'eyr' in text:
    try:
      tmp=int(text.split('eyr:')[1][:4])
      if(2020<=tmp<=2030):
        eyr=True
    except:
        eyr=False
  if 'hgt' in text:
    try:
      tmp=(text.split('hgt:')[1].split(" ")[0])
      measure=tmp[-2:]
      height=int(tmp[:-2])
      if(measure=="cm"):
        hgt=150<=height<=193
      if(measure=="in"):
        hgt=59<=height<=76
    except:
        hgt=False
  if 'hcl' in text:
    try:
      tmp=(text.split('hcl:')[1][:7])
      
      if(re.search(regex,tmp)):
        print(tmp)
        hcl=True
    except:
        hcl=False
  if 'ecl' in text:
    try:
      tmp=(text.split('ecl:')[1][:3])
      #print(tmp)
      if(tmp=="amb" or tmp=="blu" or tmp=="brn" or tmp=="grn" or tmp=="gry" or tmp=="hzl" or tmp=='oth'):
        ecl=True
    except:
        ecl=False
  if 'pid' in text:
    try:
      tmp=int(text.split('pid:')[1][:9])
      pid=True
    except:
      pid=False
  if(byr and iyr and eyr and hgt and hcl and ecl and pid):
    return True
  else:
    return False

def listToString(s):  
  # initialize an empty string 
  str1 = " " 

  # return string   
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

  

print(sum(1 for x in flat_list if text_check(listToString(x))))
