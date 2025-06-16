// script.js
document.addEventListener('DOMContentLoaded', function() {
  const success = {{ success|default:'false'|lower }};
  
  if (success) {
    showSuccessModal();
  }
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function() {
      return true; // Allow form to submit
    });
  }
});

function showSuccessModal() {
  const modal = new bootstrap.Modal(document.getElementById('successModal'));
  modal.show();
  

  history.replaceState({}, document.title, window.location.pathname);
}











