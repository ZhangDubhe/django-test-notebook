function add_type(){
	newtype = "new type";
	$("#type-content").append(newtype);
}

function add_question() {
	location.href = API_PATH + "u/" + session.uuid + "/collect";
}

function save_question() {
	location.href = API_PATH + "u/" + session.uuid +'/';
}

