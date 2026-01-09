L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Orignal list:", L)

count=0

for i in L:
    count += i

avg = count/len(L)

print("sum= ", count)
print("average= ", avg)

L.sort()

print("The sorted list is: ",L)

print("Smallest element is: ", L[0])
print("Largest element is: ", L[-1])

