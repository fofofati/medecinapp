document.addEventListener("DOMContentLoaded", function () {
    // Liste des images à afficher en arrière-plan
    const images = [
        "/static/images/bg1.jpg",
        "/static/images/bg2.jpg",
        "/static/images/bg3.jpg",
        "/static/images/bg4.jpg"
    ];

    let index = 0;
    const background = document.getElementById("dynamic-background");

    function changeBackground() {
        background.style.backgroundImage = `url('${images[index]}')`;
        index = (index + 1) % images.length;
    }

    // Changer l'image toutes les 5 secondes
    changeBackground();
    setInterval(changeBackground, 5000);
});
