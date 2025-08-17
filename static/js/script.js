document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('sentiment-form');
    const textarea = document.getElementById('feedback-text');
    
    // Auto-resize textarea
    textarea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });
    
    // AJAX form submission (optional)
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        const text = formData.get('feedback-text').trim();
        
        if (!text) return;
        
        // Show loading state
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
        submitBtn.disabled = true;
        
        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }
            
            // For a SPA approach, you would update the DOM here
            // Since we're using server-side rendering, we'll just submit the form normally
            form.submit();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred during analysis');
        })
        .finally(() => {
            submitBtn.innerHTML = originalBtnText;
            submitBtn.disabled = false;
        });
    });
});
