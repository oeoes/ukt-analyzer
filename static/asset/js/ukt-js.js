var main = function () {


    $('.btn-info').hide();
    $('.btn-info').addClass('animated fadeInUp')
    $('.check').addClass('animated heartBeat')

    $('.wrapper').on('click', event => {
        /* ini untuk ganti background kalau di pilih */
        // ganti ke semula
        $(event.currentTarget).parent().parent().children().find('.sel-active').removeClass('sel-active')
        // ganti background objek yg diseleksi
        $(event.currentTarget).children().addClass('sel-active').fadeIn();
        // console.log($("input[name='q1']:checked").val());

        // menampilkan next button
        $(event.currentTarget).closest('.col-md-10').children().show()
    });

    // Untuk tombol next
    $('.btn-info').on('click', event => {

        $(event.currentTarget).parent().next().removeClass('card-hide')

    }).on('click', event => {

        $('.progress').children().height('+=0').animate({
            height: '+=10%'
        }, 1000)

        $(event.currentTarget).fadeOut('slow')

        // scroll ke bawah saat diklik
        $('html, body').animate({
            scrollTop: $(document).height()
        }, 1000);
    })

    $('.wrapper').on('mouseenter', event => {
        $(event.currentTarget).children().addClass('sel-hover')
    }).on('mouseleave', event => {
        $(event.currentTarget).children().removeClass('sel-hover')
    })


}

$(document).ready(main)