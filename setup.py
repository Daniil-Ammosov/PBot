from setuptools import setup
import os

if __name__ == "__main__":
    with open("requirements.txt") as f:
        setup(
                name='p_bot',
                version="0.0.1",
                author='ammosov',
                author_email='ammosov@tbdd.ru',

                packages=[
                    "p_bot",
                    "p_bot/database",
                ],

                scripts=[
                    "scripts/p_bot",
                    # "scripts/deploy_telegram_bot_db"
                ],

                # data_files=[
                #     ("/var/lib/p_bot",           ["alembic/script.py.mako", "alembic/env.py", "alembic/README"]),
                #     ("/var/lib/p_bot/versions",  ["alembic/versions/0c36b3c39152_create_telegram_user_table.py"]),
                #     ("/etc/p_bot",               ["config/alembic.ini", "config/settings.json"]),
                # ],

                url='www.tbdd.ru',
                description='Package for TBDD telegram bot',
                install_requires=f.readlines()
        )

    # Creating log file and SQLite db file
    os.mkdir("/var/log/p_bot", 0x775)
    with open("/var/log/p_bot/log", "w"):
        # with open("/var/lib/p_bot/telegram.db", "w"):
        pass
