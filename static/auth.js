function check_login() {
	if(!session.uuid || session.uuid == undefined || session.uuid == 'None'){
		location.href = API_PATH + "account/login";
	}
	console.log("Auth ",session.uuid)
}

function login(uuid) {
	session.setItem('uuid',uuid);
	// location.href = API_PATH;
}


function logout() {
	session.removeItem("uuid");
}
