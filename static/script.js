$(document).ready(function(){

    $('#menu').click(function(){
        $(this).toggleClass('fa-times');
        $('.navbar').toggleClass('navbar-toggle');
       
    });
    $(window).on('load scroll',function(){
        $('#menu').removeClass('fa-times');
        $('.navbar').removeClass('navbar-toggle');
    });

    

    if($(window).scrollTop() > 0){
        $('header').addClass('sticky');
    }
    else{
        $('header').removeClass('sticky');
    }
   
});