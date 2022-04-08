$(document).ready(function () {

	// Custom JavaScript for the Blog Page

	// Initiate typed.js text effect (done custom for each typed text effect)
	$(".animated-text-effect").typed({ 
		strings: ["May 5,6 and 7, 2022 ", "The Next Wave of Events and Workshops", "Signature of Department of EEE, CEG"], 
		contentType: "text", 
		typeSpeed: 30, 
		loop: true, 
		backDelay: 1200, 
		showCursor: true, 
		startDelay: 3200, // PRELOADER -- comment-out this line if you stop using page preloader
		cursorChar: "|" 
	});

});