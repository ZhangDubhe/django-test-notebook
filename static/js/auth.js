function check_login() {
	if(!session.uuid || session.uuid == undefined || session.uuid == 'None'){
		location.href = API_PATH + "account/login";
	}
	if(user_name == undefined ){
		// location.href = API_PATH + "account/login";
	}
	console.log("Auth ",session.uuid);
	console.log("Name ",user_name);
	
	
}

function login(uuid, user_name) {
	session.setItem('uuid',uuid);
	// location.href = API_PATH;
}


function logout() {
	session.removeItem("uuid");
}