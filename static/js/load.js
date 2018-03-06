$(function () {
	$(".type-selector").click(function () {
		var $input = $(this);
		if($input.hasClass('active')){
			$(this).removeClass("active");
		}else{
			$(this).addClass("active");
		}
	});
	$(".nav-wrapper").click(function () {
		control_panel();
	});
	
})

if($('.question-header')){
	var text = $('.question-header').text();
	text = text.replace(/[\(\（]/,'<span class="question-keyword">');
	text = text.replace(/[\(\）]/,'</span>');
	$('.question-header').html(text);
}

