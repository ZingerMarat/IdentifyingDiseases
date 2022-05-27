// EEL

function getRadioButton(value) {
var ele = document.getElementsByName(value);
for(i = 0; i < ele.length; i++) {
    if(ele[i].checked)
        return ele[i].value;
}
}

async function saveDoctorForm(){
    eel.btn_save_doctor($('#fname').val(), $('#lname').val(), $('#id').val(), $('#age').val(), getRadioButton("sex"),
        $('#temp').val(), getRadioButton("smoke"), getRadioButton("pregnancy"), getRadioButton("ethiopian"), getRadioButton("eastern"),
        $('#WBC').val(), $('#Neut').val(), $('#Lymph').val(), $('#RBC').val(),$('#HCT').val(), $('#Urea').val(), $('#Hb').val(), $('#Crtn').val(), $('#Iron').val(), $('#HDL').val(), $('#AP').val()
    )
};

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
      let input = document.createElement('input');
      input.type = 'file';
      input.onchange = _ => {
            let files = input.files[0].name;
            console.log(files);
            eel.get_blood_results(files)
    };


  input.click();

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


function nextStep(){
	$(".next").click(function(){
	if(animating) return false;
	animating = true;

	current_fs = $(this).parent();
	next_fs = $(this).parent().next();

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
}

function previousStep(){
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
}








