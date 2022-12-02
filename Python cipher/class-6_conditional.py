# a=56
# if(a>55):
#     print("True")
# if(a>5):
#     print("False")    
# else:
#     print("maybe")  

a=int(input("enter your age\n"))

if(a>18):
    print("yes")
elif(a>=18):
    print("maybe")
else:
    print("no")





a=int(input("1st person"))
b=int(input("2nd person"))
c=int(input("3rd person"))
d=int(input("4th person"))

if(a>d):
    f1=a
else:
    f1=d
if(b>c):
    f2=b
else:
    f2=c
if(f1>f2):
    print(str(f1) + "is greatest")
else:
    print(str(f2) + "is greatest")