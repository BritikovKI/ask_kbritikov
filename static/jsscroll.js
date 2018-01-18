
// var infinite = new Waypoint.Infinite({
//       element: $('.infinite-container')[0],
//       onBeforePageLoad: function () {
//         $('.loading').show();function scr(page) {
    $.ajaxSetup({
           beforeSend: function(xhr, settings){
                xhr.setRequestHeader( "X-CSRFToken", getCookie('csrftoken') )
           }
        });
    console.log("is here")
       $.ajax({
            type: 'GET',
            url: "scroll", //Ссылка на вьюху
            data:{'page':page},//Здесь можно передать данные в GET запросе, например сколько значений получить
            success: function(jso) {
                console.log("success")
                var div=document.getElementById("cont")
//hello
                div.innerHTML+=jso
                var button=document.getElementById('btn'+page)
                button.parentNode.removeChild(button)
                // Ответ приходит в переменную data. Её и рендерим на страницу
            },
            error:function () {
                console.log("error")
            }
        });

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
//       },
//       onAfterPageLoad: function ($items) {
//         $('.loading').hide();
//       }
//     });
