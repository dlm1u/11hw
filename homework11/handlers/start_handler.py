from homework11.engine.user_manager import users, save_users, create_user
from homework11.engine.scene_engine import send_scene
from homework11.engine.keyboards import build_keyboard

async def start(update, context):
    user_id = str(update.message.from_user.id)

    if user_id in users and users[user_id]["current_scene"]:
        await update.message.reply_text(" 👋 C возвращением!")
        await send_scene(update, users[user_id])
        return

    create_user(user_id)
    await update.message.reply_text(" 👋 Добро пожаловать в Мистик Фоллс!\n\nКак тебя зовут?🌟")
