🚀 DAY 5: APIs + CALLING AI MODELS
🎯 Goal:

By end of today:

You understand APIs deeply
You can call real AI models
You build your first AI-powered app
🧠 Step 1: What is an API?

👉 API = bridge between your app and a service

Example:

Your app → sends request
AI model → sends response
🔥 Real Example

You send:

{ "prompt": "Explain AI" }

You get:

{ "response": "AI is..." }

👉 This is exactly how ChatGPT works internally
---------------------------------------------------------------------------------------------------------
🧠 Step 2: Install Required Library

Open terminal:

pip install requests

👉 requests = used to call APIs
-----------------------------------------------------------------------------------------------------------
🧠 Step 3: First API Call (Simple)
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.json())

👉 You’ll get JSON (dictionary)
------------------------------------------------------------------------------------------------------------
🧠 Step 4: Calling AI API (Concept)

Real AI APIs need:

API key
endpoint
JSON body
🔥 Example Structure
import requests

url = "API_ENDPOINT"

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

data = {
    "prompt": "Explain AI"
}

response = requests.post(url, json=data, headers=headers)

print(response.json())
-------------------------------------------------------------------------------------------------
🧠 Step 5: Mini AI App (SIMULATION)

Let’s simulate AI response:

def fake_ai(prompt):
    return f"AI says: {prompt.upper()}"

user_input = input("Ask something: ")
print(fake_ai(user_input))
---------------------------------------------------------------------------------------------------
🧠 Step 6: Real AI (Optional if API key available)

If you later use OpenAI or others, same pattern applies.

🔥 Step 7: Tasks (VERY IMPORTANT)
🔥 Task 1:

Call API and print title

https://jsonplaceholder.typicode.com/posts/1

👉 Output:

title: ...
🔥 Task 2:

Create function:

def ask_ai(prompt):
    # return response
🔥 Task 3:

Take input from user → pass to function → print response

🔥 Task 4 (IMPORTANT):

Build CLI chatbot

You: hello
AI: HELLO

You: exit
Program stops
🧠 Step 8: Real Understanding

👉 Today you learned:

APIs = backbone of AI apps
JSON = communication format
Python = AI control layer
💡 VERY IMPORTANT INSIGHT

👉 You are NOT building AI models
👉 You are building AI-powered systems

This is what companies want 💯