🎯 Goal:

By end of today:

You can read/write files
You can process real data (like logs, datasets)
You understand how AI apps handle input data
----------------------------------------------------------------------------------------------
🧠 Step 1: Why File Handling?

👉 In real AI apps:

You read PDFs, logs, datasets
You store results
You process large data

👉 Everything starts with files 💯
-----------------------------------------------------------------------------------------------
🧠 Step 2: Reading Files
✅ Create a file: data.txt

Example content:

Hello Priyanshu
AI is the future
Python is powerful

✅ Read File
with open("data.txt", "r") as file:
    content = file.read()

print(content)

🔥 Line-by-Line (IMPORTANT)
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

👉 .strip() removes extra spaces/newlines
------------------------------------------------------------------------------------------------------
🧠 Step 3: Writing Files
with open("output.txt", "w") as file:
    file.write("Hello AI Engineer 🚀")
----------------------------------------------------------------------------------------------------------
🧠 Step 4: Append Mode
with open("output.txt", "a") as file:
    file.write("\nNew line added")
---------------------------------------------------------------------------------------------------------
🧠 Step 5: Real Use Case

👉 Count number of lines in file

count = 0

with open("data.txt", "r") as file:
    for line in file:
        count += 1

print("Total lines:", count)
----------------------------------------------------------------------------------------------------------
🔥 Step 6: Tasks (VERY IMPORTANT)
🔥 Task 1:

Read a file and print all lines

🔥 Task 2:

Count total words in file

👉 Hint:

line.split()
🔥 Task 3:

Find most frequent word in file

👉 Use:

dictionary (Day 3)
loop
🔥 Task 4 (REAL AI TASK):

Create a log analyzer

File:

ERROR: DB failed
INFO: Server running
ERROR: Timeout
INFO: Connected

👉 Output:

ERROR → 2
INFO → 2

