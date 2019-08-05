// Request animation frame, or just wait a little if no updates.
var scroll = window.requestAnimationFrame ||
function(callback){ window.setTimeout(callback, 2)};

// Get all the product tiles that are intended to transition on scroll. 
var elements = document.querySelectorAll('.scroll'); 

// Function that checks if any items are now in the viewport.
function loop() {
    // Loop for each product tile that we're transitioning.
    Array.prototype.forEach.call(elements, function(element){
        // Is it in the viewport?
        if (inView(element)) {
            // Add the "show" class, which transitions the opacity. 
            element.classList.add('show');
        }
    });

    // Continious loop run on window scroll.
    scroll(loop);
}

// Initial run
loop();

// Check if the product tile is in the viewport
function inView(el) {
    // Get product tile's positioning
    var rect = el.getBoundingClientRect();
    // Is it in view? Check the element top and bottom vs window height. 
    var result = (
        (rect.top <= 0 && rect.bottom >= 0)
        ||
        (rect.bottom >= window.innerHeight && rect.top <= window.innerHeight)
        ||
        (rect.top >= 0 && rect.bottom <= window.innerHeight )
    )
    // True or false.
    return result;
}


// Activate and deactivate the Space Pulse effect on the Hero Banner. This uses jQuery to manipulate the CSS play state on mouseenter and mouseleave. I did this because the effects need to be a lower z-index under the boots, but the :hover doesn't activate with lower z-indicies. 
$(document).ready(function(){
    $("#spacejam").mouseenter(function(){
        $(".pulse").css("animation-play-state", "running");
    });
    $("#spacejam").mouseleave(function(){
        $(".pulse").css("animation-play-state", "paused");
    });
});