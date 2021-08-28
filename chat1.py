from chatterbot import ChatBot
bot = ChatBot('honey')
bot = ChatBot(
    'honey',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
bot = ChatBot(
    'honey',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)
from chatterbot.trainers import ListTrainer
trainer = ListTrainer(bot)
trainer.train(['Hi',
            'Hello',
            'Hi',
            'hey buddy'
            'Hello',
            'Hi',
            'Hello',
            'How are you?',
            'I am good',
            'Glad to hear',
            'How are you?'])
response = bot.get_response('I have a complaint.')

print("Bot Response:", response)
name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)

