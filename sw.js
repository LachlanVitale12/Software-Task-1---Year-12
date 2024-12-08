//cache resources list
const cacheName = "Stat-Tracker-cache-v1"
const assets = [
    '/',
    '/search',
    '/sort',
    '/add',
    '/delete',
    '/update',
    '/index',
    '/static/css/style.css',
    '/static/icons/favicon.png',
    '/static/icons/icon_144x144.png',
    '/static/icons/icon_192x192.png',
    '/static/icons/icon_512x512.png',
    '/static/images/NBA_Image1.webp',
    '/static/images/NBA_Image2.webp',
    '/static/images/NBA_Image3.webp',
    '/static/images/NBA_Image4.webp',
    '/static/images/NBA_Image5.webp',
    '/static/images/NBA_Image6.webp',
    '/static/images/NBA_Image7.webp',
    '/static/images/NBA_Image8.webp',
    '/static/images/NBA_Image9.webp',
    '/static/images/NBA_Image10.webp',
    '/manifest.json',
    '/sw.js',
    '/static/offline.html',
]

//installation event listener
self.addEventListener('install', event =>{
    console.log("[Service Worker] Installing Service Worker and Caching Resources..."); // logs if service worker is being initiallised
    event.waitUntil(
        caches.open(cacheName).then(cache => {
            console.log("[Service Worker] Caching files..."); // logs if files are being cached
            return cache.addAll(assets);
        })
    );
});

//activation event listener
self.addEventListener('activate', event =>{
    console.log("[Service Worker] Activating Service Worker and Cleaning Old Caches..."); // logs if the service worker is activating and old cache is being cleaned
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.map(key =>{
                    if (key !== cacheName){
                        console.log("[Service Worker] Deleting Old Cache...",key); // logs if old cache needs to be deleted
                        return caches.delete(key);
                    }
                })
            );
        })
    );
});

//fetch event listener with offline fallback
self.addEventListener('fetch', event => {
    console.log("[Service Worker] Fetching Resource...",event.request.url); // logs each fetch request
    event.respondWith(
        caches.match(event.request).then(cacheRes => {
            if (cacheRes) {
                console.log("[Service Worker] Found in Cache...", event.request.url); // logs if it was found in cache
            }   else {
                console.log("[Service Worker] Fetching From Network: ", event.request.url); // logs if it is fetching from network
            }
            return cacheRes || fetch(event.request).catch(() => {
                console.log('[Service Worker] Network failed, serving offline fallback'); // logs if the network failed and offline mode needs to be activated
                return caches.match('/static/offline.html'); // serves offline fallback if network fails
            });
        })
        
    );
});