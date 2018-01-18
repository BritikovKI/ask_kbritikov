function validate() {
            $.ajaxSetup({
           beforeSend: function(xhr, settings){
                xhr.setRequestHeader( "X-CSRFToken", getCookie('csrftoken') )
           }
        });
         var login=document.getElementById('nickname').value
    var pass=document.getElementById('password').value
        if(!login)
        {
            alert("Enter login")
        }
        else {
            if (!pass) {
                alert("Enter password")
            }
            else {
                alert("Success")
                $.ajax({
                url : "auth",
                type : "POST",
                data : { nickname: login, password: pass},
                success : function(json) {
                    console.log('Positive Success')
                    // var span = document.getElementById('rate'+qID)
                    // console.log(json.total_likes)
                    // span.innerText =  json.total_likes
                    // var button=document.getElementById('like'+qID)
                    // button.isDisabled = true
                },

                error : function (json) {
                    console.log(json.ErrorMSG)
                }
            });
            }
        }
}
