document.addEventListener('DOMContentLoaded', function () {
    const startButton = document.getElementById('start-button');
    startButton.addEventListener('click', function () {
        const hour = document.getElementById('hour').value;
        const minute = document.getElementById('minute').value;
        const second = document.getElementById('second').value;

        fetch('/start_notifications', {
            method: 'POST',
            body: new URLSearchParams({ 'hour': hour, 'minute': minute, 'second': second }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        })
            .then(response => response.json())
            .then(data => {
                alert(data.status);
            });
    });
});
