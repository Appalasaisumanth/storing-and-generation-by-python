
import passcheck
import maskpass
from cryptography.fernet import Fernet
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
key = load_key()
fer = Fernet(key)

class user(object):
    def __init__(self,username,password,value):
        self.username=username
        self.password=password
        self.value=value
class all(object):
    def check_they_have_password(self):
        while True:
            choice=int((input("if u have password type 1 then type password \n else type 2 then we will give u password\n")))
            if choice==1:
                passw=maskpass.askpass(mask="*")
                print("enter 1 to see ur password ")
                show=int(input())
                if (show==1):
                    print(passw)
                if passcheck.check(passw):
                    break
            elif choice==2:
                passw=passcheck.create()
                print("this is ur password"+"\n"+passw)
                break
            else:
                print("u made a terrible choice but we are accepting one more time")
        return passw
    def remove_all_its_existance(self,username):
        list=[]
        fin=open("pass.txt","r")
        t=fin.readlines()
        for i in range(len(t)):
            if  username in t[i].split(" "):
                list.append(i)
        while(list):
            t.pop(list.pop()) 
            t.remove("\n")   
        fin.close()
        fin=open("pass.txt","w")
        fin.writelines(t)
        fin.close()
class new(all):
    def create_new_username(self):
        username=input(">enter ur username ")
        all.remove_all_its_existance(self,username)
        passw=all.check_they_have_password(self)
        value=0
        file=open("pass.txt","a")
        file.write("\n"+username+" "+(fer.encrypt(passw.encode())).decode()+" "+str(value))
        file.close()
        
class existing(all):
    def check_existing(self,username, pas):
        f=open("pass.txt",'r')
        t=f.readlines()
        f.close()
        for i in range(len(t)):
            if username  in t[i].split(" "):
                    print("ur account is existing")
                    k=t[i].split(" ")[1]
                    ker=fer.decrypt(k.encode()).decode()
                    if(ker==pas):
                        print("ur password is right")
                        return True
                    else:
                        return "y"
    def change_password(self,username):
        newpass=all.check_they_have_password(self)
        while True:
         newpass2=maskpass.askpass(mask="*")
         if(newpass==newpass2):
            break
         else:
             print("enter the new password once more the before time is wrong")
        fo=open("pass.txt",'r')
        fil=fo.readlines()
        for i in range(len(fil)):
            if username in fil[i].split(" "):
                t=[fil[i],i]
                break
        value=int(fil[i].split(" ").pop(-1))
        fil.pop(i)
        fil.append("\n"+username+" "+fer.encrypt(newpass.encode()).decode()+" "+str(value))
        fo.close()
        fo=open("pass.txt","w")
        fo.writelines(fil)
        fo.close()
        print("password changed successfully")
    def choosing(self):
        pass
    def cast_vote(self,username):
        fo=open("pass.txt",'r')
        fil=fo.readlines()
        for i in range(len(fil)):
            if username in fil[i].split(" "):
                break
        value=int(fil[i].split(" ").pop(-1))
        if(value==0):
            value=value+1
        else:
            print("you already voted")
            return 
        newpass=fil[i].split(" ").pop(-2)
        fil.pop(i)
        fil.append("\n"+username+" "+newpass+" "+str(value))
        fo.close()
        fo=open("pass.txt","w")
        fo.writelines(fil)
        fo.close()
        print("voting completes")

while True:
    print("hey  how we can we help you ")
    print("1.enter 1 for creating new user ")
    print("2.enter 2 for existing user ")
    print("3.enter 3 for exit ")
    ch=int(input(">  "))
    if ch==1:
        print("hi new user ")
        n=new()
        n.create_new_username()
    elif ch==2:
        username=input("enter ur username ")
        password=maskpass.askpass(mask="*")
        print("enter 1 to see ur password ")
        show=int(input())
        if (show==1):
            print(password)
        print("hi {} these are the possibilities  i can do for u".format(username))
        print("first we will check if ur id is   existing in our data base or not")
        o=existing()
        if(o.check_existing(username,password)==True):
            print("you confirmed as existing user u can do the following ")
            print("enter 1. to change password")
            print("enter 2. to cast vote")
            print("enter 3 for exit ")
            while True:
                i=int(input(">>"))
                if(i==1):
                    o.change_password(username)
                elif(i==2):
                    o.cast_vote(username)
                elif(i==3):
                    break
        elif(o.check_existing(username,password)=="y"):
            print("your password is wrong")
            print("please quit and re-enter the password")
            break
        else:
            print("sir ur data not in our database\n so please create new user ")
            print("hi new user ")
            n=new()
            n.create_new_username()

    elif ch==3:
        print("thanks for visiting\n  now bye bye!!")
        break
    else:
        print("you entered a wrong choice")
        print("we are giving one more chance")

 
