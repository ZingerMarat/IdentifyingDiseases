    function getRadioButton(value) {
    var ele = document.getElementsByName(value);
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked)
            return ele[i].value;
    }
}

	async function saveDoctorForm(){
        eel.btn_save_doctor($('#fname').val(), $('#lname').val(), $('#id').val(), $('#age').val(), getRadioButton("sex"),
            $('#temp').val(), getRadioButton("smoke"), getRadioButton("pregnancy"), getRadioButton("ethiopian"), getRadioButton("eastern"))
	};

let data = null;
    eel.expose(doctor_return)
	function doctor_return(status){
		if (status == "success"){
			location.href = "./results.html";
		}
		if (status == "failure"){
			$('#doctor_txt').text("תהליך הזנת הנתונים נכשל.")
		}
	}

	async function getBloodValues(){
        eel.get_blood_results()
	};

    eel.expose(blood_return)
	function blood_return(status, blood_results){
		if (status == "success"){
            $('#blood_txt').text("בדיקות נטענו בהצלחה.")
            document.getElementById("WBC").value =blood_results["WBC"]
            document.getElementById("Neut").value =blood_results["Neut"]
            document.getElementById("Lymph").value =blood_results["Lymph"]
            document.getElementById("RBC").value =blood_results["RBC"]
            document.getElementById("HCT").value =blood_results["HCT"]
            document.getElementById("Urea").value =blood_results["Urea"]
            document.getElementById("Hb").value =blood_results["Hb"]
            document.getElementById("Crtn").value =blood_results["Crtn"]
            document.getElementById("Iron").value =blood_results["Iron"]
            document.getElementById("HDL").value =blood_results["HDL"]
            document.getElementById("AP").value =blood_results["AP"];
		}
        else if (status == "failure"){
            $('#blood_txt').text("כשל בתהליך טעינת הנתונים.")
        }
        else{
                    $('#blood_txt').text("")

        }
	}

	async function getResults(){
        eel.send_results()
	};
    eel.expose(get_results)
	function get_results(status, data){
		if (status == "success"){

            document.getElementById("firstName").innerHTML =data["First name"]
            document.getElementById("lastName").innerHTML =data["Last name"]
            document.getElementById("id").innerHTML =data["ID"]
            document.getElementById("sex").innerHTML =data["Sex"]
            document.getElementById("age").innerHTML =data["Age"]
            document.getElementById("unnormal").innerHTML =data["unnormal_results"]
            document.getElementById("recommendation").innerHTML =data["Recommendation"]


		}
        else if (status == "failure"){
            $('#blood_txt').text("כשל בתהליך טעינת הנתונים.")
        }

	}

//jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

$(".next").click(function(){
	if(animating) return false;
	animating = true;

	current_fs = $(this).parent();
	next_fs = $(this).parent().next();

	//activate next step on progressbar using the index of next_fs
	$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

	//show the next fieldset
	next_fs.show();
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale current_fs down to 80%
			scale = 1 - (1 - now) * 0.2;
			//2. bring next_fs from the right(50%)
			left = (now * 50)+"%";
			//3. increase opacity of next_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({
        'transform': 'scale('+scale+')',
        'position': 'absolute'
      });
			next_fs.css({'left': left, 'opacity': opacity});
		},
		duration: 800,
		complete: function(){
			current_fs.hide();
			animating = false;
		},
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
});

$(".previous").click(function(){
	if(animating) return false;
	animating = true;

	current_fs = $(this).parent();
	previous_fs = $(this).parent().prev();

	//de-activate current step on progressbar
	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

	//show the previous fieldset
	previous_fs.show();
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale previous_fs from 80% to 100%
			scale = 0.8 + (1 - now) * 0.2;
			//2. take current_fs to the right(50%) - from 0%
			left = ((1-now) * 50)+"%";
			//3. increase opacity of previous_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({'left': left});
			previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
		},
		duration: 800,
		complete: function(){
			current_fs.hide();
			animating = false;
		},
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
});

$(".submit").click(function(){
	return false;
})




const ageEl = document.querySelector('#age');
const tempEl = document.querySelector('#temp');


const form = document.querySelector('#msform');

const WBCEl = document.querySelector('#WBC');
const NeutEl = document.querySelector('#Neut');
const LymphEl = document.querySelector('#Lymph');
const RBCEl = document.querySelector('#RBC');
const HCTEl = document.querySelector('#HCT');
const UreaEl = document.querySelector('#Urea');
const HbEl = document.querySelector('#Hb');
const CrtnEl = document.querySelector('#Crtn');
const IronEl = document.querySelector('#Iron');
const HDLEl = document.querySelector('#HDL');
const APEl = document.querySelector('#AP');



const checkTemp = () => {


    let valid = false;

    const temp = tempEl.value.trim();

    if (!isRequired(temp)) {
        $('#checkTemp_txt').text('שדה חובה, הזן טמפרטורה.')
    } else if (!isTempValid(temp)) {
        $('#checkTemp_txt').text('טמפרטורה לא תקינה, טווח תקין 25-44.')
    } else {
                $('#checkTemp_txt').text('')

        valid = true;
    }
    return valid;
};


const checkAge = () => {
    let valid = false;
    const age = ageEl.value.trim();
    if (!isRequired(age)) {
                $('#checkAge_txt').text('שדה חובה, הזן גיל.')
    } else if (!isAgeValid(age)) {
        $('#checkAge_txt').text('גיל לא תקין, טווח תקין 0-120.')

    } else {
                $('#checkAge_txt').text("")

        valid = true;
    }
    return valid;
};

const checkBlood = (bloodName) => {
    let valid = false;
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


    if (!isRequired(blootResults[bloodName]))  $('#blood_txt').text('שדה חובה, הזן תוצאות בדיקת דם.')
    else if (!isBloodResultValid(blootResults[bloodName])) $('#blood_txt').text('תוצאה לא תקינה, תוצאה לא יכולה להכיל ערכים שליליים.')
    else {
        $('#blood_txt').text("")
        valid = true;
    }
    return valid;
};
const isAgeValid = (age) => {
    return 0 < age && age < 120;
};

const isRequired = value => value === '' ? false : true;
const isTempValid = (temp) => {
    return 25 < temp && temp < 44;
};

const isBloodResultValid = (blood) =>{
    console.error(blood)
    return blood > 0;
}



form.addEventListener('submit', function (e) {
    // prevent the form from submitting
    e.preventDefault();

    // validate fields
    let isAgeValid = checkAge(),
        isTempValid = checkTemp(),
        isBloodValid = checkBlood();

    let isFormValid = isAgeValid &&
        isTempValid && isBloodValid
    // submit to the server if the form is valid
    if (isFormValid) {
        saveDoctorForm();
    }
});


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
    switch (e.target.id) {
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



