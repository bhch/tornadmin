function toggleSideNav() {
    $nav = $('#sideNav');
    if ($nav.hasClass('open')) {
        $nav.removeClass('open');
        $('body').removeClass('nav-open');
    } else {
        $nav.addClass('open');
        $('body').addClass('nav-open');
    }
}

$('#sideNavToggler').on('click', function(e) {
    toggleSideNav();
});

$('#navOverlay').on('click', function(e) {
    toggleSideNav();
});

$('#list_check_all').on('change', function(e) {
    $('.list-check').prop('checked', this.checked).trigger('change');
});

$('.list-check').on('change', function(e) {
    var $row = $(this).parent().parent().parent();

    if (this.checked) {
        $row.addClass('table-active');
    } else {
        var $checkAll = $('#list_check_all');
        if ($checkAll.prop('checked'))
            $checkAll.prop('checked', false);
        
        $row.removeClass('table-active');
    }
});
