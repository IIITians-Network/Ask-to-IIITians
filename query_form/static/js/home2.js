$(function(){
	// This is where we define the accordion container's maximum height, and scrolling if the content overflows.
	var containerOffset = $('#accordion-container').offset(); // gets the container's origin coordinates
	var containerHeight = ($(window).height() - containerOffset.top) - 16; //determines container's maximum height
	$('#accordion-container').css({ // sets container's maximum height & enables vertical scrolling for content overflow
		'max-height': containerHeight, 
		'overflow-y' : 'auto'
	});
});