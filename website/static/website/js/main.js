(function () {
  document.documentElement.classList.remove('no-js');

  // Mobile menu toggle
  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('navMenu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        menu.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
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

  // Reveal-on-scroll animation
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('visible'); });
  }

  // Animated counters
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
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
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { runCounter(e.target); co.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { co.observe(el); });
  }

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
