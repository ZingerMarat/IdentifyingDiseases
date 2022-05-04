from __future__ import print_function
import eel
from src.py_files.login import login_user, save_register


@eel.expose
def btn_save(login, pass_1, pass_2):
    print(login, pass_1)
    msg = save_register(login, pass_1, pass_2)
    eel.save_return(str(msg))


@eel.expose
def btn_login(user_name, password):
    print(user_name, password)

    msg = login_user(user_name, password)
    eel.login_return(str(msg))


eel.init('src\\web')

try:
    eel.start('html\\login.html', mode="chrome", port=0, size=(1366, 743))
except (SystemExit, MemoryError, KeyboardInterrupt):
    print("client")