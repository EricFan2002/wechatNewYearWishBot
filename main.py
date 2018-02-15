# coding=utf-8

import itchat
import time

from itchat.content import *



@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    msg.user.send("%s 祝你也新年快乐哦LoL" % msg.user["NickName"])



itchat.auto_login()
friendList = itchat.get_friends(update=True)[1:]
for aFriend in friendList:
    aFriend.send("Hey %s! 祝你新年快乐哦~ (By Eric's Bot@http://)" % aFriend["NickName"])
    time.sleep(1)


