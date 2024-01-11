from WebChatGPT import ChatGPT

bot = ChatGPT(
    "portfolio\chat.openai.com.cookies.json"
)
query = input()
response = bot.chat("Hello")

print(response)
#Ouput : What can I do for you today?

