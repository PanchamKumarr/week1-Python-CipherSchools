# while
# i=0
# while i<10:
#     print("yes " + str(i))

#     i=i+1 
# print("done")


#for

for i in range (10):
    print(i)
    if i==6:
       break

else:
    print("the loop is exhausted")



# continue statment

for i in range (10):
    if i%2:
        continue
    print(i)



    # for i in range (1,8):
#     print(i)

    #step size to print the alternate numbers

for i in range (1,8,3):
    print(i)
