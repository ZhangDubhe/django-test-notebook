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

	$('.answer-card').click(function(){
		var if_edit =  $(this).attr('contenteditable');
		var select_ans = $(this).text();
		if(if_edit == undefined){
			console.log(select_ans,session.answer);
			if(select_ans == session.answer){
				console.log('right');
				$(this).siblings('.answer-card').hide();
			}else{
				$(this).addClass('wrong');
			}
			// $(".align-left").html('<a href="'API_PATH+u/'"></a>')
		}
	})
})

if($('.question-header')){
	var text = $('.question-header').text();
	text = text.replace(/[\(\（]/,'<span class="question-keyword">');
	text = text.replace(/[\(\）]/,'</span>');
	$('.question-header').html(text);
}

