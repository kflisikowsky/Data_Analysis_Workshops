(function () {

  function enhanceSlideOverflow() {
    var maxH = Math.floor(window.innerHeight * 0.9) + 'px';
    var slides = document.querySelectorAll('.reveal .slides section.present, .reveal .slides section.present section');
    slides.forEach(function (slide) {
      if (slide.querySelector('iframe[src*="youtube.com"], iframe[src*="youtube-nocookie.com"]')) {
        slide.style.maxHeight = 'none';
        slide.style.overflowY = 'visible';
        slide.style.overflowX = 'visible';
        return;
      }
      slide.style.maxHeight = maxH;
      slide.style.overflowY = 'auto';
      slide.style.overflowX = 'hidden';
    });
  }

  function configureReveal() {
    if (!window.Reveal || typeof window.Reveal.configure !== 'function') {
      return;
    }

    Reveal.configure({
      controls: true,
      progress: true,
      history: true,
      hash: true,
      overview: true,
      center: false,
      keyboard: true,
      touch: true,
      slideNumber: 'c/t'
    });
  }

  function boot() {
    if (!window.Reveal) {
      setTimeout(boot, 120);
      return;
    }

    configureReveal();

    var onSlideChange = function () {
      enhanceSlideOverflow();
    };

    onSlideChange();
    if (typeof Reveal.on === 'function') {
      Reveal.on('ready', onSlideChange);
      Reveal.on('slidechanged', onSlideChange);
    }
    window.addEventListener('resize', enhanceSlideOverflow);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
