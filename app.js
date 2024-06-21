document.addEventListener('DOMContentLoaded', function () {
    const oilPump = document.getElementById('oil-pump');
    const energyFill = document.getElementById('energy-fill');
    const energyText = document.getElementById('energy-text');
    const scoreElement = document.getElementById('score');
    const mineButton = document.getElementById('mine-button');
    const storeButton = document.getElementById('store-button');
    const refsButton = document.getElementById('refs-button');
    const earnButton = document.getElementById('earn-button');
    const mainPage = document.getElementById('main-page');
    const storePage = document.getElementById('store-page');
    const otherPages = document.getElementById('other-pages');
    const buyPassive = document.getElementById('buy-passive');
    const buyProfit = document.getElementById('buy-profit');

    let energy = 100;
    let score = 0;
    let profitPerClick = 1;
    let passiveIncome = false;

    function updateEnergy() {
        energyFill.style.width = `${energy}%`;
        energyText.textContent = `Energy: ${energy}/100`;
    }

    function showPage(page) {
        mainPage.classList.add('hidden');
        storePage.classList.add('hidden');
        otherPages.classList.add('hidden');
        page.classList.remove('hidden');
    }

    mineButton.addEventListener('click', () => showPage(mainPage));
    storeButton.addEventListener('click', () => showPage(storePage));
    refsButton.addEventListener('click', () => showPage(otherPages));
    earnButton.addEventListener('click', () => showPage(otherPages));

    oilPump.addEventListener('click', function (event) {
        if (energy > 0) {
            score += profitPerClick;
            scoreElement.textContent = score;
            energy--;
            if (energy < 0) {
                energy = 0;
            }
            updateEnergy();

            const rect = oilPump.getBoundingClientRect();
            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;

            const numberPopup = document.createElement('div');
            numberPopup.textContent = `+${profitPerClick}`;
            numberPopup.className = 'number-popup';
            numberPopup.style.left = `${x}px`;
            numberPopup.style.top = `${y}px`;

            oilPump.parentElement.appendChild(numberPopup);
            setTimeout(() => numberPopup.remove(), 1000);

            oilPump.style.transform = 'scale(1.03)';
            setTimeout(() => oilPump.style.transform = 'scale(1)', 100);
        }
    });

    setInterval(() => {
        if (energy < 100) {
            energy++;
            updateEnergy();
        }
        if (passiveIncome) {
            score++;
            scoreElement.textContent = score;
        }
    }, 1000);

    buyPassive.addEventListener('click', () => {
        if (score >= 1000) {
            score -= 1000;
            scoreElement.textContent = score;
            passiveIncome = true;
            buyPassive.disabled = true;
        }
    });

    buyProfit.addEventListener('click', () => {
        if (score >= 2000) {
            score -= 2000;
            scoreElement.textContent = score;
            profitPerClick++;
        }
    });
});


