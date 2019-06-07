$(document).ready(function() {
    $(".dropdown-trigger").dropdown();
}

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})