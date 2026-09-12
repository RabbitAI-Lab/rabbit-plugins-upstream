
/* CLINICAL ATELIER v3 — app_v3.js (embedded, IIFE, no globals)
   theme toggle · search+marks · scrollspy · quiz engine · fold tools ·
   auto-fold + deep-links · to-top · beforeprint expansion  */
(function () {
  "use strict";
  var doc = document, html = doc.documentElement;

  /* ── theme ─────────────────────────────────────────────────────────── */
  try {
    var saved = localStorage.getItem("sg-theme");
    var dark = saved ? saved === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
    html.setAttribute("data-theme", dark ? "dark" : "light");
  } catch (e) { html.setAttribute("data-theme", "light"); }
  var tt = doc.getElementById("themeToggle");
  if (tt) tt.addEventListener("click", function () {
    var next = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
    html.setAttribute("data-theme", next);
    try { localStorage.setItem("sg-theme", next); } catch (e) {}
  });

  /* ── reduced motion ────────────────────────────────────────────────── */
  try {
    var rm = window.matchMedia("(prefers-reduced-motion: reduce)");
    function setRm(m) { html.setAttribute("data-reduced", m.matches ? "1" : "0"); }
    setRm(rm); rm.addEventListener ? rm.addEventListener("change", setRm) : rm.addListener(setRm);
  } catch (e) {}

  /* ── search normalization (N-8): same map both sides, cached haystack ─ */
  function norm(s) {
    return (s || "").normalize("NFKC")
      .replace(/[\u064A\u0649]/g, "ی").replace(/\u0643/g, "ک")
      .replace(/[\u0629]/g, "ه")
      .replace(/[\u0660-\u0669]/g, function (d) { return String.fromCharCode(d.charCodeAt(0) - 1728); })
      .replace(/[\u06F0-\u06F9]/g, function (d) { return String.fromCharCode(d.charCodeAt(0) - 1776); })
      .replace(/\u200c/g, " ").replace(/\u200e|\u200f|\u202a-\u202e/g, "")
      .toLowerCase();
  }
  var searchPanel = doc.getElementById("search");
  if (searchPanel) {
    var input = searchPanel.querySelector("input");
    var hits = searchPanel.querySelector(".search-hits");
    var targets = [];
    var units = doc.querySelectorAll(".source-unit");
    for (var i = 0; i < units.length; i++) {
      var t = units[i].querySelector(".page-text pre");
      targets.push({ el: units[i], txt: norm(t ? t.textContent : units[i].textContent) });
    }
    var cards = doc.querySelectorAll(".toc-cards a, .roadmap a, .flash-grid details, .mnemonic-grid article");
    var ctargets = [];
    for (var j = 0; j < cards.length; j++) ctargets.push({ el: cards[j], txt: norm(cards[j].textContent) });
    function clearMarks() {
      var ms = doc.querySelectorAll("mark[data-sg]");
      for (var m = 0; m < ms.length; m++) {
        var p = ms[m].parentNode;
        p.replaceChild(doc.createTextNode(ms[m].textContent), ms[m]);
        p.normalize();
      }
      var hh = doc.querySelectorAll(".search-hit");
      for (var h = 0; h < hh.length; h++) hh[h].classList.remove("search-hit");
    }
    var deb = null;
    function runSearch() {
      clearMarks();
      var q = norm(input.value).trim();
      if (!q) { if (hits) hits.textContent = ""; return; }
      var found = 0, first = null;
      for (var k = 0; k < targets.length; k++) {
        if (targets[k].txt.indexOf(q) !== -1) {
          found++;
          if (!first) first = targets[k].el;
          targets[k].el.classList.add("search-hit");
          var pre = targets[k].el.querySelector(".page-text pre");
          if (pre) markText(pre, q);
        }
      }
      if (hits) hits.textContent = found > 0
        ? found + " سندِ یافت‌شده برای «" + input.value.trim() + "»"
        : "نتیجه‌ای یافت نشد";
      if (first) {
        var fold = first.querySelector("details");
        if (fold) fold.open = true;
        first.scrollIntoView({ block: "start", behavior: html.getAttribute("data-reduced") === "1" ? "auto" : "smooth" });
      }
    }
    function markText(pre, q) {
      var walker = doc.createTreeWalker(pre, NodeFilter.SHOW_TEXT);
      var n, count = 0;
      while ((n = walker.nextNode()) && count < 40) {
        var v = n.nodeValue, idx = norm(v).indexOf(q);
        if (idx === -1) continue;
        var frag = doc.createDocumentFragment();
        var before = v.substring(0, idx);
        var mid = v.substring(idx, idx + q.length);
        var after = v.substring(idx + q.length);
        if (before) frag.appendChild(doc.createTextNode(before));
        var mk = doc.createElement("mark");
        mk.setAttribute("data-sg", "");
        mk.textContent = mid;
        frag.appendChild(mk);
        if (after) frag.appendChild(doc.createTextNode(after));
        n.parentNode.replaceChild(frag, n);
        count++;
      }
    }
    if (input) {
      input.addEventListener("input", function () {
        clearTimeout(deb);
        deb = setTimeout(runSearch, 160);
      });
      input.addEventListener("keydown", function (ev) {
        if (ev.key === "Escape") { input.value = ""; clearMarks(); if (hits) hits.textContent = ""; }
      });
    }
    doc.addEventListener("keydown", function (ev) {
      if (ev.key === "/" && doc.activeElement !== input && !/INPUT|TEXTAREA|SELECT/.test(doc.activeElement.tagName)) {
        ev.preventDefault(); input.focus();
      }
      if ((ev.ctrlKey || ev.metaKey) && ev.key.toLowerCase() === "k") {
        ev.preventDefault(); input.focus();
      }
    });
  }

  /* ── scrollspy ──────────────────────────────────────────────────────── */
  var navLinks = doc.querySelectorAll("nav.site-nav a[href^='#']");
  var sections = [];
  for (var si = 0; si < navLinks.length; si++) {
    var sec = doc.querySelector(navLinks[si].getAttribute("href"));
    if (sec) sections.push({ a: navLinks[si], s: sec });
  }
  function spy() {
    var y = window.scrollY + 130, cur = null;
    for (var x = 0; x < sections.length; x++) {
      if (sections[x].s.offsetTop <= y) cur = sections[x];
    }
    if (!cur && window.innerHeight + window.scrollY >= doc.body.offsetHeight - 40) {
      cur = sections[sections.length - 1];
    }
    for (var z = 0; z < sections.length; z++) {
      if (sections[z] === cur) {
        sections[z].a.setAttribute("aria-current", "true");
        sections[z].a.classList.add("active");
      } else {
        sections[z].a.removeAttribute("aria-current");
        sections[z].a.classList.remove("active");
      }
    }
  }
  window.addEventListener("scroll", spy, { passive: true });
  spy();

  /* ── quiz engine ────────────────────────────────────────────────────── */
  function setupQuiz(scope, key) {
    var items = scope.querySelectorAll("article:not(.bank-item.ext)");
    if (!items.length) return;
    var answered = 0, correct = 0;
    try {
      var st = JSON.parse(localStorage.getItem(key) || "[]");
      for (var q = 0; q < items.length && q < st.length; q++) {
        if (st[q]) { markAnswer(items[q], st[q]); answered++; if (st[q].right) correct++; }
      }
    } catch (e) {}
    var scoreEl = scope.querySelector(".score");
    if (scoreEl) scoreEl.textContent = answered ? correct + "/" + answered : "—";
    function markAnswer(item, info) {
      var lis = item.querySelectorAll("ol[type='A'] li");
      for (var i = 0; i < lis.length; i++) {
        if (lis[i].getAttribute("data-letter") === info.letter) lis[i].classList.add(info.right ? "correct" : "wrong");
        else if (lis[i].getAttribute("data-letter") === info.correct && !info.right) lis[i].classList.add("correct");
      }
    }
    function save() {
      var arr = [];
      for (var w = 0; w < items.length; w++) {
        var d = items[w].getAttribute("data-answer");
        var picked = items[w].getAttribute("data-picked");
        arr.push(picked ? { letter: picked, right: picked === d, correct: d } : null);
      }
      try { localStorage.setItem(key, JSON.stringify(arr)); } catch (e) {}
    }
    for (var it = 0; it < items.length; it++) {
      (function (item) {
        var answer = item.getAttribute("data-answer");
        var lis = item.querySelectorAll("ol[type='A'] li");
        for (var l = 0; l < lis.length; l++) {
          (function (li) {
            li.setAttribute("role", "button");
            li.setAttribute("tabindex", "0");
            li.setAttribute("data-letter", String.fromCharCode(65 + l));
            function pick() {
              if (item.getAttribute("data-picked")) return;
              var letter = li.getAttribute("data-letter");
              item.setAttribute("data-picked", letter);
              markAnswer(item, { letter: letter, right: letter === answer, correct: answer });
              answered++; if (letter === answer) correct++;
              if (scoreEl) scoreEl.textContent = correct + "/" + answered;
              var det = item.querySelector("details");
              if (det) det.open = true;
              save();
            }
            li.addEventListener("click", pick);
            li.addEventListener("keydown", function (ev) {
              if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); pick(); }
            });
          })(lis[l]);
        }
      })(items[it]);
    }
    var expand = scope.querySelector("[data-act='expand']");
    var collapse = scope.querySelector("[data-act='collapse']");
    var reset = scope.querySelector("[data-act='reset']");
    if (expand) expand.addEventListener("click", function () {
      var ds = scope.querySelectorAll("article details"); for (var e = 0; e < ds.length; e++) ds[e].open = true;
    });
    if (collapse) collapse.addEventListener("click", function () {
      var ds = scope.querySelectorAll("article details"); for (var c = 0; c < ds.length; c++) ds[c].open = false;
    });
    if (reset) reset.addEventListener("click", function () {
      for (var r = 0; r < items.length; r++) {
        items[r].removeAttribute("data-picked");
        var lss = items[r].querySelectorAll("ol[type='A'] li");
        for (var rr = 0; rr < lss.length; rr++) lss[rr].classList.remove("correct", "wrong");
        var dd = items[r].querySelector("details"); if (dd) dd.open = false;
      }
      answered = 0; correct = 0;
      if (scoreEl) scoreEl.textContent = "—";
      try { localStorage.removeItem(key); } catch (e) {}
    });
  }
  setupQuiz(doc.getElementById("quiz"), "sg-quiz-" + (html.getAttribute("data-file") || "x"));
  setupQuiz(doc.getElementById("bank"), "sg-bank-" + (html.getAttribute("data-file") || "x"));

  /* ── fold tools + auto-fold + deep-links ────────────────────────────── */
  var allFolds = doc.querySelectorAll("details.unit-fold");
  function openFoldFor(hash) {
    if (!hash || hash === "#text") return;
    var el = doc.querySelector(hash);
    if (!el) return;
    var fold = el.closest("details");
    if (fold) fold.open = true;
  }
  var openAll = doc.querySelector("[data-act='openall']");
  var closeAll = doc.querySelector("[data-act='closeall']");
  if (openAll) openAll.addEventListener("click", function () {
    for (var o = 0; o < allFolds.length; o++) allFolds[o].open = true;
  });
  if (closeAll) closeAll.addEventListener("click", function () {
    for (var c2 = 0; c2 < allFolds.length; c2++) allFolds[c2].open = false;
  });
  function autoFold() {
    var small = window.innerWidth <= 680;
    if (small && !html.getAttribute("data-autofolded")) {
      for (var a = 0; a < allFolds.length; a++) allFolds[a].open = false;
      html.setAttribute("data-autofolded", "1");
    }
  }
  autoFold();
  window.addEventListener("resize", autoFold);
  doc.addEventListener("click", function (ev) {
    var aEl = ev.target.closest ? ev.target.closest("a[href^='#']") : null;
    if (aEl) openFoldFor(aEl.getAttribute("href"));
  });
  if (location.hash) openFoldFor(location.hash);

  /* ── to-top ─────────────────────────────────────────────────────────── */
  var toTop = doc.getElementById("toTop");
  if (toTop) {
    function ttVis() {
      toTop.classList.toggle("show", window.scrollY > 600);
    }
    window.addEventListener("scroll", ttVis, { passive: true });
    ttVis();
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: html.getAttribute("data-reduced") === "1" ? "auto" : "smooth" });
    });
  }

  /* ── beforeprint: expand all, restore after ─────────────────────────── */
  var closedBeforePrint = [];
  window.addEventListener("beforeprint", function () {
    closedBeforePrint = [];
    for (var b = 0; b < allFolds.length; b++) {
      if (!allFolds[b].open) { closedBeforePrint.push(allFolds[b]); allFolds[b].open = true; }
    }
  });
  window.addEventListener("afterprint", function () {
    for (var ap = 0; ap < closedBeforePrint.length; ap++) closedBeforePrint[ap].open = false;
    closedBeforePrint = [];
  });
})();

