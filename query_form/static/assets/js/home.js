$('body').addClass('js');

$('.acc-heading').on('click', function(){
	$(this).siblings('.acc-content').slideToggle();
	$(this).toggleClass('active');
});

$(window).on('hashchange', function() {
 $('.acc-content:visible').siblings('.acc-heading').addClass('active');
});