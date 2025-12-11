/*==========

Theme Name: DeCore - Architecture & Interior HTML5 Template
Theme Version: 1.0

==========*/

/*==========
----- JS INDEX -----
1.Whole Script Strict Mode Syntax
2.Reviews Slider JS
3.Brands Slider JS
4.Page Loader And WOW Animation JS
5.Menu Open JS
6.DropDown Menu JS
7.Mobile Navigation Menu Removeclass JS
7.Sticky Header JS
8.Scroll To Top JS
9.Project Tabbing JS
==========*/


jQuery(document).ready(function($) {

    // Whole Script Strict Mode Syntax
    "use strict";

    // Reviews Slider JS

    var reviews_slider = new Swiper(".reviews-slider", {
        slidesPerView: 2,
        spaceBetween: 30,
        loop: true,
        speed: 2000,
        autoplay: true,
        grabCursor: true,

        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },

        breakpoints: {
            "@0.00": {
                slidesPerView: 1,
            },
            "@01.00": {
                slidesPerView: 1,
                spaceBetween: 20,
            },
            "@1.50": {
                slidesPerView: 1.9,
            },
        }
    });

    // Reviews Slider JS End

    // Brands Slider JS

    var brands_slider = new Swiper(".brands-slider", {
        slidesPerView: 4.5,
        spaceBetween: 30,
        loop: true,
        autoplay: true,
        speed: 2000,

        breakpoints: {
            "@0.00": {
                slidesPerView: 2,
            },
            "@0.75": {
                slidesPerView: 3.5,
                spaceBetween: 20,
            },
            "@1.50": {
                slidesPerView: 4,
            },
        }
    });

    // Brands Slider JS End

    // Page Loader And Wow Animation JS

    $(window).ready(function() {
        $('.page-loader').fadeOut();
        // Loader JS End
        $('body').removeClass('body-fixed');
        // Wow Animation JS Start
        new WOW().init();
        // Wow Animation JS Start
    });

    // Page Loader And Wow Animation JS End

    // Menu Open JS

    jQuery(".menu-toggle").click(function() {
        jQuery(".main-navigation").toggleClass("toggled");
    });

    // Menu Open JS End

    // DropDown Menu JS

    jQuery(".dropdown-items").click(function() {
        var cur = jQuery(this).closest(".dropdown-items");
        jQuery(".dropdown-items").not(cur).removeClass("dropdown-open");
        jQuery(this).closest(".dropdown-items").toggleClass("dropdown-open");
    });

    // DropDown Menu JS End

    // Mobile Navigation Menu Removeclass

    jQuery('.header-menu ul li a:not(.dropdown-items>a)').click(function() {
        jQuery('.header-wrapper nav').removeClass('toggled');
    });

    // Mobile Navigation Menu Removeclass End

    // Sticky Header JS

    // jQuery(window).scroll(function() { // this will work when your window scrolled.
    //     var height = jQuery(window).scrollTop(); //getting the scrolling height of window
    //     if (height > 20) {
    //         jQuery(".site-header").addClass("sticky_head");
    //     } else {
    //         jQuery(".site-header").removeClass("sticky_head");
    //     }
    // });

    // Sticky Header End

    // Scroll To Top JS

    jQuery('#scrollToTop').click(function() {
        jQuery("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });

    // Scroll To Top JS End

    // Project Tabbing JS
    jQuery("#filters").on('click', function() {
        jQuery("#portfoliolist").removeClass('bydefault_show');
    });

    $(function() {
        var filterList = {
            init: function() {
                // MixItUp plugin
                // http://mixitup.io
                $('#portfoliolist').mixItUp({
                    selectors: {
                        target: '.project-row',
                        filter: '.filter'
                    },
                    layout: {
                        display: "grid",
                    },
                    animation: {
                        effects: "fade",
                        easing: "ease-in-out",
                    },
                    load: {
                        filter: '.all, .interior-design, .architecture-design, .commercial-interior-design'
                    }
                });
            }
        };
        // Run the show!
        filterList.init();
    });

    // Project Tabbing JS End
// jQuery('.carousel').carousel()

});