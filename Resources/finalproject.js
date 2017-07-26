/* var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
*/
/*
function fadeIn(obj) {
    $(obj).fadeIn(3400);

    $(document).ready(() => {
      const commentContent = $('#comment-content');
      $('#comment-form').submit((event) => {
        event.preventDefault();
        $('#no-comments').remove();
        $('#comments')
            .append($('<div/>')
                .append($('<h4>You wrote:</h4>'))
                .append($('<p/>', {text: commentContent.val()})));
        commentContent.val('');
        commentContent.focus();
      });
    });
    */
    $(document).ready(function () {
      $('.mainlogo').hide().fadeIn(2000);});
