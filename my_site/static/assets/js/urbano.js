$(function() {
    jQuery( "#startdate" ).datepicker({
        dateFormat: 'yy-mm-dd' ,
        defaultDate: "-d",
        changeMonth: true,
        numberOfMonths: 2,
        maxDate: 0,
        onClose: function( selectedDate ) {
            jQuery( "#to" ).datepicker( "option", "minDate", selectedDate );
        }
    });
});