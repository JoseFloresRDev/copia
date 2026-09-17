document.addEventListener("DOMContentLoaded", () => {


    /* =====================================================
       MENÚ MÓVIL
    ====================================================== */

    const menuButton = document.getElementById("menu-button");
    const mobileMenu = document.getElementById("mobile-menu");


    if (menuButton && mobileMenu) {

        menuButton.addEventListener("click", () => {

            mobileMenu.classList.toggle("hidden");

        });

    }


    /* =====================================================
       SLIDER
    ====================================================== */

    const slides = document.querySelectorAll(".hero-slide");
    const dots = document.querySelectorAll(".slider-dot");

    let currentSlide = 0;

    const totalSlides = slides.length;


    function showSlide(index) {

        slides.forEach((slide, i) => {

            if (i === index) {

                slide.classList.remove("opacity-0");

                slide.classList.add("opacity-100");

            } else {

                slide.classList.remove("opacity-100");

                slide.classList.add("opacity-0");

            }

        });


        dots.forEach((dot, i) => {

            if (i === index) {

                dot.classList.remove("bg-white/40");

                dot.classList.add("bg-white");

            } else {

                dot.classList.remove("bg-white");

                dot.classList.add("bg-white/40");

            }

        });

    }


    /* =====================================================
       CAMBIO AUTOMÁTICO
    ====================================================== */

    if (totalSlides > 1) {

        setInterval(() => {

            currentSlide++;

            if (currentSlide >= totalSlides) {

                currentSlide = 0;

            }

            showSlide(currentSlide);

        }, 5000);

    }


    /* =====================================================
       BOTONES DEL SLIDER
    ====================================================== */

    dots.forEach((dot) => {

        dot.addEventListener("click", () => {

            currentSlide = Number(
                dot.dataset.slide
            );

            showSlide(currentSlide);

        });

    });

});