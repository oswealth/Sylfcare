 // Open the consultation form when the button is clicked
 document.getElementById("open-consultation-form").addEventListener("click", function() {
    // Hide the "Book Now!!!" button
    document.getElementById("open-consultation-form").style.display = "none";
    // Display the consultation form
    document.getElementById("consultation-popup").style.display = "block";
  });

  // Handle form submission
  document.getElementById("bookingForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    // Get selected therapy and age
    var therapy = document.getElementById("therapy").value;
    var age = parseInt(document.getElementById("age").value);

    // Validate age for Teen/Youth Therapy
    if (therapy === "teen" && (age < 5 || age > 18)) {
      alert("Child/Teen Therapy only accepts ages from 5 to 18.");
    } else {
      // You can add form submission logic here, like sending data to a server
      // For now, let's just display a success message
      alert("Consultation booked successfully. Please check your email for further details and instructions.");
      // Clear the form fields
      document.getElementById("bookingForm").reset();
      // Hide the consultation form
      document.getElementById("consultation-popup").style.display = "none";
      // Redirect to the services page
      window.location.href = "services.html";
    }
  });