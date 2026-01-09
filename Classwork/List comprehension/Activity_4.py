i= [2, 3, 4, 5]
j=[]
for k in i:
    if k%2==0:
        j.append(k)

print(j)

e= [x for x in i if x%2==0]
print(e)