import json
from homework11.config import STORY_FILE
from homework11.engine.keyboards import build_keyboard

with open(STORY_FILE, "r", encoding="utf-8") as f:
    STORY = json.load(f)


async def send_scene(update, user_data):
    scene_id = user_data["current_scene"]
    scene = STORY["scenes"][scene_id]

    text = scene["text"]
    choices = scene.get("choices", {})

    if scene_id in ["party_scene", "party_dance", "party_refuse"]:
        if user_data["gender"] == "Женский":
            vamp_name = "Деймон Сальватор"
            vamp_gender = "Его"
        else:
            vamp_name = "Кэтрин Пирс"
            vamp_gender = "Ее"
        text = text.replace("{vamp_name}", vamp_name).replace("{vamp_gender}", vamp_gender)

    markup = build_keyboard(choices)
    await update.message.reply_text(text, reply_markup=markup, parse_mode="Markdown")

    if not choices:
        user_data["state"] = "finished"
        await update.message.reply_text("🎮 Игра окончена! Используйте /reset, чтобы начать заново.")