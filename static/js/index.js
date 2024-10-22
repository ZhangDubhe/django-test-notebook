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
					var add_html = "<div class='dropdown-item mb-2 type-selector' id='type_"+ res.typeid +"'><b>"+newAdded+"</b></div>";
					$("#type-content").append(add_html);
					$('.type-adder').hide();
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

function update_question() {
	var questionId = parseInt($(".question-header").attr('id').split("_")[1]);
	var name = $(".question-header").text();
	var $ansCard = $(".answer-card");
	
	var right_ans = $ansCard[0].innerText;
	var ans_2 = $ansCard[1].innerText;
	var ans_3 = $ansCard[2].innerText;
	var ans_4 = $ansCard[3].innerText;
	var type = $(".type-selector.active>b").text();
	var type_id = $(".type-selector.active").attr('id');
	if(!type){
		type = 'Base';
		type_id = "type_1";
	}
	type_id = parseInt(type_id.split('_')[1]);
	layer.msg("正在与服务器发生电波关系^W");
	$.post(API_PATH + 'u/' + session.uuid +'/collect/update/',{
		question_id:questionId,
		question_type:type_id,
		question:name,
		rightAns:right_ans,
		wrongAns1:ans_2,
		wrongAns2:ans_3,
		wrongAns3:ans_4,
        csrfmiddlewaretoken:CSRFTOKEN
		},function (res) {
			layer.closeAll();
			res = JSON.parse(res);
			if(res.status == 21){
				layer.msg(res.result);
				location.href = API_PATH + "u/" + session.uuid +'/question/'+questionId;
			}else{
				layer.msg(res.result)
			}
		}
	)
}


function save_question() {
	var type = $(".type-selector.active>b").text();
	var type_id = $(".type-selector.active").attr('id');
	if(!type){
		type = 'Base';
		type_id = "type_1";
	}
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
	type_id = parseInt(type_id.split('_')[1]);
	layer.msg("正在与服务器发生电波关系^W");
	$.post(API_PATH + 'u/' + session.uuid +'/collect/add/',{
		question_type:type_id,
		question:name,
		rightAns:right_ans,
		wrongAns1:ans_2,
		wrongAns2:ans_3,
		wrongAns3:ans_4,
        csrfmiddlewaretoken:CSRFTOKEN
		},function (res) {
			layer.closeAll();
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

function choose_answer(obj) {
	var ans_id = $(obj).attr('id');
	
}

function edit_question() {
	$('#btn-edit').hide();
	$('#btn-tag').show();
	$('#btn-save').show();
	var ans_list =  $('.answer-card');
	if(ans_list.length<4){
		for(var i = 0;i<(4-ans_list.length);i++){
			$(".question-body").append('<div id="answer_'+(ans_list.length+i+1)+'" class="answer-card"> </div>');
		}
	}
	$('.question-body h5').attr('contenteditable',true).addClass('form-line');
	$('.answer-card').attr('contenteditable',true);
	$(".ban-header").text('Edit');
	
	$('.control-panel').append('<p>修改的话，第一个仍然是正确答案哦~</p>')
}

function delete_question(str){
	if(str == 'all'){
		var answers = $(".ans-container").find(".be-deleted");
		var deleted = [];
		answers.forEach(function (value) {
			var thisQuestionId = $(value).attr("id");
			console.log(thisQuestionId.split("_")[1])
			deleted.join(parseInt(thisQuestionId.split("_")[1]))
		})
	}else if( str == 'this' || !str){
		// 单选或在题目页面里选择
		var questionId = parseInt($(".question-header").attr('id').split("_")[1]);
		var deleted = [questionId]
	}
	data = {};
	data.questions = JSON.stringify(deleted);
	data.csrfmiddlewaretoken = CSRFTOKEN;
	console.log(data);
	close_delete();
	layer.msg("正在与服务器发生电波关系^W");
	$.post(API_PATH+'u/'+session.uuid+"/collect/delete/",data,function(result) {
	        res = JSON.parse(result);
	        setTimeout(layer.closeAll(), 1000);
	        if(res.status == 20){
	        	layer.msg("您的题目删除成功了");
	        	setTimeout(location.href = API_PATH + 'u/' + session.uuid + '/',3000);
	        }else{
	        	layer.msg("Request Error");
	        }
	});

}


// 多选编辑 理想为长按
function add_click(obj) {
	var $question = $(obj).parents('real-question');
	console.log($(obj));
	if($question.hasClass("be-deleted")){
		$question.removeClass('be-deleted');
	}else{
		$question.addClass('be-deleted');
	}
}

function control_panel() {
	var panel = $("#user-panel");
	console.log("Click here!");
	if($(panel).hasClass('active')){
		$(panel).removeClass('active')
		$(panel).hide();
		$(".nav-wrapper").hide();
	}else{
		$(panel).addClass('active')
		$(panel).show();
		$(".nav-wrapper").show();
	}
}

function search(){
	var shadow = '<div class="layui-layer-shade" id="layui-layer-shade1" style="z-index:999; background-color:#000; opacity:0.3; filter:alpha(opacity=30);" onclick="close_search()"></div>';
	var content =  '<div class="layer-content"><input id="search-content" oninput="search_question()" class="question-card" type="text" placeholder="search..."><span class="icon icon-search" onclick="search_question()"> </span></div>';
	$("body").append(shadow);
	$("body").append(content);
}
function open_delete(){
	var shadow = '<div class="layui-layer-shade delete-windows" id="layui-layer-shade1" style="z-index:999; background-color:#000; opacity:0.3; filter:alpha(opacity=30);" ></div>';
	var content =  '<center class="delete-windows" style="position: fixed;left: 0;top: 40%;width:100%;z-index:1099;" ><div class="question-card">嘤嘤嘤，你真的要删掉我吗？</div><button class="btn btn-default" onclick="close_delete()">还是不忍心</button><button class="btn btn-secondary" onclick="delete_question()">狠心不要你了</button></center>';
	$("body").append(shadow);
	$("body").append(content);

}

function close_delete() {
	$(".delete-windows").remove();
}
function search_question() {
	var text = $("#search-content").val();
	console.log(text);
	var value = $("#search-content").val().toLowerCase();
    $(".question-card.real-question").filter(function() {
      $(this).toggle($(this).children('p').text().toLowerCase().indexOf(value) > -1)
    });
}
function filter_question(type){
    $(".question-card.real-question").filter(function() {
    	if(type == 'All'){
    	    $(this).toggle(true);
	    }else {
    		$(this).toggle($(this).attr('type') == type)
	    }
    });
}
function close_search() {
	$("#layui-layer-shade1").remove();
	$(".layer-content").remove();
	
}

function shuffle(array) {
    var m = array.length,
        t, i;
    // 如果还剩有元素…
    while (m) {
        // 随机选取一个元素…
        i = Math.floor(Math.random() * m--);
        // 与当前元素进行交换
        t = array[m];
        array[m] = array[i];
        array[i] = t;
    }
    return array;
}