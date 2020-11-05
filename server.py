from chatbox import bot

update_id = None


def make_reply():
    reply = "Okay"
    return reply


while True:
    print(...)
    updates = bot.telegram_chatbot.get_update(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.telegram_chatbot.send_message(reply, from_)

