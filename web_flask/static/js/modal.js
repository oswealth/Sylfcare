// Open the modal when the button is clicked
document.getElementById("open-consultation-modal").addEventListener("click", function() {
    document.getElementById("consultation-modal").style.display = "block";
  });

  // Close the modal when the close button is clicked
  document.querySelector(".close").addEventListener("click", function() {
    document.getElementById("consultation-modal").style.display = "none";
  });

  // Handle form submission
  document.querySelector("#bookingForm").addEventListener("submit", function(event) {
    event.preventDefault();
    // Validate form fields
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let therapy = document.getElementById("therapy").value;
    let about = document.getElementById("about").value.trim();
    let reason = document.getElementById("reason").value.trim();

    // Simple validation example
    if (name === "" || email === "" || about === "" || reason === "") {
      alert("Please fill in all required fields.");
      return;
    }

    // If all fields are valid, you can proceed with form submission
    // You can submit the form via AJAX or perform any other action here
    // For now, let's show a success message
    alert("Consultation booked successfully. Please check your email for further details and instructions.");

    // Optionally, close the modal after successful submission
    document.getElementById("consultation-modal").style.display = "none";
  });