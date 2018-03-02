$(function () {
	$(".type-selector").click(function () {
		var $input = $(this);
		if($input.hasClass('active')){
			$(this).removeClass("active");
		}else{
			$(this).addClass("active");
		}
	})
})

$('.real-question').longPress(function(e){
 });
