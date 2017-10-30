$("#modal-book").on("submit",'js-person-create-form',function () {
  var form = $(this);

    $.ajax({
      url: form.attr("action"),
      data:form.serialize(),
      type: form.attr("method"),
      dataType: 'json',

      success: function (data) {
          if(data.form_is_valid){
              alert("Person created");
          }
          else{
              $("#modal-book .modal-content").html(data.html_form);
          }

      }
    });
    return false;

});