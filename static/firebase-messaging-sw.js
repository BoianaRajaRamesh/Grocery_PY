importScripts('https://www.gstatic.com/firebasejs/10.13.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.13.0/firebase-messaging-compat.js');

firebase.initializeApp({
    apiKey: "AIzaSyCBhC9rsVEAS5Lk8JyiBp0FouhUZYCXeKw",
    authDomain: "myfirstproject88955.firebaseapp.com",
    projectId: "myfirstproject88955",
    storageBucket: "myfirstproject88955.appspot.com",
    messagingSenderId: "1031730182137",
    appId: "1:1031730182137:web:3aebcb05be3b646bbbaf28",
    measurementId: "G-SCR1M6X62K",
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
    console.log('Received background message:', payload);
    // Customize notification here if needed
    const notificationTitle = payload.notification.title;
    const notificationOptions = {
        body: payload.notification.body,
        icon: '/static/firebase-logo.png'  // Replace with your app's icon
    };

    self.registration.showNotification(notificationTitle, notificationOptions);
});