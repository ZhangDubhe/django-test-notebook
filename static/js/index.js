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
	var type = $(".type-selector.active>b").text();
	var type_id = $(".type-selector.active").attr('id');
	if(!type){
		type = 'Base';
		type_id = "type_1";
	}
	type_id = parseInt(type_id.split('_')[1])
	var name = $("#question-name").val();
	var right_ans = $("#ans-1").val();
	var ans_2= $("#ans-2").val();
	var ans_3= $("#ans-3").val();
	var ans_4= $("#ans-4").val();
	if(!name){
		layer.msg("请输入题目");
		return
	}
	if(!right_ans){
		layer.msg("请输入正确答案");
		return
	}
	if(!ans_2){
		layer.msg("请至少输入一个错误答案");
		return
	}
	
	$.post(API_PATH + 'u/' + session.uuid +'/collect/add/',{
		question_type:type_id,
		question:name,
		rightAns:right_ans,
		wrongAns1:ans_2,
		wrongAns2:ans_3,
		wrongAns3:ans_4,
        csrfmiddlewaretoken:CSRFTOKEN
		},function (res) {
			res = JSON.parse(res);
			if(res.status == 21){
				
				layer.msg(res.result)
				
				location.href = API_PATH + "u/" + session.uuid +'/';
			}else{
				layer.msg(res.result)
			}
		}
	)
	
}

$(function () {

	
})

function click_type() {
	var environment = location.href;
	
	if("collection" in environment){
		//select type to upload new questions
		//change content in the interface
	}else if("quiz" in environment){
		//select type to filter question in quiz
		//change background in TYPE
	}else{
		//select to filter content of question to display
		//change content in the interface
	}
}

function open_question(obj){
	var question_id = parseInt($(obj).attr("id").split("_")[1]);
	new_url = API_PATH + 'u/'+ session.uuid +'/question/' + question_id
	location.href = new_url;
}