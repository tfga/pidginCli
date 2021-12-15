# encoding: utf-8

from PidginCli.pidginCli import purple, account


# Send message
def send(msg, user):

    # Split account and user if specified using ":" separator
    data = user.split(":")

    if len(data) > 1:
            if data[0] in account.keys():
                spcAccount = account[data[0]]
                user = data[1]
            else:
                raise Exception("Specified account not found")
    else:
        spcAccount = list(account.items())[0][1]

    conv = purple.PurpleConversationNew(1, spcAccount, user)
    im = purple.PurpleConvIm(conv)
    purple.PurpleConvImSend(im, msg)
