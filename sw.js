//cache resources list
const cacheName = "Stat-Tracker-cache-v1"
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
    '/models.py',
    '/static/offline.html'
];

//installation event listener
self.addEventListener('install', event => {
    console.log("[Service Worker] Installing Service Worker and Caching Resources...");
    event.waitUntil(
        caches.open(cacheName).then(cache => {
            console.log("[Service Worker] Caching files...");
            return cache.addAll(urlsToCache);
        })
    );
});

//activation event listener
self.addEventListener('activate', event => {
    console.log("[Service Worker] Activating Service Worker and Cleaning Old Caches...");
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.map(key => {
                    if (key !== cacheName) {
                        console.log("[Service Worker] Deleting Old Cache...", key);
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
                console.log("[Service Worker] Found in Cache...", event.request.url);
            }   else {
                console.log("[Service Worker] Fetching From Network: ", event.request.url);
            }
            return cacheRes || fetch(event.request).catch(() => {
                console.log('[Service Worker] Network failed, serving offline fallback');
                return caches.match('/static/offline.html'); // serves offline fallback if network fails
            });
        })
    );
});