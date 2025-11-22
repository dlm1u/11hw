import json
import os
from homework11.config import USERS_FILE

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)


users = load_users()


def create_user(user_id):
    users[user_id] = {
        "state": "waiting_name",
        "user_name": None,
        "gender": None,
        "current_scene": None,
    }
    save_users(users)


def reset_user(user_id):
    if user_id in users:
        del users[user_id]
        save_users(users)
