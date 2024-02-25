document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector("header");
    const progressBar = document.getElementById("progress-bar");
    const overlayImage = document.getElementById("overlay-image");
    const blackBlock = document.getElementById("black-block");

    window.addEventListener("scroll", function () {
        const scrolled = window.scrollY;
        const totalHeight = document.body.scrollHeight - window.innerHeight;
        const progress = (scrolled / totalHeight) * 100;

        progressBar.style.width = progress + "%";
        overlayImage.style.width = progress + "%";

        // Show black block with text when the image is covered
        if (scrolled > 40) {
            blackBlock.classList.add("show");
        } else {
            blackBlock.classList.remove("show");
        }

        if (window.scrollY > 50) {
            header.classList.add("shrink");
        } else {
            header.classList.remove("shrink");
        }
    });
});

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}