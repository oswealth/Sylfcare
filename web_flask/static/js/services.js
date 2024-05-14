// Wait for the DOM content to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Get all the "Book a Session" buttons
    var bookButtons = document.querySelectorAll(".btn-book");

    // Loop through each button and attach a click event listener
    bookButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            // Prevent the default action of the link (i.e., navigating to the booking.html page)
            event.preventDefault();
            
            // Get the href attribute of the clicked button (which should be the link to the booking form)
            var bookingsFormLink = button.getAttribute("href");

            // Redirect the user to the booking form page
            window.location.href = bookingsFormLink;
        });
    });
});