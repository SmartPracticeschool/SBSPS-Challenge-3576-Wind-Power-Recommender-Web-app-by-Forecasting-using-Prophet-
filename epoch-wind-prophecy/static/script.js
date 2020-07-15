const memuIcon = document.querySelector('.hamburger-menu');
const navbar = document.querySelector('.navbar');

memuIcon.addEventListener('click', () => {
    navbar.classList.toggle('change');
})