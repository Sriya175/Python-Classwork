# a=10
# b=-10
# print("a>>1=",a>>1)
# print("b>>1=",b>>1)

# a=5
# b=-10
# print("a<<1=",a<<1)
# print("b<<1 =", b<< 1)

print("Enter Marks Obtained in 5 Subjects:")
markOne= int(input())
markTwo= int(input())
markThree= int(input())
markFour= int(input())
markFive= int(input())
tot= markOne+markTwo+markThree+markFour+markFive
avg=tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your grade is A2")
elif avg>=71 and avg<81:
    print("Your grade is B1")
elif avg>=61 and avg<71:
    print("Your grade is B2")
elif avg>=51 and avg<61:
    print("Your grade is C1")
elif avg>=41 and avg<51:
    print("Your grade is C2")
elif avg>=33 and avg<41:
    print("Your grade is D")
elif avg>=21 and avg<33:
    print("Your grade is E1")
elif avg>=0 and avg<21:
    print("Your grade is E2")