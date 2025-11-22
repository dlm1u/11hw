from homework11.engine.keyboards import build_keyboard
from homework11.engine.user_manager import users, save_users
from homework11.engine.scene_engine import send_scene
from homework11.config import STORY_FILE
import json

with open(STORY_FILE, "r", encoding="utf-8") as f:
    STORY = json.load(f)

async def handle_message(update, context):
    user_id = str(update.message.from_user.id)
    text = update.message.text

    if user_id not in users:
        await update.message.reply_text("Напиши /start, чтобы начать игру💫")
        return

    user = users[user_id]
    state = user["state"]

    if state == "finished":
        await update.message.reply_text("🎮 Игра уже завершена. Используйте /reset, чтобы начать заново.")
        return

    if state == "waiting_name":
        user["user_name"] = text
        user["state"] = "waiting_gender"
        save_users(users)

        await update.message.reply_text(
            f"Приятно познакомиться, {text}!🌸 Теперь выбери свой пол:",
            reply_markup=build_keyboard({"Мужской": "", "Женский": ""})
        )
        return

    if state == "waiting_gender":
        if text not in ["Мужской", "Женский"]:
            await update.message.reply_text("Выбери вариант с кнопок!")
            return

        user["gender"] = text
        user["state"] = "playing"
        user["current_scene"] = STORY["start_scene"]
        save_users(users)

        await update.message.reply_text("✨Отлично! Приключение начинается...")
        await send_scene(update, user)
        return

    scene = STORY["scenes"][user["current_scene"]]

    if text not in scene["choices"]:
        await update.message.reply_text("Выберите один из вариантов.")
        return

    user["current_scene"] = scene["choices"][text]
    save_users(users)

    await send_scene(update, user)