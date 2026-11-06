(function () {
  document.documentElement.classList.remove('no-js');

  // Mobile / tablet menu drawer
  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('navMenu');
  var closeBtn = document.getElementById('navClose');
  var backdrop = document.getElementById('navBackdrop');
  function setMenu(open) {
    if (!menu || !toggle) return;
    menu.classList.toggle('open', open);
    document.body.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (backdrop) backdrop.hidden = !open;
    if (open) {
      var first = menu.querySelector('.nav-link');
      if (first) setTimeout(function () { first.focus(); }, 50);
    }
  }
  if (toggle && menu) {
    toggle.addEventListener('click', function () { setMenu(!menu.classList.contains('open')); });
    if (closeBtn) closeBtn.addEventListener('click', function () { setMenu(false); toggle.focus(); });
    if (backdrop) backdrop.addEventListener('click', function () { setMenu(false); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) { setMenu(false); toggle.focus(); }
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1100 && menu.classList.contains('open')) setMenu(false);
    });
  }

  // Navbar shadow, scroll progress bar, back-to-top button
  var navbar = document.getElementById('navbar');
  var progress = document.getElementById('scrollProgress');
  var toTop = document.getElementById('toTop');
  function onScroll() {
    var y = window.scrollY;
    if (navbar) navbar.classList.toggle('scrolled', y > 10);
    if (progress) {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.width = (max > 0 ? (y / max) * 100 : 0) + '%';
    }
    if (toTop) toTop.classList.toggle('show', y > 600);
  }
  if (toTop) toTop.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  var root = document.documentElement;
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Image placeholders: shimmer on the frame until the photo arrives, then fade it in
  document.querySelectorAll('main img').forEach(function (img) {
    var frame = img.parentElement;
    if (img.complete && img.naturalWidth) { img.classList.add('img-loaded'); return; }
    img.classList.add('img-wait');
    if (frame) frame.classList.add('img-loading');
    function done() {
      img.classList.add('img-loaded');
      if (frame) frame.classList.remove('img-loading');
    }
    img.addEventListener('load', done, { once: true });
    img.addEventListener('error', done, { once: true });
  });

  // Section entrances: pick a direction per element and stagger siblings
  var items = document.querySelectorAll('.reveal');
  items.forEach(function (el) {
    if (el.matches('.ind-card, .ff-item, .credit-item, .gallery-item, .fact, .stat, .core-card')) el.classList.add('reveal-zoom');
    else if (el.matches('.ai-visual, .founder-card')) el.classList.add('reveal-left');
    else if (el.matches('.hero-visual')) el.classList.add('reveal-right');
    var sibs = el.parentElement ? Array.prototype.filter.call(el.parentElement.children, function (c) {
      return c.classList.contains('reveal');
    }) : [];
    var i = sibs.indexOf(el);
    if (sibs.length > 1 && i > 0) el.style.transitionDelay = Math.min(i, 7) * 80 + 'ms';
  });

  function show(el) {
    el.classList.add('visible', 'in');
    // Once the entrance has played, drop the reveal classes so the element's own
    // hover transitions (card lifts, zooms) work at normal speed again.
    var delay = parseFloat(el.style.transitionDelay) || 0;
    setTimeout(function () {
      el.classList.remove('reveal', 'reveal-zoom', 'reveal-left', 'reveal-right', 'visible');
      el.style.transitionDelay = '';
    }, 1000 + delay);
  }
  function startReveals() {
    if ('IntersectionObserver' in window && !reduceMotion) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) { show(entry.target); io.unobserve(entry.target); }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      items.forEach(function (el) { io.observe(el); });
    } else {
      items.forEach(function (el) { el.classList.add('visible', 'in'); });
    }
  }

  // Animated counters
  var reduce = reduceMotion;
  function runCounter(el) {
    var target = parseInt(el.getAttribute('data-count'), 10) || 0;
    var suffix = el.getAttribute('data-suffix') || '';
    if (reduce || target < 2) { el.textContent = target + suffix; return; }
    var start = null, dur = 1400;
    function tick(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3))) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  var counters = document.querySelectorAll('[data-count]');
  function startCounters() {
    if ('IntersectionObserver' in window) {
      var co = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { runCounter(e.target); co.unobserve(e.target); }
        });
      }, { threshold: 0.6 });
      counters.forEach(function (el) { co.observe(el); });
    }
  }

  // Brand preloader (first page of a visit). Entrance animations start once it lifts,
  // so the hero and counters animate in view instead of behind the curtain.
  var preloader = document.getElementById('preloader');
  var started = false;
  function startAnimations() {
    if (started) return; started = true;
    root.classList.add('page-ready');
    startReveals(); startCounters();
  }
  if (preloader && root.classList.contains('pl-active')) {
    var t0 = (window.performance && performance.now) ? performance.now() : 0;
    var lifted = false;
    var lift = function () {
      if (lifted) return; lifted = true;
      try { sessionStorage.setItem('rpSeen', '1'); } catch (e) {}
      var wait = Math.max(0, 1100 - ((window.performance && performance.now) ? performance.now() - t0 : 0));
      setTimeout(function () {
        preloader.classList.add('pl-done');
        root.classList.remove('pl-active');
        setTimeout(startAnimations, 250);
        setTimeout(function () { if (preloader.parentNode) preloader.parentNode.removeChild(preloader); }, 1200);
      }, wait);
    };
    if (document.readyState === 'complete') lift();
    else window.addEventListener('load', lift);
    setTimeout(lift, 3500); // never hold the page longer than this on slow connections
  } else {
    if (preloader && preloader.parentNode) preloader.parentNode.removeChild(preloader);
    startAnimations();
  }

  // Thin loading bar when moving to another page of the site
  var navBar = document.getElementById('navProgress');
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || !navBar || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    if (a.target === '_blank' || a.hasAttribute('download')) return;
    var url = new URL(a.href, location.href);
    if (url.origin !== location.origin || (url.pathname === location.pathname && url.hash)) return;
    if (!/^https?:$/.test(url.protocol)) return;
    navBar.classList.add('loading');
  });
  window.addEventListener('pageshow', function () { if (navBar) navBar.classList.remove('loading'); });

  // Flour yield calculator
  var calc = document.getElementById('calc');
  if (calc) {
    var COLORS = { maida: '#ffffff', suji: '#ffd166', atta: '#ff9aa8', bran: '#c98b4a', loss: '#5a1a24' };
    var FLOUR = ['maida', 'suji', 'atta'];
    var tpdEl = document.getElementById('calcTpd');
    var daysEl = document.getElementById('calcDays');
    var sliders = calc.querySelectorAll('input[type="range"]');
    var defaults = {};
    sliders.forEach(function (s) { defaults[s.id] = s.value; });

    function fmt(n) {
      return n.toLocaleString('en-IN', { maximumFractionDigits: n < 100 ? 1 : 0 }) + ' t';
    }
    function update() {
      var tpd = Math.max(parseFloat(tpdEl.value) || 0, 0);
      var days = Math.max(parseFloat(daysEl.value) || 0, 0);
      var total = 0, rows = '', bars = '', flour = 0;
      sliders.forEach(function (s) {
        var pct = parseFloat(s.value);
        total += pct;
        s.nextElementSibling.textContent = pct + '%';
      });
      sliders.forEach(function (s) {
        var key = s.getAttribute('data-key');
        var pct = parseFloat(s.value);
        var day = tpd * pct / 100;
        if (FLOUR.indexOf(key) > -1) flour += day;
        rows += '<tr><td><span class="sw" style="background:' + COLORS[key] + '"></span>' + s.getAttribute('data-label') +
                ' <small>(' + pct + '%)</small></td><td>' + fmt(day) + '</td><td>' + fmt(day * days) + '</td></tr>';
        bars += '<span style="width:' + (total > 0 ? pct / total * 100 : 0) + '%;background:' + COLORS[key] + '" title="' + s.getAttribute('data-label') + '"></span>';
      });
      document.getElementById('calcBody').innerHTML = rows;
      document.getElementById('calcBars').innerHTML = bars;
      document.getElementById('calcFlour').textContent = fmt(flour);
      var t = document.getElementById('calcTotal');
      var rounded = Math.round(total * 10) / 10;
      if (Math.abs(rounded - 100) < 0.05) {
        t.textContent = 'Split adds up to 100%. Flour extraction: ' + (tpd ? Math.round(flour / tpd * 1000) / 10 : 0) + '%';
        t.classList.remove('warn');
      } else {
        t.textContent = 'Split adds up to ' + rounded + '%. Adjust the sliders to total 100%.';
        t.classList.add('warn');
      }
    }
    calc.addEventListener('input', update);
    document.getElementById('calcReset').addEventListener('click', function () {
      sliders.forEach(function (s) { s.value = defaults[s.id]; });
      tpdEl.value = 150; daysEl.value = 26;
      update();
    });
    update();
  }

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
