console.log('Website Loaded');

window.addEventListener('scroll', function () {

    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {

        const position = card.getBoundingClientRect().top;

        if (position < window.innerHeight - 100) {
            card.style.transform = 'translateY(0px)';
            card.style.opacity = '1';
        }

    });

});