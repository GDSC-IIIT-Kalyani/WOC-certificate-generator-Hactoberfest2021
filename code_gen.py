import random as ran
codes = []
alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = [0,1,2,3,4,5,6,7,8,9]
num = int(input("Enter Number Of Winners: "))
for i in range (0,num):
   a = ran.randint(0,9)
   b = ran.randint(0,25)
   codes.append(alphabets[b]+str(numbers[a])+alphabets[int(a+b/2)]+str(numbers[int(a/2)])+alphabets[int(b/2)]+str(numbers[int(a/3)])+alphabets[int(b/3)]+str(numbers[int(a*3)])+alphabets[int(b/4)])
for i in range (0,num):
   print(codes[i])
