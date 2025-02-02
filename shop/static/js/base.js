window.addEventListener('scroll', function(){
    document.getElementById('header_nav').classList.toggle('header_nav_scroll', window.scrollY > 90)
})

$(document).ready(function(){
    $(window).scroll(function(){
        if ($(this).scrollTop() > 500) {
            $('#top_button').fadeIn();
        } else {
            $('#top_button').fadeOut();
        }
    });
    $('#top_button').click(function(){
        $('html, body').animate({scrollTop: 0}, 100);
        return false;
    })
})