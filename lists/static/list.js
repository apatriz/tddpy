jQuery(document).ready(function ($) {
    $("input[name='text']").on('click keypress',  function () {
        $('.has-error').hide();
    });
});


