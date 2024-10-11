document.addEventListener("DOMContentLoaded", function() {
    // Target the login button and add an event listener to show the popup
    document.querySelector(".btn-primary").addEventListener("click", function() {
        document.querySelector(".popup").classList.add("active");
    });

    // Target the close button inside the popup and add an event listener to hide the popup
    document.querySelector(".popup .close-btn").addEventListener("click", function() {
        document.querySelector(".popup").classList.remove("active");
    });
});