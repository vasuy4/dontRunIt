import subprocess
from loader import bot
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_default_commands

from telebot.types import Message
import os


@bot.message_handler(commands=["get"])
def bot_get(message: Message):
    """Отправляет видео из корневого каталога, удаляет его и завершает работу бота"""
    with open("./output.mp4", "rb") as video_file:
        bot.send_video(message.chat.id, video_file)

    try:
        os.remove("./output.mp4")
    except:
        pass

    # bot.stop_polling()


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    """Хэндлер, выводящий сообщение при запуске бота"""
    print("message")
    bot.reply_to(message, "Здарова")



if __name__ == "__main__":
    # subprocess.run(['python', 'camera_recording.py'])  # creationflags=subprocess.CREATE_NO_WINDOW
    print("bot started")

    set_default_commands(bot)
    bot.add_custom_filter(StateFilter(bot))
    bot.infinity_polling()
