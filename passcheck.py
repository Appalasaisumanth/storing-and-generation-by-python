import re
import random 
#addition of new string to re
r=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
def checks(string):
   l=len(string)
   if(l<8 or l>79):
    print("length should be in 8-79 chars")
    return False
   elif not(re.search("[a-z]",string)):
      print("must contain a small letter")
      return False
   elif not(re.search("[A-z]",string)):
      print("must contain a capital letter")
      return False
   elif not (re.search("[0-9]",string)):
      print("must contai a number")
      return False
   elif re.search("[\s\t]",string):
      print("must not contain spaces")
      return False
   elif not(r.search(string)):
      return False
   return True
   
def check(str):
    while True:
        if( checks(str)):
           print("rememember this password ")
           break
        else:
           print("ur password doesn't met our basic conditions but  we are giving other chance to type")
           print("password strength should be improved")
           return False
    return True

class genpass(object):
    def number(self):
        return str(((random.randint(0,9))))
    def capital(self):
        return chr(random.randint(65,90))
    def small(self):
        return chr(random.randint(97,122))
    def specchar(self):
        dict= {1:chr(random.randint(33,47)),
               2:chr(random.randint(58,63)),
               3:chr(random.randint(91,93)),
               4:chr(random.randint(123,126)),
               }
        return dict[random.randint(1,4)]
def create():
    password=genpass()
    dict2={1:password.number(),
       2:password.capital(),
       3:password.small(),
       4:password.specchar()}
    l =random.randint(8,15)
    list=[ 0,0,0,0]
    t=random.randint(1,4)
    list[t-1]+=1
    s=dict2[t]
    while(l>3):
        temp=random.randint(1,4)
        list[temp-1]+=1
        s=s+dict2[temp]
        l-=1
    for i in range(len(list)):
        if list[i]==0:
            s=s+dict2[i+1]
            list[i]+=1
        else:
            if(len(s)<8):
                temp=random.randint(1,4)
                list[temp-1]+=1
                s=s+dict2[temp]
    return s

  
if __name__=="__main__":
   while True:
      print("enter 1. to check ur password strength")
      print("enter 2. to generate a new password")
      print("enter 3. for exit")
      i=int(input(">>> "))
      if i==1:
         print("this will check the password")
         print("you must enter the password of length 8 to 15 characters")
         print("must contain no spaces atleast one special character,one number,one capital and one small")
         str=input(">> ")
         check()
      elif i==2:
        print("you can generate password only length of 8-15")
        str=create()
        print("enter 1.to see ur password")
        j=int(input(">> "))
        if(j==1):
           print(str)
      else:
         print("thankyou for visiting us")
         exit(0)
        