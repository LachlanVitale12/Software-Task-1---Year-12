//cache resources list
self.CACHE_NAME = "wave-solution-cache-v1"
const urlsToCache = [
    '/',
    '/search',
    '/sort',
    '/index',
    '/static/css/style.css',
    '/static/icons/favicon.png',
    '/static/icons/icon_144x144.png',
    '/static/icons/icon_192x192.png',
    '/static/icons/icon_512x512.png',
    '/static/images/NBA_Image.webp',
    '/manifest.json',
    '/sw.js',
    '/models.py'
];

//installation event listener
self.addEventListener('install', function(event) {
    console.log("[Service Worker] Installing Service Worker and Caching Resources...");
    event.waitUntil(
        caches.open(self.CACHE_NAME)
            .then(function(cache) {
                console.log("[Service Worker] Caching files...");
                return cache.addAll(urlsToCache);
            })
    );
});

//activation event listener
self.addEventListener('activate', function(event) {
    console.log("[Service Worker] Activating Service Worker and Cleaning Old Caches...");
    event.waitUntil(
        caches.keys().then(function(cacheNames){
            return Promise.all(
                cacheNames.map(function(cache){
                    if (cache !== self.CACHE_NAME){
                        console.log("[Service Worker] Deleting Old Cache...",cache);
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
});

//fetch event listener
self.addEventListener('fetch', function(event) {
    console.log("[Service Worker] Fetching Resource...",event.request.url);
    event.respondWith(
        caches.match(event.request)
            .then(function(response){
                if (response){
                    console.log("[Service Worker] Found in Cache...", event.request.url);
                    return response;
                }
                console.log("[Service Worker] Fetching From Network: ", event.request.url);
                return fetch(event.request);
            })
    );
});