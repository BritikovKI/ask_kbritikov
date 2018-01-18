function validate() {
            $.ajaxSetup({
           beforeSend: function(xhr, settings){
                xhr.setRequestHeader( "X-CSRFToken", getCookie('csrftoken') )
           }
        });
         var login=document.getElementsByName('nickname')
    var pass=document.getElementsByName('password')
        if(!login[0].value)
        {
            alert("Enter login")
        }
        else {
            if (!pass[0].value) {
                alert("Enter password")
            }
            else {
                alert("Success")
                $.ajax({
                url : "auth",
                type : "POST",
                data : { nickname: login[0].value, password: pass[0].value},
                success : function(json) {
                    console.log('Positive Success')
                    return location.href='/'
                    // var span = document.getElementById('rate'+qID)
                    // console.log(json.total_likes)
                    // span.innerText =  json.total_likes
                    // var button=document.getElementById('like'+qID)
                    // button.isDisabled = true
                },

                error : function (json) {
                    console.log(json.ErrorMSG)
                    return location.href='/'
                }
            });
            }
        }
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
