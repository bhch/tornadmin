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
