jQuery(document).ready(function ($) {
    $("input[name='text']").on('keypress click',  function () {
        $('.has-error').hide();
    });
});


