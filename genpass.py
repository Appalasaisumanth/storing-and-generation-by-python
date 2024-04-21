import random
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
    print(create())

