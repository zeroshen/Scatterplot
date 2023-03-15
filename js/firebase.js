// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.1/firebase-app.js";
import { getAnalytics, logEvent } from "https://www.gstatic.com/firebasejs/9.9.1/firebase-analytics.js";
import { getDatabase, ref, set } from "https://www.gstatic.com/firebasejs/9.9.1/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyA93VIx_fblkljeyoUGbSTs83KNzAsEBzI",
    authDomain: "scatterplots-73801.firebaseapp.com",
    databaseURL: "https://scatterplots-73801-default-rtdb.firebaseio.com",
    projectId: "scatterplots-73801",
    storageBucket: "scatterplots-73801.appspot.com",
    messagingSenderId: "737447391617",
    appId: "1:737447391617:web:4825c74df36da9921db880",
    measurementId: "G-VYX2M9Q84K"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
logEvent(analytics, 'notification_received');

const db = getDatabase(app);

window.db = db;
window.ref = ref;
window.set = set;