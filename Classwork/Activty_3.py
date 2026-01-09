num=int(input("Enter a number: "))
sum=0
temp=num
# power=len(str(num))
power=0
t=num
while t>0:
    digit=t%10
    t//=10
    power+=1
print(power)
while temp > 0:
    digit=temp%10
    sum+=digit**power
    temp//=10
if num==sum:
    print(num, "is an Armstorng number")
else:
    print(num,"is not an armstrong number")

