$(document).ready(function() {
    $("img").click(function() {

        var temporal = $(this).attr("src");

        $(this).attr("src", $(this).attr("data-alt-src"));
        $(this).attr("data-alt-src", temporal);


    });
});