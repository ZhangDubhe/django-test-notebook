$(function () {
	$(".type-selector").click(function () {
		var $input = $(this);
		var text = $(this).children('b').text();
		if($input.hasClass('active')){
			$(this).removeClass("active");
		}else{
			$(this).addClass("active");
		}
		$(".ban-header").text(text);
		filter_question(text);
	});
	
	$(".type-base").click(function () {
		$(".type-selector").removeClass("active");
		$(".ban-header").text('Base');
		filter_question('All');
	});
	
	$(".nav-wrapper").click(function () {
		control_panel();
	});

	$('div.answer-card').click(function(){
		var if_edit =  $(this).attr('contenteditable');
		var select_ans = $(this).text();
		var result = 0;
		var questionId = parseInt($(".question-header").attr('id').split("_")[1]);
		if(if_edit == undefined){
			console.log(select_ans,session.answer);
			// check whether correct
			if(select_ans == session.answer){
				console.log('right');
				$(this).siblings('.answer-card').hide();
				result = 1;
			}else{
				$(this).addClass('wrong');
			}
			// change icon
			var questionList = JSON.parse(session.question_list);
			var this_index = questionList.indexOf(questionId.toString())

			console.log('now at:',this_index,questionList);
			if(this_index > 0){
				$(".control-panel .align-left").html('<a href="'+API_PATH+'u/'+session.uuid+'/question/'+questionList[this_index-1]+'">\<</a>');
			}
			else{
				$(".control-panel .align-left").html('');
			}
			if(this_index < questionList.length-1){
				$(".control-panel .align-right").html('<a href="'+API_PATH+'u/'+session.uuid+'/question/'+questionList[this_index+1]+'">\></a>');
			}
			else{
				$(".control-panel .align-right").html('');
			}

			// upload to database
			$.post(API_PATH+'u/'+session.uuid+'/question/'+questionId+'/'+result+'/',{
				csrfmiddlewaretoken:CSRFTOKEN
			},function (res) {
				res = JSON.parse(res);
				if(res.status == 20){
					layer.msg('OK next');
				}
			})
		}

	})
})

if($('.question-header')){
	var text = $('.question-header').text();
	text = text.replace(/[\(\（]/,'<span class="question-keyword">');
	text = text.replace(/[\(\）]/,'</span>');
	$('.question-header').html(text);
}

