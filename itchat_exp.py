import itchat

@itchat.msg_register([itchat.content.TEXT,
                      itchat.content.MAP,
                      itchat.content.CARD,
                      itchat.content.NOTE,
                      itchat.content.SHARING])
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))
    print(msg)


itchat.auto_login(hotReload=True)
itchat.run()
# itchat.send("Hello, again", toUserName="filehelper")
