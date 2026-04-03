# sum = 0
# for i in range(101):
#   sum+=i
# print(sum)

# i = 0
# sum2 = 0
# while i <=100:
#   sum2+=i
#   i+=1
# print(sum2)

# res = int(input("Give no..."))
# total = 0
# for i in range(0,res + 1):
#   total+=i
  
# print(total)

res = int(input("Enter a no..."))
if res == 0:
  print("Zero")
elif res % 2 ==0:
  print(f"{res} is Even")
else:
  print(f"{res} is Odd")