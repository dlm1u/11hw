from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

def build_keyboard(choices):
    if not choices:
        return ReplyKeyboardRemove()

    keyboard = [[choice] for choice in choices.keys()]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

