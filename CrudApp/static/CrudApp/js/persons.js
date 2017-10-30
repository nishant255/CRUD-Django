$(".get").hide();
$(".post").hide();
$(".put").hide();
$(".delete").hide();

$(".js-get").on('click', function () {
    $(".get").show();
    $(".post").hide();
    $(".put").hide();
    $(".delete").hide();
});
$(".js-post").on('click', function () {
    $(".get").hide();
    $(".post").show();
    $(".put").hide();
    $(".delete").hide();
});
$(".js-put").on('click', function () {
    $(".get").hide();
    $(".post").hide();
    $(".put").show();
    $(".delete").hide();
});
$(".js-delete").on('click', function () {
    $(".get").hide();
    $(".post").hide();
    $(".put").hide();
    $(".delete").show();
});

$(document).on("submit", "#get-form", function () {
    var form = $(this);
    var data = form.serializeArray();
    var url = /person/ + data[0].value;
    $.ajax({
        url: url,
        type: 'get',
        dataType: 'json',
        success: function (data) {
            var person = data[0].fields;
            $('.res-get-userName').val(person.userName);
            $('.res-get-firstName').val(person.firstName);
            $('.res-get-lastName').val(person.lastName);
            $('.res-get-email').val(person.email);
            return false;
        }
    });
    return false;
});

$(document).on('submit', ".post-form", function () {
    var form = $(this);
    console.log(form.serializeArray());
    $.post("/create/", form.serialize(), function () {
        $(".post-form input").val(" ");
        $('.post-result').append("Successfully created user");
    });
    return false;
});
