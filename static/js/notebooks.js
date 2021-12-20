$(function () {
  $(".publish").click(function () {
    $("input[name='status']").val("P");
    $("#notebook-form").submit();
  });

  $(".update").click(function () {
    $("input[name='status']").val("P");
    //$("input[name='edited']").prop("checked");
    $("input[name='edited']").val("True");
    $("#notebook-form").submit();
  });

  $(".draft").click(function () {
    $("input[name='status']").val("D");
    $("#notebook-form").submit();
  });
});
