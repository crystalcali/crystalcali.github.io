document.addEventListener('DOMContentLoaded', function () {
    const oilPump = document.getElementById('oil-pump');
    const energyFill = document.getElementById('energy-fill');
    const energyText = document.getElementById('energy-text');
    const scoreElement = document.getElementById('score');
    let energy = 100;
    let score = 0;

    oilPump.addEventListener('click', function (event) {
        score++;
        scoreElement.textContent = score;
        energy--;
        if (energy < 0) {
            energy = 0;
        }
        energyFill.style.width = `${energy}%`;
        energyText.textContent = `${energy}/100`;

        const rect = oilPump.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        const numberPopup = document.createElement('div');
        numberPopup.textContent = '+1';
        numberPopup.className = 'number-popup';
        numberPopup.style.left = `${x}px`;
        numberPopup.style.top = `${y}px`;

        oilPump.parentElement.appendChild(numberPopup);
        setTimeout(() => numberPopup.remove(), 1000);

        oilPump.style.transform = 'scale(1.03)';
        setTimeout(() => oilPump.style.transform = 'scale(1)', 100);
    });

    setInterval(() => {
        if (energy < 100) {
            energy++;
            energyFill.style.width = `${energy}%`;
            energyText.textContent = `${energy}/100`;
        }
    }, 1000);
});
