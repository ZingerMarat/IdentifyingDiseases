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