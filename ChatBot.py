# import os
from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
                                
SchoolBot = ChatBot("SchoolBot",
                  logic_adapters =[
                    {
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'I am sorry, but I do not understand.',
                        'maximum_similarity_threshold': 0.90
                    }
                ])
        
##corpus_trainer = ChatterBotCorpusTrainer(SchoolBot)
##corpus_trainer.train("chatterbot.corpus.english")


trainer = ChatterBotCorpusTrainer(SchoolBot)

trainer.train(r'C:/Users/17390463/OneDrive - Maynooth University/Documents/ChatBot/greeting.yaml')
trainer.train(r'C:/Users/17390463/OneDrive - Maynooth University/Documents/ChatBot/classes.yaml')
print("Hello, Welcome to the Acdmey of Code! How can I help?")
while(True):
    
    user_input = input()
    if(user_input == 'quit'):
        break
    response = SchoolBot.get_response(user_input)
    print(response)
