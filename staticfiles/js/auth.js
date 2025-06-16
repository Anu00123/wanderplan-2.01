
 // Toggle between login and signup forms
        document.querySelectorAll('.auth-tab').forEach(tab => {
            tab.addEventListener('click', function() {
                const tabId = this.getAttribute('data-tab');
                
                // Update active tab
                document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                
                // Update active form
                document.querySelectorAll('.auth-form').forEach(form => form.classList.remove('active'));
                document.getElementById(`${tabId}-form`).classList.add('active');
                
                // Update header text
                if (tabId === 'login') {
                    document.getElementById('auth-title').textContent = 'Welcome Back!';
                    document.getElementById('auth-subtitle').textContent = 'Please login to your account';
                    document.getElementById('switch-message').innerHTML = 'Don\'t have an account? <a href="#" id="switch-link">Sign up</a>';
                } else {
                    document.getElementById('auth-title').textContent = 'Create Account';
                    document.getElementById('auth-subtitle').textContent = 'Join our community today';
                    document.getElementById('switch-message').innerHTML = 'Already have an account? <a href="#" id="switch-link">Login</a>';
                }
                
                // Update switch link event
                setupSwitchLink();
            });
        });
        
        // Password toggle functionality
        document.querySelectorAll('.password-toggle').forEach(toggle => {
            toggle.addEventListener('click', function() {
                const targetId = this.getAttribute('data-target');
                const passwordInput = document.getElementById(targetId);
                const icon = this.querySelector('i');
                
                if (passwordInput.type === 'password') {
                    passwordInput.type = 'text';
                    icon.classList.remove('fa-eye');
                    icon.classList.add('fa-eye-slash');
                } else {
                    passwordInput.type = 'password';
                    icon.classList.remove('fa-eye-slash');
                    icon.classList.add('fa-eye');
                }
            });
        });
        
        // Switch between forms via footer link
        function setupSwitchLink() {
            const switchLink = document.getElementById('switch-link');
            if (switchLink) {
                switchLink.addEventListener('click', function(e) {
                    e.preventDefault();
                    const activeTab = document.querySelector('.auth-tab:not(.active)');
                    activeTab.click();
                });
            }
        }
        
        // Initialize
        setupSwitchLink();






