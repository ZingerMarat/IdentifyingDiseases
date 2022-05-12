from __future__ import print_function
import eel
from src.py_files.login import login_user, save_register
from src.py_files.doctor import Doctor


@eel.expose
def btn_save(login, pass_1, pass_2, id):
    msg = save_register(login, pass_1, pass_2, id)
    eel.save_return(str(msg))


@eel.expose
def btn_login(user_name, password):

    msg = login_user(user_name, password)
    eel.login_return(str(msg))


data = None
@eel.expose
def btn_save_doctor(fname, lname, id, age, sex, temp, smoke, pregnancy, ethiopian, eastern):
    msg = ""
    global data
    try:
        doctor_dict = {
            "first_name": fname,
            "last_name": lname,
            "user_id": id,
            "user_age": int(age),
            "user_gender": sex,
            "user_smoking": int(smoke),
            "user_pregnancy": int(pregnancy),
            "user_eastern_community": int(ethiopian),
            "user_ethiopian_community": int(eastern),
            "user_temperature": float(temp),
        }

        doctor = Doctor(doctor_dict)
        doctor.init_doctor()
        msg = doctor.add_patient_info()
        data = doctor.get_all_data()

    except Exception as Error:
        print(Error)
        msg = "failure"
    eel.doctor_return(str(msg))


@eel.expose
def get_blood_results():
    msg = ""
    blood_results = None
    try:
        doc = Doctor()
        blood_results = doc.get_input()
        msg = "success"
    except Exception as Error:
        print(Error)
        msg = "failure"
    eel.blood_return(str(msg), blood_results)

@eel.expose
def send_results():
    msg = ""
    try:
        msg = "success"
    except Exception as Error:
        print(Error)
        msg = "failure"
    eel.get_results(str(msg), data)


eel.init('src\\web')

try:
    eel.start('html\\login.html', mode="chrome", port=0, size=(1920, 1080))
except (SystemExit, MemoryError, KeyboardInterrupt):
    print("client")
