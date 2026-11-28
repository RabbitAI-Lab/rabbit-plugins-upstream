/* Narration layer for editable decks. Injected by narrate.py; reads #narration-data
 * and follows the deck's active slide. It never edits the deck state. */
(() => {
  'use strict';
  const dataEl = document.getElementById('narration-data');
  if (!dataEl) return;
  let data;
  try {
    data = JSON.parse(dataEl.textContent || '{}');
  } catch {
    return;
  }
  const tracks = data.slides || {};
  const SPEEDS = [0.75, 1, 1.25, 1.5, 2];
  const PREF_KEY = 'audio-report-deck:player';
  const STRINGS = {
    en: { exit: 'Exit', play: 'Play narration', pause: 'Pause', speed: 'Playback speed', auto: 'Auto-advance', script: 'Show script', noAudio: 'No narration on this page', stale: 'Script changed after recording', page: 'Page' },
    zh: { exit: '\u9000\u51fa', play: '\u64ad\u653e\u65c1\u767d', pause: '\u6682\u505c', speed: '\u500d\u901f', auto: '\u81ea\u52a8\u8fde\u64ad', script: '\u67e5\u770b\u8bb2\u7a3f', noAudio: '\u672c\u9875\u6ca1\u6709\u65c1\u767d', stale: '\u8bb2\u7a3f\u5728\u5f55\u97f3\u540e\u6539\u8fc7', page: '\u7b2c' },
    'zh-tw': { exit: '\u9000\u51fa', play: '\u64ad\u653e\u65c1\u767d', pause: '\u66ab\u505c', speed: '\u500d\u901f', auto: '\u81ea\u52d5\u9023\u64ad', script: '\u67e5\u770b\u8b1b\u7a3f', noAudio: '\u672c\u9801\u6c92\u6709\u65c1\u767d', stale: '\u8b1b\u7a3f\u5728\u9304\u97f3\u5f8c\u6539\u904e', page: '\u7b2c' },
    ja: { exit: '\u7d42\u4e86', play: '\u30ca\u30ec\u30fc\u30b7\u30e7\u30f3\u3092\u518d\u751f', pause: '\u4e00\u6642\u505c\u6b62', speed: '\u518d\u751f\u901f\u5ea6', auto: '\u81ea\u52d5\u3067\u6b21\u3078', script: '\u539f\u7a3f\u3092\u8868\u793a', noAudio: '\u3053\u306e\u30da\u30fc\u30b8\u306b\u306f\u30ca\u30ec\u30fc\u30b7\u30e7\u30f3\u304c\u3042\u308a\u307e\u305b\u3093', stale: '\u9332\u97f3\u5f8c\u306b\u539f\u7a3f\u304c\u5909\u66f4\u3055\u308c\u307e\u3057\u305f', page: '\u30da\u30fc\u30b8' },
    ko: { exit: '\ub098\uac00\uae30', play: '\ub0b4\ub808\uc774\uc158 \uc7ac\uc0dd', pause: '\uc77c\uc2dc\uc815\uc9c0', speed: '\uc7ac\uc0dd \uc18d\ub3c4', auto: '\uc790\ub3d9 \ub118\uae40', script: '\ub300\ubcf8 \ubcf4\uae30', noAudio: '\uc774 \ud398\uc774\uc9c0\uc5d0\ub294 \ub0b4\ub808\uc774\uc158\uc774 \uc5c6\uc2b5\ub2c8\ub2e4', stale: '\ub179\uc74c \ud6c4 \ub300\ubcf8\uc774 \ubcc0\uacbd\ub428', page: '\ud398\uc774\uc9c0' },
    es: { exit: 'Salir', play: 'Reproducir narraci\u00f3n', pause: 'Pausa', speed: 'Velocidad', auto: 'Avance autom\u00e1tico', script: 'Ver guion', noAudio: 'Esta p\u00e1gina no tiene narraci\u00f3n', stale: 'El guion cambi\u00f3 tras la grabaci\u00f3n', page: 'P\u00e1gina' },
    'pt-br': { exit: 'Sair', play: 'Reproduzir narra\u00e7\u00e3o', pause: 'Pausar', speed: 'Velocidade', auto: 'Avan\u00e7o autom\u00e1tico', script: 'Ver roteiro', noAudio: 'Esta p\u00e1gina n\u00e3o tem narra\u00e7\u00e3o', stale: 'Roteiro alterado ap\u00f3s a grava\u00e7\u00e3o', page: 'P\u00e1gina' },
    de: { exit: 'Beenden', play: 'Erz\u00e4hlung abspielen', pause: 'Pause', speed: 'Geschwindigkeit', auto: 'Automatisch weiter', script: 'Skript anzeigen', noAudio: 'Diese Seite hat keine Erz\u00e4hlung', stale: 'Skript nach der Aufnahme ge\u00e4ndert', page: 'Seite' },
    fr: { exit: 'Quitter', play: 'Lire la narration', pause: 'Pause', speed: 'Vitesse', auto: 'Lecture encha\u00een\u00e9e', script: 'Voir le texte', noAudio: 'Cette page n\u2019a pas de narration', stale: 'Texte modifi\u00e9 apr\u00e8s l\u2019enregistrement', page: 'Page' },
  };
  const ICONS = {
    play: '<path d="M7 4v16l13-8z"/>',
    pause: '<path d="M8 5v14M16 5v14"/>',
    auto: '<path d="m5 4 10 8-10 8z"/><path d="M19 5v14"/>',
    script: '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
  };
  const icon = (name) => `<svg viewBox="0 0 24 24" aria-hidden="true">${ICONS[name]}</svg>`;

  let prefs = { speed: 1, auto: true };
  try {
    prefs = { ...prefs, ...JSON.parse(localStorage.getItem(PREF_KEY) || '{}') };
  } catch {}
  const savePrefs = () => {
    try {
      localStorage.setItem(PREF_KEY, JSON.stringify(prefs));
    } catch {}
  };

  const audio = new Audio();
  audio.preload = 'auto';
  let index = -1;
  let loadedId = null;
  let wantPlay = false;
  let advancing = false;
  let hideTimer = 0;

  function deck() {
    return window.editableDeck;
  }
  function slides() {
    try {
      return deck()?.getState()?.slides || [];
    } catch {
      return [];
    }
  }
  function locale() {
    const raw = String(deck()?.getLocale?.() || document.documentElement.lang || 'en').toLowerCase();
    if (STRINGS[raw]) return raw;
    if (raw.startsWith('zh')) return /tw|hk|hant/.test(raw) ? 'zh-tw' : 'zh';
    if (raw.startsWith('pt')) return 'pt-br';
    return STRINGS[raw.slice(0, 2)] ? raw.slice(0, 2) : 'en';
  }
  const t = (key) => (STRINGS[locale()] || STRINGS.en)[key] || STRINGS.en[key];

  // FNV-1a over whitespace-normalized text; must match narrate.py text_hash().
  function textHash(text) {
    const s = String(text || '').replace(/\s+/g, ' ').trim();
    let h = 0x811c9dc5;
    const bytes = new TextEncoder().encode(s);
    for (const b of bytes) {
      h ^= b;
      h = Math.imul(h, 0x01000193) >>> 0;
    }
    return h.toString(16).padStart(8, '0');
  }

  function activeIndex() {
    const el = document.querySelector('#canvas .card-section.active');
    return el ? Number(el.dataset.cardIndex) : 0;
  }
  const isPresenting = () => document.body.classList.contains('presentation');
  const isViewing = () => document.body.classList.contains('viewing');

  document.getElementById('narration-bar')?.remove();
  document.getElementById('narration-script')?.remove();
  const bar = document.createElement('div');
  bar.id = 'narration-bar';
  bar.setAttribute('role', 'toolbar');
  bar.innerHTML = `
    <button type="button" class="nb-btn nb-play" data-nb="play">${icon('play')}</button>
    <div class="nb-track"><span class="nb-page"></span><input type="range" min="0" max="1000" value="0" class="nb-seek"><span class="nb-time">0:00</span></div>
    <button type="button" class="nb-btn nb-speed" data-nb="speed">1\u00d7</button>
    <button type="button" class="nb-btn nb-toggle nb-auto" data-nb="auto">${icon('auto')}<span class="nb-label"></span></button>
    <button type="button" class="nb-btn nb-toggle" data-nb="script">${icon('script')}</button>
    <span class="nb-sep" aria-hidden="true"></span>
    <button type="button" class="nb-btn nb-exit" data-nb="exit"></button>`;
  const panel = document.createElement('aside');
  panel.id = 'narration-script';
  panel.hidden = true;
  document.body.append(bar, panel);
  const $ = (sel) => bar.querySelector(sel);
  const seek = $('.nb-seek');

  function fmt(sec) {
    if (!Number.isFinite(sec)) return '0:00';
    const s = Math.max(0, Math.round(sec));
    return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
  }

  function labels() {
    $('[data-nb=speed]').title = $('[data-nb=speed]').ariaLabel = t('speed');
    $('[data-nb=auto]').title = $('[data-nb=auto]').ariaLabel = `${t('auto')} (A)`;
    $('[data-nb=auto] .nb-label').textContent = t('auto');
    $('[data-nb=exit]').textContent = t('exit');
    $('[data-nb=script]').title = $('[data-nb=script]').ariaLabel = t('script');
    seek.ariaLabel = t('play');
    const playing = !audio.paused;
    const play = $('[data-nb=play]');
    play.innerHTML = icon(playing ? 'pause' : 'play');
    play.title = play.ariaLabel = playing ? t('pause') : t('play');
    $('[data-nb=speed]').textContent = `${prefs.speed}\u00d7`;
    $('[data-nb=auto]').classList.toggle('on', !!prefs.auto);
    $('[data-nb=auto]').setAttribute('aria-pressed', String(!!prefs.auto));
    $('[data-nb=script]').classList.toggle('on', !panel.hidden);
  }

  function current() {
    const list = slides();
    const slide = list[index];
    if (!slide) return { slide: null, track: null, total: list.length };
    return { slide, track: tracks[slide.id] || null, total: list.length };
  }

  function renderInfo() {
    const { slide, track, total } = current();
    const page = $('.nb-page');
    page.textContent = `${index + 1} / ${total}`;
    const notes = slide?.notes || '';
    const stale = !!(track && track.textHash && notes && textHash(notes) !== track.textHash);
    bar.classList.toggle('nb-empty', !track);
    bar.classList.toggle('nb-stale', stale);
    seek.disabled = !track;
    bar.title = !track ? t('noAudio') : stale ? t('stale') : '';
    panel.textContent = notes || t('noAudio');
    panel.lang = slide?.locale || '';
    labels();
  }

  function load(play) {
    const { slide, track } = current();
    const id = slide?.id || null;
    if (id !== loadedId) {
      loadedId = id;
      audio.pause();
      seek.value = 0;
      $('.nb-time').textContent = fmt(track?.duration);
      if (track?.src) {
        audio.src = track.src;
        audio.playbackRate = prefs.speed;
      } else {
        audio.removeAttribute('src');
        audio.load();
      }
    }
    renderInfo();
    if (play && track?.src) {
      audio.playbackRate = prefs.speed;
      audio.play().catch(() => {
        wantPlay = false;
        labels();
      });
    } else if (play && !track && prefs.auto) {
      // Silent page: hold briefly, then continue the run.
      setTimeout(() => {
        if (wantPlay && current().slide?.id === id) goNext();
      }, 2500);
    }
  }

  function goTo(target) {
    const list = slides();
    if (target < 0 || target >= list.length) return false;
    if (isPresenting()) {
      const btn = document.querySelector(`#present-nav [data-act=${target > activeIndex() ? 'next' : 'prev'}]`);
      for (let i = Math.abs(target - activeIndex()); i > 0 && btn; i -= 1) btn.click();
    } else {
      const card = document.querySelector(`#canvas .card-section[data-card-index="${target}"]`);
      if (card) window.scrollTo({ top: Math.max(0, scrollY + card.getBoundingClientRect().top - 124), behavior: 'smooth' });
    }
    return true;
  }
  function goNext() {
    advancing = true;
    if (!goTo(index + 1)) {
      wantPlay = false;
      advancing = false;
      labels();
    }
  }

  function sync() {
    const next = activeIndex();
    if (next === index) return;
    index = next;
    const resume = wantPlay;
    advancing = false;
    load(resume);
  }

  function togglePlay() {
    const { track } = current();
    if (!audio.paused) {
      wantPlay = false;
      audio.pause();
    } else {
      wantPlay = true;
      if (track?.src) load(true);
      else if (prefs.auto) goNext();
    }
    labels();
  }

  bar.addEventListener('click', (event) => {
    const button = event.target.closest('[data-nb]');
    if (!button) return;
    event.stopPropagation();
    const action = button.dataset.nb;
    if (action === 'play') togglePlay();
    if (action === 'speed') {
      prefs.speed = SPEEDS[(SPEEDS.indexOf(prefs.speed) + 1) % SPEEDS.length] || 1;
      audio.playbackRate = prefs.speed;
      savePrefs();
    }
    if (action === 'auto') {
      prefs.auto = !prefs.auto;
      savePrefs();
    }
    if (action === 'script') panel.hidden = !panel.hidden;
    if (action === 'exit') {
      wantPlay = false;
      audio.pause();
      document.querySelector('#present-nav [data-act=exit-present]')?.click();
    }
    labels();
  });
  seek.addEventListener('input', () => {
    if (Number.isFinite(audio.duration)) audio.currentTime = (seek.value / 1000) * audio.duration;
  });
  audio.addEventListener('timeupdate', () => {
    if (Number.isFinite(audio.duration) && audio.duration > 0) {
      seek.value = Math.round((audio.currentTime / audio.duration) * 1000);
      $('.nb-time').textContent = `${fmt(audio.currentTime)} / ${fmt(audio.duration)}`;
    }
  });
  audio.addEventListener('play', labels);
  audio.addEventListener('pause', labels);
  audio.addEventListener('ended', () => {
    labels();
    if (wantPlay && prefs.auto) setTimeout(goNext, 600);
    else wantPlay = false;
  });

  // Space plays or pauses the narration. Captured before the deck sees it, which would
  // otherwise turn the page (Present) or scroll (page view).
  let spaceHandled = false;
  window.addEventListener(
    'keydown',
    (event) => {
      if (event.key !== ' ' || event.metaKey || event.ctrlKey || event.altKey) return;
      if (event.target.closest?.('input,textarea,select,[contenteditable=true]')) return;
      if (!isViewing() && !isPresenting()) return;
      event.preventDefault();
      event.stopImmediatePropagation();
      spaceHandled = true;
      if (!event.repeat) togglePlay();
    },
    true
  );
  window.addEventListener(
    'keyup',
    (event) => {
      if (event.key !== ' ' || !spaceHandled) return;
      // Keep a focused button from also firing a click on key release.
      event.preventDefault();
      event.stopImmediatePropagation();
      spaceHandled = false;
    },
    true
  );

  document.addEventListener('keydown', (event) => {
    if (event.metaKey || event.ctrlKey || event.altKey) return;
    if (event.target.closest?.('input,textarea,select,[contenteditable=true]')) return;
    if (!isViewing() && !isPresenting()) return;
    const key = event.key.toLowerCase();
    if (key === 'p') {
      event.preventDefault();
      togglePlay();
    } else if (key === 'a') {
      event.preventDefault();
      prefs.auto = !prefs.auto;
      savePrefs();
      labels();
    } else if (key === ']') {
      event.preventDefault();
      prefs.speed = SPEEDS[(SPEEDS.indexOf(prefs.speed) + 1) % SPEEDS.length] || 1;
      audio.playbackRate = prefs.speed;
      savePrefs();
      labels();
    }
  });

  function wake() {
    bar.classList.remove('nb-idle');
    clearTimeout(hideTimer);
    if (isPresenting()) hideTimer = setTimeout(() => bar.classList.add('nb-idle'), 5000);
  }
  ['pointermove', 'pointerdown', 'keydown'].forEach((type) => document.addEventListener(type, wake, { passive: true }));

  function start() {
    if (!deck()) {
      setTimeout(start, 120);
      return;
    }
    const canvas = document.getElementById('canvas');
    new MutationObserver(() => {
      sync();
      if (!advancing) renderInfo();
    }).observe(canvas, { subtree: true, childList: true, attributes: true, attributeFilter: ['class'] });
    new MutationObserver(wake).observe(document.body, { attributes: true, attributeFilter: ['class'] });
    index = -1;
    sync();
    wake();
  }
  start();
})();
