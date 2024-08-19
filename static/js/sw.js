var cacheName = 'Fastkart';
var filesToCache = [
    // 'static/css/vendors/bootstrap.css',
    // 'static/css/vendors/bootstrap.rtl.css',
    // 'static/css/vendors/slick-theme.css',
    // 'static/css/vendors/slick.css',
    // 'static/css/dark.css',
    // 'static/css/date-picker.css',
    // 'static/css/iconly.css',
    // 'static/css/pricing-slider.css',
    // 'static/css/style.css',
    // 'static/js/date-picker/datepicker.js',
    // 'static/js/date-picker/datepicker.en.js',
    // 'static/js/date-picker/datepicker.custom.js',
    // 'static/js/pricing-slider/pricing-slider-custom.js',
    // 'static/js/bootstrap.bundle.min.js',
    // 'static/js/feather.min.js',
    // 'static/js/here-map-info.js',
    // 'static/js/here-map-route.js',
    // 'static/js/jquery-3.6.0.min.js',
    // 'static/js/jquery-swipe-1.11.3.min.js',
    // 'static/js/jquery.mobile-1.4.5.min.js',
    // 'static/js/lord-icon-2.1.0.js',
    // 'static/js/otp.js',
    // 'static/js/pricing-slider.js',
    // 'static/js/script.js',
    // 'static/js/slick-custom.js',
    // 'static/js/slick.js',
    // 'static/js/slick.min.js',
    'static/js/theme-setting.js'
];


/* Start the service worker and cache all of the app's content */
self.addEventListener('install', function (e) {
    e.waitUntil(
        caches.open(cacheName).then(function (cache) {
            return cache.addAll(filesToCache);
        })
    );
    self.skipWaiting();
});

/* Serve cached content when offline */
self.addEventListener('fetch', function (e) {
    e.respondWith(
        caches.match(e.request).then(function (response) {
            return response || fetch(e.request);
        })
    );
});