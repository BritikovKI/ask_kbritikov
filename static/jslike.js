

function like(user, qID, positive) {
            $.ajaxSetup({
           beforeSend: function(xhr, settings){
                xhr.setRequestHeader( "X-CSRFToken", getCookie('csrftoken') )
           }
        });
        // like
        if (positive) {
            $.ajax({
                url : "like",
                type : "POST",
                data : { user: user, question: qID, positive: positive },
                success : function(json) {
                    console.log('Positive Success')
                    var span = document.getElementById('rate'+qID)
                    console.log(json.total_likes)
                    span.innerText =  json.total_likes
                    var button=document.getElementById('like'+qID)
                    button.isDisabled = true
                },

                error : function (json) {
                    console.log(json.ErrorMSG)
                }
            });
        }
        //dislike
        else {
            $.ajax({
                url: "like",
                type: "POST",
                data: { user: user, question: qID, positive: positive },
                success: function (json) {
                    console.log('Negative Success')
                    span = document.getElementById('rate'+qID)
                    button=document.getElementById('dislike'+qID)
                    span.innerText =  json.total_likes
                     button.isDisabled = true
                },

                error: function (json) {
                    console.log(json.ErrorMSG)
                }
            })
        }
};


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

