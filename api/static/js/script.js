(function () {
  var root = document.documentElement;
  var themeToggle = document.getElementById('theme-toggle');
  var menuToggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('nav-menu');

  /* ---- Theme ---- */
  function applyTheme(theme, save) {
    root.setAttribute('data-theme', theme);
    if (themeToggle) themeToggle.setAttribute('aria-pressed', String(theme === 'dark'));
    if (save) {
      try { localStorage.setItem('theme', theme); } catch (e) {}
    }
  }

  applyTheme(root.getAttribute('data-theme') || 'light', false);

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      applyTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark', true);
    });
  }

  /* ---- Mobile menu ---- */
  function setMenu(open) {
    if (!menu || !menuToggle) return;
    menu.classList.toggle('active', open);
    menuToggle.setAttribute('aria-expanded', String(open));
    menuToggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  }

  if (menuToggle && menu) {
    menuToggle.addEventListener('click', function () {
      setMenu(!menu.classList.contains('active'));
    });

    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) setMenu(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('active')) {
        setMenu(false);
        menuToggle.focus();
      }
    });

    window.matchMedia('(min-width: 761px)').addEventListener('change', function (e) {
      if (e.matches) setMenu(false);
    });
  }
})();
