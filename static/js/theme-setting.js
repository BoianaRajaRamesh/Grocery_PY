(function ($) {
    "use strict";

    /*========================
     Dark local storage setting js
    ==========================*/
    $('#darkButton').change(function () {
        if ($(this).is(":checked")) {
            $('body').addClass('dark');
            $("#change-link").attr("href", darkCssPath);
            localStorage.setItem('body', 'dark');
            localStorage.setItem('layoutcss', darkCssPath);
        } else {
            $('body').removeClass('dark');
            $("#change-link").attr("href", defaultCssPath);
            localStorage.setItem('body', '');
            localStorage.setItem('layoutcss', defaultCssPath);
        }
    });

    $("body").attr("class", localStorage.getItem('body'));
    $("#change-link").attr("href", localStorage.getItem('layoutcss') ? localStorage.getItem('layoutcss') : defaultCssPath);
    localStorage.getItem('body') ? $('#darkButton').attr('checked', true) : '';


    /*========================
     RTL local storage setting js
    ==========================*/
    $('#rtlButton').change(function () {
        if ($(this).is(":checked")) {
            $("html").attr("dir", "rtl");
            $("#rtl-link").attr("href", rtlCssPath);
            localStorage.setItem('rtlcss', rtlCssPath);
            localStorage.setItem('dir', 'rtl');
        } else {
            $("html").attr("dir", '');
            $("#rtl-link").attr("href", defaultRtlCssPath);
            localStorage.setItem('rtlcss', defaultRtlCssPath);
            localStorage.setItem('dir', '');
        }
    });

    $("html").attr("dir", localStorage.getItem('dir'));
    $("#rtl-link").attr("href", localStorage.getItem('rtlcss') ? localStorage.getItem('rtlcss') : defaultRtlCssPath);
    localStorage.getItem('dir') ? $('#rtlButton').attr('checked', true) : '';
})(jQuery);
