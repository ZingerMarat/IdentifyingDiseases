

var fnameEl = document.querySelector('#fname');
var lnameEl = document.querySelector('#lname');
var idEl = document.querySelector('#id');
var ageEl = document.querySelector('#age');
var tempEl = document.querySelector('#temp');

const WBCEl = document.querySelector('#WBC');
const NeutEl = document.querySelector('#Neut'); // %
const LymphEl = document.querySelector('#Lymph'); // %
const RBCEl = document.querySelector('#RBC');
const HCTEl = document.querySelector('#HCT'); // %
const UreaEl = document.querySelector('#Urea');
const HbEl = document.querySelector('#Hb');
const CrtnEl = document.querySelector('#Crtn');
const IronEl = document.querySelector('#Iron');
const HDLEl = document.querySelector('#HDL');
const APEl = document.querySelector('#AP');


const form = document.querySelector('#doctorForm');

const checkFname = () => {

    let valid = false;

    const fname = fnameEl.value.trim();

    if (!isRequired(fname)) {
        showError(fnameEl, 'שם פרטי לא יכול להישאר ריק.');
    } else {
        showSuccess(fnameEl);
        valid = true;
    }
    return valid;
};

const checkLname = () => {

    let valid = false;

    const lname = lnameEl.value.trim();

    if (!isRequired(lname)) {
        showError(lnameEl, 'שם משפחה לא יכול להישאר ריק.');
    } else {
        showSuccess(lnameEl);
        valid = true;
    }
    return valid;
}

const checkId = () => {
    let valid = false;

    const id = idEl.value.trim();

    if (!isRequired(id)) {
        showError(idEl, 'תעודת זהות לא יכולה להישאר ריקה.');
    } else if(!onlyNumbers(id)){
        showError(idEl, 'תעודת זהות יכולה להכיל מספרים בלבד.');

    } else if(!(id.length === 9)){
        showError(idEl, 'תעודת זהות חייבת להכיל 9 ספרות.');
    } else {
        showSuccess(idEl);
        valid = true;
    }
    return valid;
}

const checkAge = () => {

    let valid = false;

    const age = ageEl.value.trim();

    if (!isRequired(age)) {
        showError(ageEl, 'גיל לא יכול להישאר ריק.');
    } else if(!(0 <= age && age <= 120)){
        showError(ageEl, 'גיל יכול להיות בין 0 ל 120.');
    } else {
        showSuccess(ageEl);
        valid = true;
    }
    return valid;
}

const checkTemp = () => {
    let valid = false;

    const temp = tempEl.value.trim();

    if (!isRequired(temp)) {
        showError(tempEl, 'טמפרטורה לא יכולה להישאר ריקה.');
    } else if(!(34 <= temp && temp <= 42)){
        showError(tempEl, 'טמפרטורה יכולה להיות בין 34 ל 42.');
    } else {
        showSuccess(tempEl);
        valid = true;
    }
    return valid;
};


const isRequired = value => value === '' ? false : true;


function onlyNumbers(str) {
  return /^[0-9]+$/.test(str);
}

const isBloodResultValid = (blood, name='') =>{
    let valid = "failure";
    if (blood > 0){
        valid = "success";
        if ((name === "Neut" || name === "Lymph" ||name === "HCT")){
            if (blood > 100){
                valid = "not percentage";
            }
        }
    }
    return valid;
}

const checkBlood = (bloodName) => {
    let valid = false;

    let bloodTypes = {
        "WBC": WBCEl,
        "Neut": NeutEl,
        "Lymph": LymphEl,
        "RBC": RBCEl,
        "HCT": HCTEl,
        "Urea": UreaEl,
        "Hb": HbEl,
        "Crtn": CrtnEl,
        "Iron": IronEl,
        "HDL": HDLEl,
        "AP": APEl
    }

    const WBC = WBCEl.value.trim();
    const Neut = NeutEl.value.trim();
    const Lymph = LymphEl.value.trim();
    const RBC = RBCEl.value.trim();
    const HCT = HCTEl.value.trim();
    const Urea = UreaEl.value.trim();
    const Hb = HbEl.value.trim();
    const Crtn = CrtnEl.value.trim();
    const Iron = IronEl.value.trim();
    const HDL = HDLEl.value.trim();
    const AP = APEl.value.trim();

    let blootResults = {
        "WBC": WBC,
        "Neut": Neut,
        "Lymph": Lymph,
        "RBC": RBC,
        "HCT": HCT,
        "Urea": Urea,
        "Hb": Hb,
        "Crtn": Crtn,
        "Iron": Iron,
        "HDL": HDL,
        "AP": AP
    }

    if (!isRequired(blootResults[bloodName])) {
        showError(bloodTypes[bloodName], 'תוצאת בדיקה לא יכולה להישאר ריקה.');

    } else if (isBloodResultValid(blootResults[bloodName]) === "failure") {
        showError(bloodTypes[bloodName], 'תוצאת בדיקה אינה יכולה להיות שלילית.');

    } else if (isBloodResultValid(blootResults[bloodName], bloodName) === "not percentage") {
        showError(bloodTypes[bloodName], 'תוצאת בדיקה באחוזים חייבת להיות בין 0 ל 100.');

    } else {
       showSuccess(bloodTypes[bloodName]);
        valid = true;
    }

    return valid;
};

const showError = (input, message) => {
    // get the form-field element
    const formField = input.parentElement;
    const btnGroup = input.parentElement;
    // add the error class
    formField.classList.remove('success')

    formField.classList.add('error');

    // show the error message
    const error = formField.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    // get the form-field element
    const formField = input.parentElement;

    // remove the error class
    formField.classList.remove('error');
    formField.classList.add('success');

    // hide the error message
    const error = formField.querySelector('small');
    error.textContent = '';
}


const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        // cancel the previous timer
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        // setup a new timer
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

form.addEventListener('input', debounce(function (e) {
    switch (e.target.name) {

        // first step
        case 'fname':
            checkFname();
            break;
        case 'lname':
            checkLname();
            break;
        case 'id':
            checkId();
            break;
        case 'age':
            checkAge();
            break;
        case 'temp':
            checkTemp();
            break;


       case 'WBC':
            checkBlood('WBC');
            break;
        case 'Neut':
            checkBlood('Neut');
            break;
        case 'Lymph':
            checkBlood('Lymph');
            break;
        case 'RBC':
            checkBlood('RBC');
            break;
        case 'HCT':
            checkBlood('HCT');
            break;
        case 'Urea':
            checkBlood('Urea');
            break;
        case 'Hb':
            checkBlood('Hb');
            break;
        case 'Crtn':
            checkBlood('Crtn');
            break;
        case 'Iron':
            checkBlood('Iron');
            break;
        case 'HDL':
            checkBlood('HDL');
            break;
        case 'AP':
            checkBlood('AP');
            break;

    }
}));

let firstStep = false;
let thirdStep = false;

const firstStepComplete = () =>{
    let isFnameValid = checkFname(),
        isLnameValid = checkLname(),
        isIdValid = checkId(),
        isAgeValid = checkAge(),
        isTempValid = checkTemp();

    firstStep = isFnameValid &&
        isLnameValid &&
        isIdValid &&
        isAgeValid &&
        isTempValid;
    if (firstStep){
        nextStep();
    }
    return firstStep;
}


const thirdStepComplete = () =>{

    let WBC = checkBlood("WBC"),
        Neut = checkBlood("Neut") ,
        Lymph = checkBlood("Lymph") ,
        RBC = checkBlood("RBC") ,
        HCT = checkBlood("HCT") ,
        Urea = checkBlood("Urea") ,
        Hb = checkBlood("Hb") ,
        Crtn = checkBlood("Crtn") ,
        Iron = checkBlood("Iron") ,
        HDL = checkBlood("HDL") ,
        AP = checkBlood("AP");

    thirdStep = WBC &&
        Neut &&
        Lymph &&
        RBC &&
       HCT &&
        Urea &&
        Hb &&
       Crtn &&
        Iron &&
        HDL &&
        AP;

    return thirdStep;

}

form.addEventListener('submit', e => {

   e.preventDefault();

   if (firstStepComplete() && thirdStepComplete()) {
      saveDoctorForm();
   }
   else {
       alert("אנא ודא כי כלל השדות מלאים.");
   }
});