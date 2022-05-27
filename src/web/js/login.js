$('#login-button').click(function(){
  $('#login-button').fadeOut("slow",function(){
    $("#container").fadeIn();
    TweenMax.from("#container", .4, { scale: 0, ease:Sine.easeInOut});
    TweenMax.to("#container", .4, { scale: 1, ease:Sine.easeInOut});
  });
});

$(".close-btn").click(function(){
  TweenMax.from("#container", .4, { scale: 1, ease:Sine.easeInOut});
  TweenMax.to("#container", .4, { left:"0px", scale: 0, ease:Sine.easeInOut});
  $("#container, #forgotten-container").fadeOut(800, function(){
    $("#login-button").fadeIn(800);
  });
});


	$('#login-button').click(function(){
  $('#login-button').fadeOut("slow",function(){
    $(".login-container").fadeIn();
    TweenMax.from('.login-container', .4, { scale: 0, ease:Sine.easeInOut});
    TweenMax.to('.login-container', .4, { scale: 1, ease:Sine.easeInOut});
  });
});

$(".close-btn").click(function(){
  TweenMax.from('.login-container', .4, { scale: 1, ease:Sine.easeInOut});
  TweenMax.to('.login-container', .4, { left:"0px", scale: 0, ease:Sine.easeInOut});
    $(".login-container").fadeOut(800, function(){
    $("#login-button").fadeIn(800);
  });
});



	// NEW USER REGISTRATION
	async function save_register_js(){
		eel.btn_save($('#new_username').val(),$('#new_pass').val(),$('#new_repass').val(),$('#new_id').val())
	};
	eel.expose(save_return); // USED TO PASS THE FUNCTION TO BE SEEN AT PYTHON
	function save_return(status){
		if (status == "success"){
			$('#return_register').text('תהליך רישום הושלם בהצלחה');
			$('#new_username').val('');
			$('#new_pass').val('');
			$('#new_repass').val('');
			$('#new_id').val('');
		}
		if (status == "failure"){
			$('#return_register').text('שגיאה בתהליך רישום, שדות ריקים או סיסמאות לא תואמות');
		}
		else if (status == "digit failure"){
			$('#return_register').text('שגיאה בתהליך רישום, סיסמא חייבת להכיל לפחות ספרה אחת.');
		}
		else if (status == "letter failure"){
			$('#return_register').text('שגיאה בתהליך רישום, סיסמא חייבת להכיל לפחות אות אחת');
		}
		else if (status == "special failure"){
			$('#return_register').text('שגיאה בתהליך רישום, סיסמא חייבת להכיל לפחות תו מיוחד אחד');
		}
		else if (status == "alpha failure"){
			$('#return_register').text('שגיאה בתהליך רישום, שם משתמש חייב להיות מורכב מאותיות באנגלית.');
		}
		else if (status == "max digit failure"){
			$('#return_register').text('שגיאה בתהליך רישום, שם משתמש יכול להכיל לכל היותר 2 ספרות.');
		}
		else if (status == "invalid id failure"){
			$('#return_register').text('שגיאה בתהליך רישום, תעודת זהות לא חוקית.');
		}
		else if (status == "len id failure"){
			$('#return_register').text('שגיאה בתהליך רישום, אורך לא חוקי של תעודת זהות.');
		}
		else if (status == "user exist"){
			$('#return_register').text('שגיאה בתהליך רישום, שם משתמש קיים במערכת.');
		}
	};

	// USER LOGIN
	async function login_user(){
		eel.btn_login($('#username').val(), $('#password').val())
	};

	eel.expose(login_return)
	function login_return(status){
		if (status == "success"){
			location.href = "./index.html";
		}
		if (status == "failure"){
			$('#login_txt').text("שם משתמש או סיסמא שגויים")
		}
	}


