# with open("FileHandle/data.txt","r") as file:
#   content = file.read()
# print(content)
  
# with open("FileHandle/data.txt" ,"r") as file:
#   for line in file:
#     print(line.strip())   # remove white spaces after line
    
# with open("FileHandle/data.txt","w") as file:
#   file.write("Hello AI Engineer")

with open("fileHandle/data.txt","a") as file:
  file.write("\nNew Line Added")

# count = 0
# with open ("fileHandle/data.txt","r") as file:
#   for line in file:
#     count+=1
#   print(count,"count")

# task 1
# Read a file and print all lines
# with open("filehandle/data.txt","r") as file:
#   for line in file:
#     print(line.strip())
#   content = file.read()
#   print(content)

#task 2
#count word
# with open("filehandle/data.txt","r") as file:
#   count = 0
#   for line in file:
#     count+=len(line.split())
#     print(line.split())
#   print(count)

# 🔥 Task 3:
# Find most frequent word in file
# with open("fileHandle/data.txt","r") as file:
#   freq={}
#   for line in file:
#     keys = line.split()
#     for key in keys:
#       if key in freq:
#         freq[key]+=1
#       else:
#         freq[key]=1
#   print(freq)
  
# max_word = None
# max_count = 0
# for word in freq:
#   if freq[word] > max_count:
#     max_word=word
#     max_count=freq[word]
# print(max_count,max_word)

# task 4
# log analyzer  file .txt

# with open("fileHandle/file.txt","r") as file:
#   freq={}
#   for line in file:
#     key=line.split(":")[0]
#     if key in freq:
#       freq[key]+=1
#     else:
#       freq[key]=1
# print(freq)

# task 5
with open("fileHandle/skill.txt","r") as file:
  for skill in file:
    print(f"Priyanshu Knows {skill.strip()}")
    
