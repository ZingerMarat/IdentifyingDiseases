import pandas as pd
import os
import openpyxl

excel_path = os.getcwd() + r"\src\web\files\storage"


class Doctor:
    def __init__(self, patient_info=None):
        self.test_result = {
            'WBC': 0, 'Neut': 0, 'Lymph': 0,
            'RBC': 0, 'HCT': 0, 'Urea': 0,
            'Hb': 0, 'Crtn': 0, 'Iron': 0,
            'HDL': 0, 'AP': 0
        }

        self.disease_treatment = {
            'Anemia': 0, 'Diet': 0, 'Bleeding': 0,
            'Hyperlipidemia': 0, 'Disruption_of_blood_formation': 0, 'Hematological_disorder': 0,
            'Iron_poisoning': 0, 'Dehydration': 0, 'Infection': 0,
            'Vitamin_deficiency': 0, 'Viral_disease': 0, 'Diseases_of_the_biliary_tract': 0,
            'Heart_diseases': 0, 'Blood_disease': 0, 'Liver_disease': 0,
            'Kidney_disease': 0, 'Iron_deficiency': 0, 'Muscle_diseases': 0,
            'Smokers': 0, 'Lung_disease': 0, 'Overactive_thyroid_gland': 0,
            'Adult_diabetes': 0, 'Cancer': 0, 'Increased_consumption_of_meat': 0,
            'Use_of_various_medications': 0, 'Malnutrition': 0
        }

        self.patient_info = patient_info
        self.blood_results = {}

        self.all_data = None

    def init_doctor(self):
        self.get_input()

        self.set_test_results()
        self.set_disease_treatment()

        self.build_recommendation_list()
        self.set_diagnosis()

    def set_test_results(self):

        # WBC rating
        if 0 <= self.patient_info["user_age"] <= 3:
            if self.blood_results["WBC"] < 6000:
                self.test_result['WBC'] = -1
            elif self.blood_results["WBC"] > 17500 * 1.5:
                self.test_result['WBC'] = 2
            elif self.blood_results["WBC"] > 17500:
                self.test_result['WBC'] = 1
        elif 4 <= self.patient_info["user_age"] <= 17:
            if self.blood_results["WBC"] < 5500:
                self.test_result['WBC'] = -1
            elif self.blood_results["WBC"] > 15500 * 1.5:
                self.test_result['WBC'] = 2
            elif self.blood_results["WBC"] > 15500:
                self.test_result['WBC'] = 1
        elif self.patient_info["user_age"] >= 18:
            if self.blood_results["WBC"] < 4500:
                self.test_result['WBC'] = -1
            elif self.blood_results["WBC"] > 11000 * 1.5:
                self.test_result['WBC'] = 2
            elif self.blood_results["WBC"] > 11000:
                self.test_result['WBC'] = 1

        # Neut rating
        if self.blood_results["Neut"] < 28:
            self.test_result['Neut'] = -1
        elif self.blood_results["Neut"] > 54:
            self.test_result['Neut'] = 1

        # Lymph rating
        if self.blood_results["Lymph"] < 36:
            self.test_result['Lymph'] = -1
        elif self.blood_results["Lymph"] > 52:
            self.test_result['Lymph'] = 1

        # RBC rating
        if self.blood_results["RBC"] < 4.5:
            self.test_result['RBC'] = -1
        elif self.blood_results["RBC"] > 6:
            self.test_result['RBC'] = 1

        # HCT rating
        if self.patient_info["user_gender"] == 'm':
            if self.blood_results["HCT"] < 37:
                self.test_result['HCT'] = -1
            elif self.blood_results["HCT"] > 54:
                self.test_result['HCT'] = 1
        elif self.patient_info["user_gender"] == 'w':
            if self.blood_results["HCT"] < 33:
                self.test_result['HCT'] = -1
            elif self.blood_results["HCT"] > 47:
                self.test_result['HCT'] = 1

        # Urea rating
        if self.patient_info["user_eastern_community"] == 0:
            if self.blood_results["Urea"] < 17:
                self.test_result['Urea'] = -1
            elif self.blood_results["Urea"] > 43:
                self.test_result['Urea'] = 1
        elif self.patient_info["user_eastern_community"] == 1:
            if self.blood_results["Urea"] < 17 * 1.1:
                self.test_result['Urea'] = -1
            elif self.blood_results["Urea"] > 43 * 1.1:
                self.test_result['Urea'] = 1

        # Hb rating
        if self.patient_info["user_gender"] == 'w':
            if self.blood_results["Hb"] < 12:
                self.test_result['Hb'] = -1
            elif self.blood_results["Hb"] > 16:
                self.test_result['Hb'] = 1
        elif self.patient_info["user_gender"] == 'm':
            if self.blood_results["Hb"] < 12:
                self.test_result['Hb'] = -1
            elif self.blood_results["Hb"] > 18:
                self.test_result['Hb'] = 1
        elif 0 <= self.patient_info["user_age"] <= 17:
            if self.blood_results["Hb"] < 11.5:
                self.test_result['Hb'] = -1
            elif self.blood_results["Hb"] > 15.5:
                self.test_result['Hb'] = 1

        # Crtn rating
        if 0 <= self.patient_info["user_age"] <= 2:
            if self.blood_results["Crtn"] < 0.2:
                self.test_result['Crtn'] = -1
            elif self.blood_results["Crtn"] > 0.5:
                self.test_result['Crtn'] = 1
        elif 3 <= self.patient_info["user_age"] <= 17:
            if self.blood_results["Crtn"] < 0.5:
                self.test_result['Crtn'] = -1
            elif self.blood_results["Crtn"] > 1:
                self.test_result['Crtn'] = 1
        elif 18 <= self.patient_info["user_age"] <= 59:
            if self.blood_results["Crtn"] < 0.6:
                self.test_result['Crtn'] = -1
            elif self.blood_results["Crtn"] > 1:
                self.test_result['Crtn'] = 1
        elif 60 <= self.patient_info["user_age"]:
            if self.blood_results["Crtn"] < 0.6:
                self.test_result['Crtn'] = -1
            elif self.blood_results["Crtn"] > 1.2:
                self.test_result['Crtn'] = 1

        # Iron rating
        if self.patient_info["user_gender"] == 'm':
            if self.blood_results["Iron"] < 60:
                self.test_result['Iron'] = -1
            elif self.blood_results["Iron"] > 160:
                self.test_result['Iron'] = 1
        elif self.patient_info["user_gender"] == 'w':
            if self.blood_results["Iron"] < 60 * 0.8:
                self.test_result['Iron'] = -1
            elif self.blood_results["Iron"] > 160 * 0.8:
                self.test_result['Iron'] = 1

        # HDL rating
        if self.patient_info["user_ethiopian_community"] == 0:
            if self.patient_info["user_gender"] == 'm':
                if self.blood_results["HDL"] < 29:
                    self.test_result['HDL'] = -1
                elif self.blood_results["HDL"] > 62:
                    self.test_result['HDL'] = 1
            elif self.patient_info["user_gender"] == 'w':
                if self.blood_results["HDL"] < 34:
                    self.test_result['HDL'] = -1
                elif self.blood_results["HDL"] > 82:
                    self.test_result['HDL'] = 1
        elif self.patient_info["user_ethiopian_community"] == 1:
            if self.patient_info["user_gender"] == 'm':
                if self.blood_results["HDL"] < 29 * 1.2:
                    self.test_result['HDL'] = -1
                elif self.blood_results["HDL"] > 62 * 1.2:
                    self.test_result['HDL'] = 1
            elif self.patient_info["user_gender"] == 'w':
                if self.blood_results["HDL"] < 34 * 1.2:
                    self.test_result['HDL'] = -1
                elif self.blood_results["HDL"] > 82 * 1.2:
                    self.test_result['HDL'] = 1

        # AP rating
        if self.patient_info["user_eastern_community"] == 1:
            if self.blood_results["AP"] < 60:
                self.test_result['AP'] = -1
            elif self.blood_results["AP"] > 120:
                self.test_result['AP'] = 1
        elif self.patient_info["user_eastern_community"] == 0:
            if self.blood_results["AP"] < 30:
                self.test_result['AP'] = -1
            elif self.blood_results["AP"] > 90:
                self.test_result['AP'] = 1

    def build_recommendation_list(self):

        recommendation_list = []

        if self.disease_treatment['Anemia'] == 1:
            recommendation_list.append('שני כדורי 10 מ"ג של B12 ביום למשך חודש ')
        if self.disease_treatment['Diet'] == 1:
            recommendation_list.append('לתאם פגישה עם תזונאי')
        if self.disease_treatment['Bleeding'] == 1:
            recommendation_list.append('להתפנות בדחיפות לבית החולים')
        if self.disease_treatment['Hyperlipidemia'] == 1:
            recommendation_list.append('לתאם פגישה עם תזונאי, כדור 5 מ"ג של סימוביל ביום למשך שבוע')
        if self.disease_treatment['Disruption_of_blood_formation'] == 1:
            recommendation_list.append('כדור 10 מ"ג של B12 ביום למשך חודש')
            recommendation_list.append('כדור 5 מ"ג של חומצה פולית ביום למשך חודש')
        if self.disease_treatment['Hematological_disorder'] == 1:
            recommendation_list.append('זריקה של הורמון לעידוד ייצור תאי הדם האדומים')
        if self.disease_treatment['Iron_poisoning'] == 1:
            recommendation_list.append('להתפנות לבית החולים')
        if self.disease_treatment['Dehydration'] == 1:
            recommendation_list.append('מנוחה מוחלטת בשכיבה, החזרת נוזלים בשתייה')
        if self.disease_treatment['Infection'] == 1:
            recommendation_list.append('אנטיביוטיקה ייעודית')
        if self.disease_treatment['Vitamin_deficiency'] == 1:
            recommendation_list.append('הפנייה לבדיקת דם לזיהוי הוויטמינים החסרים')
            recommendation_list.append('הפנייה לבדיקת דם לזיהוי הוויטמינים החסרים')
        if self.disease_treatment['Viral_disease'] == 1:
            recommendation_list.append('לנוח בבית')
        if self.disease_treatment['Diseases_of_the_biliary_tract'] == 1:
            recommendation_list.append('הפנייה לטיפול כירורגי')
        if self.disease_treatment['Heart_diseases'] == 1:
            recommendation_list.append('לתאם פגישה עם תזונאי')
        if self.disease_treatment['Blood_disease'] == 1:
            if 'לתאם פגישה עם תזונאי' not in recommendation_list:
                recommendation_list.append('שילוב של ציקלופוספאמיד וקורטיקוסרואידים')
        if self.disease_treatment['Liver_disease'] == 1:
            recommendation_list.append('הפנייה לאבחנה ספציפית לצורך קביעת טיפול')
        if self.disease_treatment['Kidney_disease'] == 1:
            recommendation_list.append('איזון את רמות הסוכר בדם')
        if self.disease_treatment['Iron_deficiency'] == 1:
            recommendation_list.append('שני כדורי 10 מ"ג של B12 ביום למשך חודש')
        if self.disease_treatment['Muscle_diseases'] == 1:
            recommendation_list.append('שני כדורי 5 מ"ג של כורכום c3 של אלטמן ביום למשך חודש')
        if self.disease_treatment['Smokers'] == 1:
            recommendation_list.append('להפסיק לעשן')
        if self.disease_treatment['Lung_disease'] == 1:
            recommendation_list.append('להפסיק לעשן / הפנייה לצילום רנטגן של הריאות')
        if self.disease_treatment['Overactive_thyroid_gland'] == 1:
            recommendation_list.append('Propylthiouracil להקטנת פעילות בלוטת התריס')
        if self.disease_treatment['Adult_diabetes'] == 1:
            recommendation_list.append('התאמת אינסולין למטופל')
        if self.disease_treatment['Cancer'] == 1:
            recommendation_list.append('אנטרקטיניב - Entrectinib')
        if self.disease_treatment['Increased_consumption_of_meat'] == 1:
            if 'לתאם פגישה עם תזונאי' not in recommendation_list:
                recommendation_list.append('לתאם פגישה עם תזונאי')
        if self.disease_treatment['Use_of_various_medications'] == 1:
            recommendation_list.append('הפנייה לרופא המשפחה לצורך בדיקת התאמה בין התרופות')
        if self.disease_treatment['Malnutrition'] == 1:
            if 'לתאם פגישה עם תזונאי' not in recommendation_list:
                recommendation_list.append('לתאם פגישה עם תזונאי')

        self.patient_info["Recommendation"] = ", ".join(recommendation_list)

    def set_disease_treatment(self):
        # Smoking person
        if self.patient_info["user_smoking"] == 1:
            self.test_result['Smoking'] = 1

        # WBC condition
        if self.test_result['WBC'] == 1 and self.patient_info["user_temperature"] >= 37:
            self.disease_treatment['Infection'] = 1
        elif self.test_result['WBC'] == 2:
            self.disease_treatment['Blood_disease'] = 1
            self.disease_treatment['Cancer'] = 1
        elif self.test_result['WBC'] == -1:
            self.disease_treatment['Viral_disease'] = 1

        # Neut condition
        if self.test_result['Neut'] == 1:
            self.disease_treatment['Infection'] = 1
        elif self.test_result['Neut'] == -1:
            self.disease_treatment['Disruption_of_blood_formation'] = 1
            self.disease_treatment['Infection'] = 1

        # Lymph condition
        if self.test_result['Lymph'] == 1:
            self.disease_treatment['Infection'] = 1
            self.disease_treatment['Cancer'] = 1
        elif self.test_result['Lymph'] == -1:
            self.disease_treatment['Disruption_of_blood_formation'] = 1

        # RBC condition
        if self.test_result['RBC'] == 1:
            self.disease_treatment['Disruption_of_blood_formation'] = 1
        elif self.test_result['RBC'] == -1:
            self.disease_treatment['Anemia'] = 1
            self.disease_treatment['Bleeding'] = 1

        # HCT condition
        if self.test_result['HCT'] == 1:
            self.disease_treatment['Smokers'] = 1
        elif self.test_result['HCT'] == -1:
            self.disease_treatment['Anemia'] = 1
            self.disease_treatment['Bleeding'] = 1

        # Urea condition
        if self.test_result['Urea'] == 1:
            self.disease_treatment['Kidney_disease'] = 1
            self.disease_treatment['Dehydration'] = 1
            self.disease_treatment['Malnutrition'] = 1
        elif self.test_result['Urea'] == -1 and self.patient_info["user_pregnancy"] == 0:
            self.disease_treatment['Malnutrition'] = 1
            self.disease_treatment['Liver_disease'] = 1

        # Hb condition
        if self.test_result['Hb'] == -1:
            self.disease_treatment['Anemia'] = 1
            self.disease_treatment['Hematological_disorder'] = 1
            self.disease_treatment['Bleeding'] = 1
            self.disease_treatment['Iron_deficiency'] = 1

        # Crtn condition
        if self.test_result['Crtn'] == 1:
            self.disease_treatment['Kidney_disease'] = 1
            self.disease_treatment['Muscle_diseases'] = 1
            self.disease_treatment['Increased_consumption_of_meat'] = 1
        if self.test_result['Crtn'] == -1:
            self.disease_treatment['Malnutrition'] = 1

        # Iron condition
        if self.test_result['Iron'] == 1:
            self.disease_treatment['Iron_poisoning'] = 1
        elif self.test_result['Iron'] == -1:
            self.disease_treatment['Iron_deficiency'] = 1
            self.disease_treatment['Malnutrition'] = 1
            self.disease_treatment['Bleeding'] = 1
            self.disease_treatment['Anemia'] = 1

        # HDL condition
        if self.test_result['HDL'] == -1:
            self.disease_treatment['Heart_diseases'] = 1
            self.disease_treatment['Hyperlipidemia'] = 1
            self.disease_treatment['Adult_diabetes'] = 1

        # AP condition
        if self.test_result['AP'] == 1:
            self.disease_treatment['Liver_disease'] = 1
            self.disease_treatment['Diseases_of_the_biliary_tract'] = 1
            self.disease_treatment['Overactive_thyroid_gland'] = 1
            self.disease_treatment['Use_of_various_medications'] = 1
        elif self.test_result['AP'] == -1:
            self.disease_treatment['Malnutrition'] = 1
            self.disease_treatment['Vitamin_deficiency'] = 1

    def set_diagnosis(self):
        self.patient_info["Diagnosis"] = ", ".join([k for k, v in self.disease_treatment.items() if v == 1])

    def get_unnormal_results(self):
        unnormal = ""
        for k, v in self.test_result.items():
            if v == -1:
                unnormal += f"{k} - נמוך, "
            elif v == 1:
                unnormal += f"{k} - גבוה, "
            elif v == 2:
                unnormal += f"{k} - חריג, "

        self.patient_info["unnormal_results"] = unnormal

    def collect_data(self):
        community = ""
        smoking = ""
        pregnancy = ""
        if self.patient_info["user_ethiopian_community"] == 1:
            community = "Ethiopian"
        if self.patient_info["user_eastern_community"] == 1:
            community = "Eastern"
        if self.patient_info["user_smoking"] == 1:
            smoking = "Yes"
        else:
            smoking = "No"
        if self.patient_info["user_pregnancy"] == 1:
            pregnancy = "Yes"
        else:
            pregnancy = "No"

        if self.blood_results:
            self.patient_info.update(self.blood_results)

        data = {
            "First name": self.patient_info["first_name"],
            "Last name": self.patient_info["last_name"],
            "ID": self.patient_info["user_id"],
            "Age": self.patient_info["user_age"],
            "Sex": self.patient_info["user_gender"],
            "Smoking": smoking,
            "Pregnancy": pregnancy,
            "Community": community,
            "WBC": self.patient_info["WBC"],
            "Neut": self.patient_info["Neut"],
            "Lymph": self.patient_info["Lymph"],
            "RBC": self.patient_info["RBC"],
            "HCT": self.patient_info["HCT"],
            "Urea": self.patient_info["Urea"],
            "Hb": self.patient_info["Hb"],
            "Crtn": self.patient_info["Crtn"],
            "Iron": self.patient_info["Iron"],
            "HDL": self.patient_info["HDL"],
            "AP": self.patient_info["AP"],
            "Diagnosis": self.patient_info["Diagnosis"],
            "Recommendation": self.patient_info["Recommendation"],
        }
        self.patient_info = data
        self.get_unnormal_results()
        data = {k: [v] for k, v in data.items()}
        self.all_data = data

    def get_all_data(self):
        return self.patient_info

    def add_patient_info(self):
        try:
            self.collect_data()

            df = pd.DataFrame(self.all_data)
            wb = openpyxl.load_workbook(excel_path + r"\output.xlsx")

            sheet = wb.active

            for index, row in df.iterrows():
                sheet.append(row.values.tolist())

            wb.save(excel_path + r"\output.xlsx")
            msg = "success"
            return msg
        except Exception as Error:
            print(Error)
            msg = "failure"
            print(msg)
            return msg

    def get_input(self):
        df = pd.read_excel(excel_path + r"\input.xlsx")
        temp = df.to_dict()

        data = {}

        d1 = list(temp["probe"].values())
        d2 = list(temp["result"].values())

        for _ in range(len(d1)):
            data[d1[_]] = d2[_]

        self.blood_results = data
        return data
