function modalop() {

         $('#myModalBox').css('display','block').animate({opacity: 1, top:'30%'},500);
};

function modalc() {
$('#myModalBox')
			.animate({opacity: 0, top: '45%'}, 200,  // плавно меняем прозрачность на 0 и одновременно двигаем окно вверх
				function(){ // после анимации
					$(this).css('display', 'none'); // делаем ему display: none;
				}
			);
}

function sendAns( qID){
     $.ajaxSetup({
           beforeSend: function(xhr, settings){
                xhr.setRequestHeader( "X-CSRFToken", getCookie('csrftoken') )
           }
        });
     $('#myModalBox')
			.animate({opacity: 0, top: '45%'}, 200,  // плавно меняем прозрачность на 0 и одновременно двигаем окно вверх
				function(){ // после анимации
					$(this).css('display', 'none'); // делаем ему display: none;
				}
			);
     var textbox=document.getElementsByName('text')
     console.log( textbox[0].value)
     $.ajax({
                url : "question?question="+qID,
                type : "POST",
                data : {  text: textbox[0].value},
                success : function(json) {
                    console.log('Positive Success')
                    return location.href='question?question='+qID
                },

                error : function (json) {
                    console.log(json.ErrorMSG)
                }
            });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
