import json
import datetime

class Chatbot:
    def __init__(self, bot_name):  # Changed 'init' to '__init__'
        self.bot_name = bot_name
        self.conversations = []

    def respond(self, user_input):
        response = f"Hello! You said: {user_input}"  # Simple echo response
        return response

    def log_conversation(self, user_input, response):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.conversations.append({"timestamp": timestamp, "user": user_input, "bot": response})

    def save_logs(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.conversations, file, indent=4)

class ChatbotManager:
    def __init__(self):  # Changed 'init' to '__init__'
        self.chatbots = {}

    def create_chatbot(self, bot_name):
        if bot_name in self.chatbots:
            print(f"Chatbot '{bot_name}' already exists.")
        else:
            self.chatbots[bot_name] = Chatbot(bot_name)
            print(f"Chatbot '{bot_name}' created successfully.")

    def get_chatbot(self, bot_name):
        return self.chatbots.get(bot_name, None)

    def list_chatbots(self):
        return list(self.chatbots.keys())

if __name__ == "__main__":  # Corrected the 'if name == "main":' line
    manager = ChatbotManager()
    manager.create_chatbot("SupportBot")
    bot = manager.get_chatbot("SupportBot")
    
    if bot:
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                bot.save_logs("chat_logs.json")
                print("Chat logs saved. Exiting...")
                break
            bot.log_conversation(user_input, bot.respond(user_input))  # Log conversation
            print(f"{bot.bot_name}: {bot.respond(user_input)}")
