/* Manage Class Funtions https://www.sitepoint.com/add-remove-css-class-vanilla-js/ */
function addClass(e, l) {
    elements = document.querySelectorAll(e);
    for (var s = 0; s < elements.length; s++) elements[s].classList.add(l);
}
function removeClass(e, l) {
    elements = document.querySelectorAll(e);
    for (var s = 0; s < elements.length; s++) elements[s].classList.remove(l);
}


$(document).ready(function () {
    //change selectboxes to selectize mode to be searchable
       $("select").select2();
    });
