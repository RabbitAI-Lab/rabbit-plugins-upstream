/* 知识库 HTML 报告预览 —— docsify 插件（独立文件）
 *
 * 站内 .html/.htm 报告（如迭代报告、热力图、导出的网页报表）点击后，
 * 在右侧内容区以 iframe 平铺预览，覆盖 docsify 的 404。
 * HTML 自带样式与脚本（tab 切换、悬浮提示等），iframe 隔离渲染最干净，
 * 不会与 docsify / 页面样式互相干扰。
 *
 * 与 table-preview.js 同构：hashchange + MutationObserver 兜底；
 * iframe 同源加载，高度随内容自适应（load / ResizeObserver / 窗口缩放）。
 */
(function () {
  'use strict';

  var HTML_RE = /\.html?(\?.*)?$/i;   // .htm / .html

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  function fileNameOf(url) {
    var s = String(url).split('?')[0].split('#')[0].split('/').pop();
    try { return decodeURIComponent(s); } catch (e) { return s; }
  }

  function siteBase() {
    return location.pathname.replace(/[^/]*$/, '');
  }

  // 内容根容器：观察 .content 能同时覆盖 docsify 正文与目录页
  function contentRoot() {
    return document.querySelector('.content') || document.querySelector('#main') ||
      document.querySelector('.markdown-section') || document.body;
  }

  // 右侧内容区容器：#main（docsify 渲染正文的 article），找不到时回退创建
  function mainContainer() {
    var m = document.querySelector('#main') || document.querySelector('.markdown-section');
    if (m) return m;
    var c = document.querySelector('.content');
    if (c) {
      var art = el('article');
      art.id = 'main';
      art.className = 'markdown-section';
      c.appendChild(art);
      return art;
    }
    return contentRoot();
  }

  /* ---------- iframe 高度自适应（同源文档可直接读） ---------- */
  var fitTimer = 0;
  function scheduleFit(f) {
    if (fitTimer) clearTimeout(fitTimer);
    fitTimer = setTimeout(function () { fitFrame(f); }, 120);
  }
  function fitFrame(f) {
    var doc = f.contentDocument;
    if (!doc) return;
    var h = 0;
    try {
      h = doc.documentElement.scrollHeight || doc.body.scrollHeight || 0;
    } catch (e) { /* 跨域等异常保持原高度 */ }
    if (!h) return;
    var vh = window.innerHeight || 600;
    // 内容不足一屏时不高不矮按内容，超高则完整展开（整页随外层滚动）
    f.style.height = Math.max(h + 4, Math.min(600, vh)) + 'px';
  }
  function watchFrame(f) {
    var doc = f.contentDocument;
    if (!doc || !doc.body) return;
    if (window.ResizeObserver) {
      try {
        new ResizeObserver(function () { scheduleFit(f); }).observe(doc.body);
      } catch (e) { /* 个别浏览器不支持则退化为 load/resize 触发 */ }
    }
  }

  /* ---------- 路由 ---------- */
  function routeHtmlFile() {
    var h = location.hash || '';
    if (h.indexOf('#/') !== 0) return null;
    var path = h.slice(2).split('?')[0].split('#')[0];
    if (!HTML_RE.test(path)) return null;
    var decoded;
    try { decoded = decodeURIComponent(path); } catch (e) { decoded = path; }
    var pathname = location.pathname;
    if (/\/index\.html$/.test(pathname)) pathname = pathname.slice(0, -'index.html'.length);
    if (pathname && !/\/$/.test(pathname)) pathname += '/';
    return { fileUrl: location.origin + pathname + decoded, routePath: decoded };
  }

  function renderHtmlInline(fileUrl, label) {
    var main = mainContainer();
    if (!main) return;

    var page = el('div', 'kb-html-page');
    var head = el('div', 'kb-html-head');
    head.appendChild(el('span', 'kb-html-title', esc(label || fileNameOf(fileUrl))));
    var open = el('a', 'kb-html-open', '新窗口打开');
    open.href = fileUrl;
    open.target = '_blank';
    open.rel = 'noopener';
    head.appendChild(open);
    page.appendChild(head);

    var fr = el('iframe', 'kb-html-frame');
    fr.src = fileUrl;
    page.appendChild(fr);

    main.innerHTML = '';
    main.appendChild(page);

    fr.addEventListener('load', function () { fitFrame(fr); watchFrame(fr); });
    fitFrame(fr);
  }

  // 幂等渲染：右侧内容区已有 html 预览则跳过。
  // docsify 会先把 fetch 到的 html 源码当 markdown 写入 #main（渲染成一堆乱码），
  // 用 50ms 防抖延迟到它写完后覆盖；MutationObserver 观察内容区，被 docsify 重写时兜底重铺。
  var renderTimer = 0;
  function ensureHtmlRoute() {
    var r = routeHtmlFile();
    if (!r) return;
    var main = mainContainer();
    if (main && main.querySelector('.kb-html-page')) return;
    clearTimeout(renderTimer);
    renderTimer = setTimeout(function () {
      var rr = routeHtmlFile();
      if (rr) renderHtmlInline(rr.fileUrl, fileNameOf(rr.fileUrl));
    }, 50);
  }

  /* ---------- 入口 ---------- */
  function start() {
    var mo = new MutationObserver(function () { ensureHtmlRoute(); });
    var observeTarget = function () {
      var root = contentRoot();
      if (root) mo.observe(root, { childList: true, subtree: true });
    };
    observeTarget();
    ensureHtmlRoute();
    setTimeout(observeTarget, 300);
    setTimeout(observeTarget, 1500);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();

  window.addEventListener('hashchange', function () {
    ensureHtmlRoute();
    setTimeout(ensureHtmlRoute, 250);
  });
  // 首屏直接打开 html 路由（粘贴 URL / 侧边栏直达）也能预览
  ensureHtmlRoute();
  setTimeout(ensureHtmlRoute, 600);
})();
