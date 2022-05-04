import pandas as pd
import os
csv_path = os.getcwd() + "\\src\\web\\files\\storage\\users.csv"

def check_credentials(username, password):
    users_csv = pd.read_csv(csv_path, usecols=("username", "password"))
    user_index, password_index = -1, -1
    try:
        user_index = users_csv[users_csv["username"] == username].index[0]
        password_index = users_csv['password'].index[user_index]
    except IndexError as error:
        print(error)
        return False

    return username == users_csv['username'].values[user_index] and \
           password == users_csv['password'].values[password_index]


def add_cred(username, password):
    credentials = {"username": username, "password": password}

    cred = pd.DataFrame(credentials, index={30})
    cred.to_csv(csv_path, index=False, header=False, mode='a')


def save_register(username, pass_1, pass_2):
    try:
        if username != "" and pass_1 != "" and pass_2 != "" and pass_1 == pass_2:
            add_cred(username, pass_1)
            msg = "success"
            return msg
        else:
            msg = "failure"
            return msg
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg

def check_register(username, pass_1, pass_2):
    pass


def login_user(user_name, password):
    try:
        if check_credentials(user_name, password):
            msg = "success"
            print(msg)
            return msg
        else:
            msg = "failure"
            print(msg)
            return msg

    except Exception as Error:
        print(Error)
        msg = "failure"
        print(msg)
        return msg
