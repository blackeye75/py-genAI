# task 1
# import requests
# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# print("title...."+response.json()["title"])

# task 2 and 3

# def ask_ai(prompt):
#   return f"Your prompt is {prompt.upper()}"

# res=ask_ai("Hello how are you")
# print(res)

# task 4

def ask_ai(prompt):
    return prompt.upper()

while True:
    user_input = input("You: ")

    if user_input == "exit":
        print("Chat ended.")
        break

    response = ask_ai(user_input)
    print("AI:", response)