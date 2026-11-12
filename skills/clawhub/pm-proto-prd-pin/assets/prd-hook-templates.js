/**
 * pm-proto-prd-pin 2.0 通用定位钩子模板。
 *
 * 与核心引擎当前版本行为一致：容器映射、动态容器强制重渲染、标题兜底、弹窗分类打开。
 * 所有项目差异都放在 window.PRD_HOOK_CONFIG，本文件不写任何项目名、地址或密钥。
 *
 * PRD_HOOK_CONFIG 字段：
 *   containerHints:  [["#containerId", "viewKey"], ...]
 *   titleViewHints:  { "标题关键词": "viewKey" }
 *   dynamicPattern:  RegExp，命中时即使已在目标视图也强制重渲染
 *   modalOpeners:    [{ title, selector, view, open }]，按顺序匹配
 *   switchView:      function(viewKey) 切视图并渲染动态内容
 *   currentView:     function() 返回当前视图 key
 *   scope:           function() 返回 { top, home }
 */
(function () {
  var cfg = window.PRD_HOOK_CONFIG || {};
  var hints = cfg.containerHints || [];
  var openers = cfg.modalOpeners || [];
  var titleHints = cfg.titleViewHints || {};
  var dynamicPattern = cfg.dynamicPattern || /(?:)/;
  var switchView = typeof cfg.switchView === 'function' ? cfg.switchView : function () {};
  var currentView = typeof cfg.currentView === 'function' ? cfg.currentView : function () { return ''; };
  var scope = typeof cfg.scope === 'function' ? cfg.scope : function () { return { top: '', home: '' }; };

  window.PRD_GET_CURRENT_VIEW = currentView;
  window.PRD_PIN_SCOPE = scope;

  function inferView(selector, pin) {
    var el = null;
    try { el = document.querySelector(selector); } catch (e) {}
    var title = (pin && pin.title) || '';
    var view = '';
    var holder = el && el.closest ? el.closest('[data-view]') : null;
    if (holder) view = holder.getAttribute('data-view') || '';
    if (!view) {
      var m = /\[data-view="([^"]+)"\]/.exec(selector);
      if (m) view = m[1];
    }
    if (!view) {
      var sm = /section:nth-of-type\((\d+)\)/.exec(selector);
      if (sm) {
        var secs = document.querySelectorAll('main section');
        var target = secs[parseInt(sm[1], 10) - 1];
        if (target) view = target.getAttribute('data-view') || '';
      }
    }
    if (!view) {
      for (var i = 0; i < hints.length; i++) {
        if (selector.indexOf(hints[i][0]) >= 0) { view = hints[i][1]; break; }
      }
    }
    if (!view) {
      for (var key in titleHints) {
        if (key && title.indexOf(key) >= 0) { view = titleHints[key]; break; }
      }
    }
    return view;
  }

  window.PRD_PIN_LOCATOR = {
    navigate: function (selector, pin) {
      var view = inferView(selector, pin);
      var dynamic = dynamicPattern.test(selector);
      /* 动态容器锚点即使已在目标视图也重渲染，避免内容未生成导致偶发定位失败。 */
      if (view && (view !== currentView() || dynamic)) switchView(view);
    },
    openModal: function (pin) {
      var title = (pin && pin.title) || '';
      var sel = (pin && pin.selector) || '';
      for (var i = 0; i < openers.length; i++) {
        var o = openers[i];
        var hitTitle = o.title && title.indexOf(o.title) >= 0;
        var hitSelector = o.selector && sel.indexOf(o.selector) >= 0;
        if (!hitTitle && !hitSelector) continue;
        if (o.view) switchView(o.view);
        if (typeof o.open === 'function') {
          try { o.open(); } catch (e) { console.warn('[prd-locate]', e); }
        }
        return;
      }
    }
  };
})();
