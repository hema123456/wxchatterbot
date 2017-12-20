#!usr/bin/env python
# coding: utf-8

from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot=Bot()
bot.friends()
bot.groups()
#friend = bot.friends()[0] #
#friend.send('Hello')
group = bot.groups().search('快递天团F5')[0]
group.send('我是聊天机器人００７，现在我们可以开始聊天啦！')


chatbot = ChatBot("deepThought")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.chinese")
#自动交互聊天
@bot.register(group)
def reply_my_friend(msg):
    return chatbot.get_response(msg.text).text

#监听消息并转发
# @bot.register(group)
# def print_others(msg):
#     msg.forward(bot.file_helper)

#保持监听状态
embed()