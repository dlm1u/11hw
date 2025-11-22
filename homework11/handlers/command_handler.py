from homework11.engine.user_manager import users, reset_user

async def help_cmd(update, context):
    await update.message.reply_text(
        "📜 Команды:\n"
        "/start - начать\n"
        "/reset - сбросить игру\n"
        "/stats - статус\n"
        "\help - помощь"
    )


async def reset_cmd(update, context):
    user_id = str(update.message.from_user.id)
    reset_user(user_id)
    await update.message.reply_text("🔄 Прогресс сброшен!")

async def stats_cmd(update, context):
    user_id = str(update.message.from_user.id)

    if user_id not in users or not users[user_id]["current_scene"]:
        await update.message.reply_text("Вы еще не начали игру ❌. Используйте /start 💫")
        return

    user = users[user_id]

    await update.message.reply_text(
        f"📝Ваш профиль:\n"
        f"Имя: {user['user_name']}\n"
        f"Пол: {user['gender']}\n"
        f"Сцена: {user['current_scene']}\n"
    )
