#my project of creating a password checker and generator

num=list(chr(x) for x in range(48, 58))
capchar=list(chr(x) for x in range(65,91))
char=list(chr(x) for x in range(97,123))
sps=list(chr(x) for x in range(32, 48))

def pswd_gen():
    import random
    s=""
    for i in range(3):
        n= str(random.choice(num))
        cap=random.choice(char)
        ch=random.choice(capchar)
        spp=random.choice(sps)
        s=n+ch+cap+spp+s
    return s


def chec(str):
    sl=list(str);sm=cp=sp=nu=0
    for i in sl:
        if i in char:
            sm+=1
        if i in capchar:
            cp+=1
        if i in sps:
            sp+=1
        if i in num:
            nu+=1
    if sm<1 or cp<1 or sp<1 or nu<1: #this is the line to check if the password is good strong or weaak
        return False
    else:
        return True

while True:
    pswd=input("Enter a password")
    condition=chec(pswd)
    if condition==True:
        print("Password is okay.")
        break
    else:
        print("password isn't okay.\nIt should have at least:\n 1 small charcter,\n 1 cap letter, \n 1 special charcetr,\n 1 number")
        resp=input("do you want to generate a new password?Yes or No").lower()
        if resp=="y":
            passw = pswd_gen()
            print(f"This is the new password: \n {passw}")
            break
        else:
            print()