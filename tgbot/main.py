import os
import django

from tgbot.bot_app import bot

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djproject.settings")

django.setup()
banned_users = set()
print('BOT ОНЛАЙН')


def main():
    """Функция для входа бота"""
    while True:
        try:
            bot.polling(none_stop=True)
            # send_time_namaz()
        except Exception as error:
            # time.sleep(3)
            print(error)


if __name__ == '__main__':
    main()
