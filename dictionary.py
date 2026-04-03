# dictionary

# user = {
#     "name": "Priyanshu",
#     "age": 23,
#     "is_dev": True
# }
# print(user["name"])
# print(user.get("name"))    safe

# print(user.items())    

# for key in user:
#   print(key)
#   print(user[key])
  
# for key, value in user.items():
#   print(key,value)
  
  
# response = {
#     "status": "success",
#     "data": {
#         "answer": "AI is future"
#     }
# }
# print(response.items())
# response["data"]["answer"]="AI is Cool"
# print(response["data"]["answer"])


# list of dictionary

# users = [
#     {"name": "Priyanshu", "age": 23},
#     {"name": "Rohit", "age": 25},
#     {"name": "Aman", "age": 21}
# ]

# for user in users:
#   print(user["name"],user["age"])


# task 1
# Create a dictionary for a student
# name, age, marks
# Print all values

# student = {
#   "name" : "Priyanshu Raj",
#   "age":25,
#   "marks" : 100
# }
# for key in student:
#   print(student[key])

# task 2
# student["marks"]=90
# for key in student:
#   print(student[key])


# task 3
# Find student with highest marks

# students = [
#  {"name": "A", "marks": 80},
#  {"name": "B", "marks": 95},
#  {"name": "C", "marks": 789}
# ]

# max=students[0]
# for stud in students:
#   if stud["marks"]> max["marks"]:
#     max=stud
# print(max["name"])


#task 4
# count freq of nums
# nums = [1,1,2,3,3,3,4]
# freq = {}
# for num in nums:
#   if num in freq:
#     freq[num]+=1
#   else:
#     freq[num]=1

# print(freq)


# task 5
# 👉 Print:
# Priyanshu knows Python
# Priyanshu knows AI
# Priyanshu knows MERN
data = {
    "user": {
        "name": "Priyanshu",
        "skills": ["Python", "AI", "MERN","Node"]
    }
}

for skill in data["user"]["skills"]:
  # print(data["user"]["name"]+ " knows " + skill )
  print(f"{data['user']['name']} knows {skill}")
