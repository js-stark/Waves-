/**
 * Particle HTML Template V2 002
 * Theme JS
 * Author: Dragan Milenkovic
 * Copyright - 2021 Skilltech Web Design - skilltechwebdesign.com
 * URL: https://themeforest.net/item/particle-modern-tech-startup-html-template/20078383?ref=Skilltech
 */

$(document).ready(function () {


	// Desktop Menu Dropdown
	$('.navbar-nav > li > ul > li').on('click', function(e) {
		e.stopPropagation();
		$(this).siblings().removeClass('pa-expand-children');
		$(this).toggleClass('pa-expand-children');
	});



	/** 
	 * Smooth Anchor Scrolling
	 * https://css-tricks.com/snippets/jquery/smooth-scrolling/
	 */

	// Select all links with hashes
	$('a[href*="#"]').not('[href="#"]').not('[href="#0"]').click(function(event) { // Select a AND Remove links that don't actually link to anything
		// On-page links
		if (
			location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') &&
			location.hostname == this.hostname
		) {
			// Figure out element to scroll to
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
			// Does a scroll target exist?
			if (target.length) {
				// Only prevent default if animation is actually gonna happen
				event.preventDefault();
				$('html, body').animate({
					scrollTop: target.offset().top
				}, 800, 'easeInOutQuad',
				function(){
					// Callback after animation
					// Must change focus!
					var $target = $(target);
					$target.focus();
					if ($target.is(":focus")) { // Checking if the target was focused
						return false;
					} else {
						$target.attr('tabindex', '-1'); // Adding tabindex for elements not focusable
						$target.focus(); // Set focus again
					};
				});
			}
		}
	});


	// // Initiate Off Canvas Menu
	// $('#main-nav').hcOffcanvasNav({
	// 	// options here
	// 	disableAt: 1200, // when mobile menu changes to desktop (match here and in main CSS file)
	// 	insertClose: false,
	// 	insertBack: true,
	// 	// labelClose: 'Close', // what it says on the close button
	// 	labelBack: 'Back', // what it says on the back button
	// 	levelTitleAsBack: false,
	// 	pushContent: true,
	// 	pushContent: '.pushable-content', // CSS selector for pushable content container
	// 	position: 'right',
	// 	// width: 280,
	// 	// height: 'auto',
	// 	swipeGestures: true,
	// 	// expanded: false, // initialize the menu in expanded mode
	// 	// levelOpen: 'overlap', // overlap / expand / none
	// 	levelSpacing: 17, // in pixels
	// 	// levelTitles: false, // shows titles for submenus
	// 	// closeOpenLevels: true, // close sub levels when the nav closes
	// 	// closeActiveLevel: false, // clear active levels when the nav closes
	// 	// navTitle: null, // the title of the first level
	// 	// navClass: '', // extra CSS class(es)
	// 	// disableBody: true, // disable body scroll 
	// 	// closeOnClick: true, // close the nav on click
	// 	// customToggle: null, // custom toggle element
	// 	// bodyInsert: 'prepend', // prepend or append the menu to body
	// 	// keepClasses: true, // should original menus and their items classes be preserved or excluded.
	// 	// removeOriginalNav: false, // remove original menu from the DOM
	// 	// rtl: false // enable RTL mode
	// });


	// Configue WOW.js and animate.css elements (animations) - Before initialization
	$('.counterskills').addClass('wow fadeIn');
	$('.fadeInDelay00Duration10').addClass('wow fadeIn');
	$('.fadeInDelay03Duration10').addClass('wow fadeIn');
	$('.fadeInDelay05Duration10').addClass('wow fadeIn');
	$('.fadeInDelay06Duration10').addClass('wow fadeIn');
	$('.fadeInDelay10Duration10').addClass('wow fadeIn');
	$('.fadeInDelay15Duration10').addClass('wow fadeIn');
	$('.fadeInUpDelay03Duration10').addClass('wow fadeInUp');
	$('.fadeInUpDelay06Duration10').addClass('wow fadeInUp');
	$('.fadeInLeftDelay03Duration10').addClass('wow fadeInLeft');
	$('.fadeInLeftDelay05Duration10').addClass('wow fadeInLeft');
	$('.fadeInRightDelay05Duration10').addClass('wow fadeInRight');
	$('.fadeInRightDelay11Duration10').addClass('wow fadeInRight');
	$('.fadeInRight--Custom').addClass('wow fadeInRightCustom');
	$('.fadeInLeft--Custom').addClass('wow fadeInLeftCustom');
	$('.progressBar').addClass('wow progressBar');
	$('.slideup').addClass('wow slideInUp');
	$('.slideUp').addClass('wow slideInUp');
	$('.slideDownDelay10Duration10').addClass('wow slideInDown');
	$('.slideDownDelay07Duration10').addClass('wow slideInDown');
	$('.bounceDelay35Duration12').addClass('wow bounce');


	// Innitiate WOW.js for animations
	new WOW().init();


	// Configue WOW.js and animate.css elements (animations) - After initialization
	$('.counterskills').attr({'data-wow-delay':'1.0s'});
	$('.fadeInDelay00Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.0s'});
	$('.fadeInDelay03Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.3s'});
	$('.fadeInDelay05Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.5s'});
	$('.fadeInDelay06Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.6s'});
	$('.fadeInDelay10Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'1.0s'});
	$('.fadeInDelay15Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'1.5s'});
	$('.fadeInUpDelay03Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.3s'});
	$('.fadeInUpDelay06Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.6s'});
	$('.fadeInLeftDelay03Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.3s'});
	$('.fadeInLeftDelay05Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.5s'});
	$('.fadeInRightDelay05Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.5s'});
	$('.fadeInRightDelay11Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'1.1s'});
	$('.fadeInRight--Custom, .fadeInLeft--Custom').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.5s'});
	$('.fadeInRightDelay11Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'1.1s'});
	$('.slideDownDelay10Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'1.0s'});
	$('.slideDownDelay07Duration10').attr({'data-wow-duration':'1.0s','data-wow-delay':'0.7s'});
	$('.bounceDelay35Duration12').attr({'data-wow-duration':'1.2s','data-wow-delay':'3.5s'});


	// Back to Top Button
	$(window).scroll(function() {    
		var scroll = $(window).scrollTop();
		if (scroll >= 1200) {
			$(".pa-back-to-top-wrap").addClass("pa-backtotop-visible");
		} else {
			$(".pa-back-to-top-wrap").removeClass("pa-backtotop-visible");
		}
	});


	// Dark Mode Switch
	$('span.lm-button').on('click', function(e) {
		event.preventDefault();
		$('body').toggleClass('pa-dark-mode');
		$('.dark-sensitive').toggleClass('pa-dark-mode');
	});

	// $('.parallax-mirror:nth-child(1)').addClass('tp_hce_particle_style');
	// $('.parallax-mirror:nth-child(2)').addClass('hce_form_present');

});