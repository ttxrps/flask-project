// function toggleMenu(){
//     const navigation = document.querySelector('.navigation');
//     const toggle = document.querySelector('.toggle');
//     navigation.classList.toggle('active');
//     toggle.classList.toggle('active');
// }
window.addEventListener("scroll", function(){
    var nav = document.querySelector("nav");
    nav.classList.toggle("sticky", window.scrollY > 0)
})

var myIndex = 0;
    fetchEPICImage();
    
    function fetchEPICImage() {
        var i;
        var x = document.getElementsByClassName("mySlides");
        for (i = 0; i < x.length; i++) {
            x[i].style.display = "none";  
        }
        myIndex++;
        if (myIndex > x.length) {myIndex = 1}    
        x[myIndex-1].style.display = "block";  
        setTimeout(fetchEPICImage, 5000); // Change image every 2 seconds
    }