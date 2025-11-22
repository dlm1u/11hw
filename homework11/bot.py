from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import BOT_TOKEN
from handlers.start_handler import start
from handlers.command_handler import help_cmd, reset_cmd, stats_cmd
from handlers.message_handler import handle_message


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("reset", reset_cmd))
    app.add_handler(CommandHandler("stats", stats_cmd))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен!")

    app.run_polling()

if __name__ == "__main__":
    main()

