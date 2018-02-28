function add_type(){
	var newAdded = $('#type-inputer').val();
	console.log(newAdded);
	if(newAdded){
		$.post(API_PATH + 'u/' + session.uuid +'/collect/add/',{
				type:newAdded,
	            csrfmiddlewaretoken:CSRFTOKEN
			},function (res) {
				res = JSON.parse(res);
				if(res.status == 20){
					var add_html = "<div class='question-card mb-2' id='type_"+ res.typeid +"'><b>"+newAdded+"</b></div>";
					$("#type-content").append(add_html);
				}else{
					layer.msg(res.result)
				}
			}
		)
	} else {
		layer.msg('请输入正确的类型')
	}

}

function add_question() {
	location.href = API_PATH + "u/" + session.uuid + "/collect";
}

function save_question() {
	location.href = API_PATH + "u/" + session.uuid +'/';
}

