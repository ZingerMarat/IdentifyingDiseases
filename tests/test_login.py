import pytest
from src.py_files.login import *


def test_save_register(capfd, monkeypatch):
    path = os.getcwd()[:-6] + r"\src\web\files\storage\users.csv"
    print(path)
    set_path_test(path)

    user_name = "kfir58"
    password = "Q!w2e3r4"
    re_password = "Q!w2e3r4"
    user_id = "205583032"

    text = save_register(user_name, password, re_password, user_id)

    assert text == "success"


def test_check_username(capfd, monkeypatch):
    user_name = "kfir39"

    text = check_username(user_name)

    assert text == "success"


def test_check_ID(capfd, monkeypatch):
    user_id = "205583032"

    text = check_ID(user_id)

    assert text == "success"
