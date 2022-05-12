import pytest
from src.py_files.doctor import Doctor



@pytest.fixture()
def doctor():
    patient = {'first_name': 'כפיר', 'last_name': 'גרמן', 'user_id': '205583032', 'user_age': 28, 'user_gender': 'm',
               'user_smoking': 0, 'user_pregnancy': 0, 'user_eastern_community': 0, 'user_ethiopian_community': 0,
               'user_temperature': 36.0}
    doc = Doctor(patient)

    yield doc


def test_add_data(capfd, monkeypatch, doctor):
    doctor.excel_path = f"E:/OneDrive/Desktop/Assignments/Test and Quality/Final Project/src/web/files/storage"
    data = {'First name': ['כפיר'],
            'Last name': ['גרמן'],
            'ID': ['205583032'],
            'Age': [28],
            'Sex': ['m'],
            'Smoking': ['Yes'],
            'Pregnancy': ['Yes'],
            'Community': ['Eastern'],
            'WBC': [10000.0],
            'Neut': [55.0],
            'Lymph': [40.0],
            'RBC': [7.0],
            'HCT': [40.0],
            'Urea': [44.0],
            'Hb': [15.0],
            'Crtn': [1.1],
            'Iron': [80.0],
            'HDL': [63.0],
            'AP': [80.0],
            'Diagnosis': [
                'Disruption_of_blood_formation, Infection, Kidney_disease, Muscle_diseases, Increased_consumption_of_meat'],
            'Recommendation': [
                'כדור 10 מ"ג של B12 ביום למשך חודש, כדור 5 מ"ג של חומצה פולית ביום למשך חודש, אנטיביוטיקה ייעודית, איזון את רמות הסוכר בדם, שני כדורי 5 מ"ג של כורכום c3 של אלטמן ביום למשך חודש, לתאם פגישה עם תזונאי'],
            'unnormal_results': ['Neut - גבוה, RBC - גבוה, Crtn - גבוה, HDL - גבוה, Smoking - גבוה, ']
            }
    doctor.all_data = data

    text = doctor.add_patient_info()

    assert text == "success"
