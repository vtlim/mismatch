function validateForm() {
    var errs = [];

    var lhs_value = document.forms["myform"]["text_lhs"].value;
    var rhs_value = document.forms["myform"]["text_rhs"].value;

    if ((lhs_value == "") || (rhs_value == "")) {
        errs.push(suffix);
    }
    return errs;
}

function submitForm() {
    var errors = validateForm();
    if (errors.length == 0) {
        console.log("VALIDATION SUCCESS");
        alert('pause');
        document.getElementById("myform").submit();
    } else {
        console.log("VALIDATION ERROR(S): ", errors);
    }
}
