mx=0
msD=0
for i in range(120115, 120201):
    tmp=0
    for j in range(1,i+1):
        if i%j==0:
            tmp+=1
    if tmp>=msD:
        msD=tmp
        mx=i
print(msD, mx)
