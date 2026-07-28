// ---------------- Mobile Menu Logic (smooth slide) ----------------
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu   = document.getElementById('mobile-menu');
    const menuIcon     = document.getElementById('menu-icon');
    const mobileOverlay = document.getElementById('mobile-menu-overlay');
    let mobileOpen = false;

    function toggleMenu() {
      mobileOpen = !mobileOpen;
      if (mobileOpen) {
        mobileOverlay.classList.remove('hidden');
        requestAnimationFrame(() => {
          mobileOverlay.classList.remove('opacity-0');
          mobileMenu.classList.remove('translate-x-full');
        });
        menuIcon.style.transform = 'rotate(90deg)';
        setTimeout(() => {
          menuIcon.className = 'fa-solid fa-xmark text-2xl transition-transform duration-300 text-sultanGreen';
          menuIcon.style.transform = 'rotate(0deg)';
        }, 150);
      } else {
        mobileOverlay.classList.add('opacity-0');
        mobileMenu.classList.add('translate-x-full');
        menuIcon.style.transform = 'rotate(-90deg)';
        setTimeout(() => {
          menuIcon.className = 'fa-solid fa-bars text-2xl transition-transform duration-300';
          menuIcon.style.transform = 'rotate(0deg)';
        }, 150);
        setTimeout(() => {
          mobileOverlay.classList.add('hidden');
        }, 300);
      }
    }

    mobileMenuBtn.addEventListener('click', toggleMenu);
    if(mobileOverlay) mobileOverlay.addEventListener('click', toggleMenu);

    // Close mobile menu on nav link click
    document.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', () => {
        if(mobileOpen) toggleMenu();
      });
    });

    // ---------------- Sticky Header on scroll ----------------
    const header = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('py-1', 'shadow-md');
        header.classList.remove('shadow-soft');
      } else {
        header.classList.remove('py-1', 'shadow-md');
        header.classList.add('shadow-soft');
      }
    }, { passive: true });

    // ---------------- Active Nav Highlighter ----------------
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        if (pageYOffset >= section.offsetTop - 130) {
          current = section.getAttribute('id');
        }
      });
      navLinks.forEach(link => {
        link.classList.remove('active-nav');
        if (link.getAttribute('href') === `#${current}`) {
          link.classList.add('active-nav');
        }
      });
    }, { passive: true });

    // ---------------- Scroll Reveal (IntersectionObserver) ----------------
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
