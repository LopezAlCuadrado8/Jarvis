$(document).ready(function () {


    // Display speak message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');
    }

    //Display hood
    eel.expose(Showhood)
    function Showhood(){
        $("#Oval").attr("hidden", false);
        $("#Siriwave").attr("hidden",true);
    }

});

