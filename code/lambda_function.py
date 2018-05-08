def lambda_handler(event, context):

    message = unicode(str(event['Body']), 'utf-8')
    phone_number = event['From']

    if message.lower() == u"start":
        return "In California, it is illegal to eat oranges while doing what?\n1) Gardening\n2) Bathing\n3) Driving\n4) Working on a computer";
    elif message == "2" or message.lower() == "bathing":
        return "Lucky guess"
    elif message == "1" or message.lower() == "gardening":
        return "Wrong, you lose"
    elif message == "3" or message.lower() == "driving":
        return "Nope"
    elif message == "4" or message.lower() == "working on a computer":
        return "It is literally impossible for you to be more wrong"