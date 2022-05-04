import pandas as pd
import os
import re

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


def add_cred(username, password, user_id):
    credentials = {"username": username, "password": password, "id": user_id}

    cred = pd.DataFrame(credentials, index={30})
    print("cred = pd.DataFrame(credentials, index={30})")
    cred.to_csv(csv_path, index=False, header=False, mode='a')
    print("cred.to_csv(csv_path, index=False, header=False, mode='a')")


def save_register(username, pass_1, pass_2, user_id):
    msg = "failure"
    try:
        if username != "" and pass_1 != "" and pass_2 != "" and pass_1 == pass_2:
            user_msg, pass_msg, id_msg = check_username(username), check_password(pass_1), check_ID(user_id)
            if user_msg == "success" and pass_msg == "success" and id_msg == "success":
                add_cred(username, pass_1, user_id)
                msg = "success"
            elif user_msg != "success":
                msg = user_msg
            elif id_msg != "success":
                msg = id_msg
            elif pass_msg != "success":
                msg = pass_msg

        else:
            msg = "failure"
        return msg
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg


def check_username(username):
    # check if len of username between 6 and 8, contains only letters and max of 2 numbers
    msg = "failure"
    if 6 <= len(username) <= 8:
        count_dig = 0
        let = re.compile(r'[a-zA-Z]')
        dig = re.compile(r'[0-9]')
        for i in username:
            if dig.match(i):
                count_dig += 1
            elif not let.match(i):
                return "alpha failure"

        if 0 <= count_dig <= 2:
            msg = "success"
        else:
            msg = "max digit failure"
    return msg


def check_password(password):
    # check if len of password between 8 and 10, contains at least one number, one letter and one special character
    msg = "failure"
    if 8 <= len(password) <= 10:
        count_dig = 0
        count_spec = 0
        count_let = 0
        dig = re.compile(r'[0-9]')
        let = re.compile(r'[a-zA-Z]')
        spec = re.compile(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]')
        for i in password:
            if dig.match(i):
                count_dig += 1
            elif let.match(i):
                count_let += 1
            elif spec.match(i):
                count_spec += 1

        if count_dig >= 1 and count_let >= 1 and count_spec >= 1:
            msg = "success"
        elif count_dig < 1:
            msg = "digit failure"
        elif count_let < 1:
            msg = "letter failure"
        elif count_spec < 1:
            msg = "special failure"
    return msg


def check_ID(ID):
    # check if ID is a valid
    if len(ID) != 9:
        return "len id failure"
    IdList = list()
    id_list = list(map(int, ID))
    counter = 0

    for i in range(9):
        id_list[i] *= (i % 2) + 1
        if id_list[i] > 9:
            id_list[i] -= 9
        counter += id_list[i]

    if counter % 10 == 0:
        return "success"
    else:
        return "invalid id failure"


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
