nums = [1,20,3,4]
# # for num in nums:
# #   print(num)
  
# nums.append(10)
# # for num in nums:
# #   print(num)
  
# print(len(nums))

# task 1

# def check(num):
#   if num % 2 == 0:
#     return f"{num} is even"
#   else:
#     return  f" {num} is odd"

# input = int(input("Enter a no..."))  
# ans = check(input)
# print(ans)

# task 2

# def total(arr):
#   return sum(arr)

# print(total(nums))

# def total2(arr):
#   ans = 0
#   for i in arr:
#     ans+=i
#   return ans
# print(total2(nums))

# task 3
# def max(arr):
#   ans = arr[0]
#   for i in arr:
#     if i > ans:
#       ans = i
#   return ans

# print(max(nums))

# task 4

def max(arr):
  ans = arr[0]
  for num in arr:
    if num > ans:
      ans=num
  return ans

res = list(map(int ,input().split()))
print(max(res))