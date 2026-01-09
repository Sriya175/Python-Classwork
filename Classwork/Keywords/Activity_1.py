# a=input("Enter a word: ")
# for i in a:
#     if (i=="A" or i=="a"):
#         print("A is found")
#         break
#     else:
#         print("A not found")

a=input("Enter a word: ")
for i in a:
    if (i=="A" or i=="a"):
        print("A is found")
        continue
    else:
        print("A not found")