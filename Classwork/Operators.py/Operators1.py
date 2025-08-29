# # tree1=98
# # tree2=94
# # tree3=41
# # tree4=95
# # tree5=11
# # sum=tree1+tree2+tree3+tree4+tree5
# # print("The sum of all 5 trees is:", sum)
# # average=sum/5
# # print("The average of all 5 trees is:", average)
# try:
#     amount=int(input("Please Enter amount of Withdraw:"))
#     note_1=amount//100
#     note_2=(amount%100)//50
#     note_3=((amount%100)%50)//10
#     note_4=(((amount%100)%50)%10)//5
#     note_5=((((amount%100)%50)%10)%5)//1
#     print("notes of 100 rupees:" , note_1)
#     print("notes of 50 rupees:" , note_2)
#     print("notes of 10 rupees:" , note_3)
#     print("notes of 5 rupees:" , note_4)
#     print("notes of 1 rupees:" , note_5)
# except ValueError:
#     print("Enter a valid integer value")
print("Enter marks obtained in four subjects:")
math=int(input("Maths:"))
english=int(input("English:"))
science=int(input("Science:"))
hindi=int(input("Hindi:"))
sum=math+english+science+hindi
print("sum of Math, English, Science, Hindi: ")
perc=(sum/400)*100
print(end="Percentage Mark = ")
print(perc)