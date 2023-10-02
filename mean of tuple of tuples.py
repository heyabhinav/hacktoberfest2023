tup1 = ((1,2),(3,4.15,5.15),(7,8,12,15))
s2=0
for i in range(len(tup1)):
    s=0
    for j in range(len(tup1[i])):
        s=s+tup1[i][j]
    m1 = s/len(tup1[i])
    print("Mean of element"+str(i+1),":",m1)
    s2+=m1
m2 = s2/len(tup1)
print("Mean of means :",m2)
