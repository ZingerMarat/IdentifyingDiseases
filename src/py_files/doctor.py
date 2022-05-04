#dictinary which contains the test results
# -1 low
# 0 medium
# 1 high
# 2 critical

test_results = {'WBC': 0, 'Neut': 0, 'Lymph' : 0,
                'RBC': 0, 'HCT': 0, 'Urea': 0,
                'Hb': 0, 'Crtn': 0, 'Iron': 0,
                'HDL': 0, 'AP': 0}

#dictinary which contains the treatment
# 0 no need to be treated
# 1 need to be treated

disease_treatment = {'Anemia': 0, 'Diet': 0, 'Bleeding' : 0,
                'Hyperlipidemia': 0, 'Disruption_of_blood_formation': 0, 'Hematological_disorder': 0,
                'Iron_poisoning': 0, 'Dehydration': 0, 'Infection': 0,
                'Vitamin_deficiency': 0, 'Viral_disease': 0, 'Diseases_of_the_biliary_tract': 0,
                'Heart_diseases': 0, 'Blood_disease': 0, 'Liver_disease': 0,
                'Kidney_disease': 0, 'Iron_deficiency': 0, 'Muscle_diseases': 0,
                'Smokers': 0, 'Lung_disease': 0, 'Overactive_thyroid_gland': 0,
                'Adult_diabetes': 0, 'Increased_consumption_of_meat': 0, 'Use_of_various_medications': 0,
                'Malnutrition': 0}

#user information
user_age = 32
user_gender = 'm'
user_eastern_community = 0
user_ethiopian_community = 0
user_temperature = 36.6

#variables which contains the test results
WBC = 11001
Neut = 55
Lymph = 53
RBC = 7
HCT = 55
Urea = 44
Hb = 19
Crtn = 1.1
Iron = 161
HDL = 63
AP = 91

def set_test_results(t_r):
    #WBC rating
    if 0 <= user_age <= 3:
        if WBC < 6000:
            t_r['WBC'] = -1
        elif WBC > 17500:
            t_r['WBC'] = 1
    elif 4 <= user_age <= 17:
        if WBC < 5500:
            t_r['WBC'] = -1
        elif WBC > 15500:
            t_r['WBC'] = 1
    elif  user_age >= 18:
        if WBC < 4500:
            t_r['WBC'] = -1
        elif WBC > 11000:
            t_r['WBC'] = 1

    #Neut rating
    if Neut < 28:
        t_r['Neut'] = -1
    elif Neut > 54:
        t_r['Neut'] = 1

    #Lymph rating
    if Lymph < 36:
        t_r['Lymph'] = -1
    elif Lymph > 52:
        t_r['Lymph'] = 1

    #RBC rating
    if RBC < 4.5:
        t_r['RBC'] = -1
    elif RBC > 6:
        t_r['RBC'] = 1

    #HCT rating
    if user_gender == 'm':
        if HCT < 37:
            t_r['HCT'] = -1
        elif HCT > 54:
            t_r['HCT'] = 1
    elif user_gender == 'w':
        if HCT < 33:
            t_r['HCT'] = -1
        elif HCT > 47:
            t_r['HCT'] = 1

    #Urea rating
    if user_eastern_community == 0:
        if Urea < 17:
            t_r['Urea'] = -1
        elif Urea > 43:
            t_r['Urea'] = 1
    elif user_eastern_community == 1:
        if Urea < 17*1.1:
            t_r['Urea'] = -1
        elif Urea > 43*1.1:
            t_r['Urea'] = 1

    #Hb rating
    if user_gender == 'w':
        if Hb < 12:
            t_r['Hb'] = -1
        elif Hb > 16:
            t_r['Hb'] = 1
    elif user_gender == 'm':
        if Hb < 12:
            t_r['Hb'] = -1
        elif Hb > 18:
            t_r['Hb'] = 1
    elif 0 <= user_age <= 17:
        if Hb < 11.5:
            t_r['Hb'] = -1
        elif Hb > 15.5:
            t_r['Hb'] = 1

    #Crtn rating
    if 0 <= user_age <= 2:
        if Crtn < 0.2:
            t_r['Crtn'] = -1
        elif Crtn > 0.5:
            t_r['Crtn'] = 1
    elif 3 <= user_age <= 17:
        if Crtn < 0.5:
            t_r['Crtn'] = -1
        elif Crtn > 1:
            t_r['Crtn'] = 1
    elif 18 <= user_age <= 59:
        if Crtn < 0.6:
            t_r['Crtn'] = -1
        elif Crtn > 1:
            t_r['Crtn'] = 1
    elif 60 <= user_age:
        if Crtn < 0.6:
            t_r['Crtn'] = -1
        elif Crtn > 1.2:
            t_r['Crtn'] = 1

    #Iron rating
    if user_gender == 'm':
        if Iron < 60:
            t_r['Iron'] = -1
        elif Iron > 160:
            t_r['Iron'] = 1
    elif user_gender == 'w':
        if Iron < 60*0.8:
            t_r['Iron'] = -1
        elif Iron > 160*0.8:
            t_r['Iron'] = 1

    #HDL rating
    if user_ethiopian_community == 0:
        if user_gender == 'm':
            if HDL < 29:
                t_r['HDL'] = -1
            elif HDL > 62:
                t_r['HDL'] = 1
        elif user_gender == 'w':
            if HDL < 34:
                t_r['HDL'] = -1
            elif HDL > 82:
                t_r['HDL'] = 1
    elif user_ethiopian_community == 1:
        if user_gender == 'm':
            if HDL < 29*1.2:
                t_r['HDL'] = -1
            elif HDL > 62*1.2:
                t_r['HDL'] = 1
        elif user_gender == 'w':
            if HDL < 34*1.2:
                t_r['HDL'] = -1
            elif HDL > 82*1.2:
                t_r['HDL'] = 1

    #AP rating
    if user_eastern_community == 1:
        if AP < 60:
            t_r['AP'] = -1
        elif AP > 120:
            t_r['AP'] = 1
    elif user_eastern_community == 0:
            if AP < 30:
                t_r['AP'] = -1
            elif AP > 90:
                t_r['AP'] = 1

def set_disease_treatment(t_r, t_d):
    #TODO: finish this
    #WBC condition
    if t_r['WBC'] == 1 and user_temperature >= 37:
        t_d['Infection'] = 1
    elif t_r['WBC'] == -1:
        t_d['Viral_disease'] = 1

set_test_results(test_results)
print(test_results)







