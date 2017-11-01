# encoding: utf-8

from PidginCli.pidginCli import purple, account


# Send message
def send(msg, user):
    
    conv = purple.PurpleConversationNew(1, account, user)
    im = purple.PurpleConvIm(conv)
    purple.PurpleConvImSend(im, msg)
