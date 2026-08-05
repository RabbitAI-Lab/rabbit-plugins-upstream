// validate/layout-checks.js — 布局检查(Phase 2 新增;浏览器端自包含函数)
// 规则设计约束:对旧 29 页(纯绝对定位写法)零命中 —— 已由 test/survey.js 预扫描证实:
//   嵌套标记 0 处、未标记流式可见元素 0 处、布局容器内重叠倒挂 0 对。
// 2026-08-02 重构 D 期:新增设计检查(对齐离群/子级溢出),仅在 design.tier 配置后启用。
function layoutChecks(arg) {
  const design = (arg && arg.design) || {};
  const tierOn = !!design.tier;
  const issues = [];
  const OBJ = '[data-object="true"]';
  const container = document.querySelector(".slide-container");
  if (!container) return issues;
  const hidden = (cs) => cs.display === "none" || cs.visibility === "hidden";
  // 只看"自身"可见性:直接文本节点/自身背景(后代已标记时,后代文字不应让容器误报)
  const visibleContent = (el, cs) =>
    cs.backgroundColor !== "rgba(0, 0, 0, 0)" ||
    (cs.backgroundImage && cs.backgroundImage !== "none") ||
    Array.from(el.childNodes).some((n) => n.nodeType === 3 && n.textContent.trim() !== "");
  const isLayoutContainer = (cs) => cs.display.includes("flex") || cs.display.includes("grid");

  // 0) SVG 图标 currentColor 陷阱(2026-08-05 第三轮重构 B0 实测):
  //    截图前页面文字会被 *{color:transparent} 隐藏,stroke/fill=currentColor 随之变透明 →
  //    图标在 PPTX 里空白(浏览器预览正常,极隐蔽)。旧夹具/资产全文无 currentColor(grep 证实),基线零新增。
  document.querySelectorAll(".slide-container svg").forEach((el) => {
    if (/currentColor/i.test(el.outerHTML))
      issues.push({
        level: "WARN",
        msg: "SVG 含 currentColor:转换截图时会被文字隐藏规则变透明,图标将空白",
        fix: "stroke/fill 改显式 hex(或 style=\"stroke:var(--色)\");见 assets/icons.md 铁律",
      });
  });

  // 1) 嵌套 data-object → ERROR(H2:语义不明,提取器只认外层)
  document.querySelectorAll(OBJ).forEach((el) => {
    if (el.parentElement && el.parentElement.closest(OBJ))
      issues.push({
        level: "ERROR",
        msg: `data-object 嵌套:内层标记无效且语义不明: <${el.tagName.toLowerCase()}> "${(el.textContent || "").trim().slice(0, 20)}"`,
        fix: "拆成两个并列的 data-object,或去掉内层标记(外层容器内的子元素本就会按位置逐个提取)",
      });
  });

  // 2) 布局容器(flex/grid)的可见流入子级必须可归结到某个 data-object
  document.querySelectorAll(".slide-container *").forEach((el) => {
    const cs = getComputedStyle(el);
    if (!isLayoutContainer(cs) || hidden(cs)) return;
    Array.from(el.children).forEach((c) => {
      if (c.closest(OBJ)) return; // 自身或祖先已标记 → 会被提取
      const ccs = getComputedStyle(c);
      if (hidden(ccs)) return;
      const r = c.getBoundingClientRect();
      if (r.width < 2 || r.height < 2) return;
      if (visibleContent(c, ccs))
        issues.push({
          level: "ERROR",
          msg: `布局容器(${cs.display})的可见子级未标记 data-object,转换时会被忽略: <${c.tagName.toLowerCase()}> "${(c.textContent || "").trim().slice(0, 20)}"`,
          fix: '给该子级补 data-object="true" data-object-type="textbox|shape",或并入已标记的兄弟元素',
        });
    });
  });

  // 3) 重叠倒挂预警(仅布局容器内的 data-object):PPTX 按 DOM 序叠放,浏览器按 z-index;
  //    两序倒挂且区域重叠时,PPTX 与浏览器视觉分叉(H3)。旧绝对定位页的规则见 html-spec.md。
  document.querySelectorAll(".slide-container *").forEach((parent) => {
    const pcs = getComputedStyle(parent);
    if (!isLayoutContainer(pcs)) return;
    const kids = Array.from(parent.children)
      .filter((c) => c.matches(OBJ))
      .map((c, i) => {
        const z = getComputedStyle(c).zIndex;
        return { el: c, dom: i, z: z === "auto" ? 0 : parseInt(z, 10) || 0, r: c.getBoundingClientRect() };
      });
    for (let i = 0; i < kids.length; i++)
      for (let j = i + 1; j < kids.length; j++) {
        const a = kids[i], b = kids[j];
        const overlap = a.r.left < b.r.right && b.r.left < a.r.right && a.r.top < b.r.bottom && b.r.top < a.r.bottom;
        if (a.z > b.z && overlap)
          issues.push({
            level: "WARN",
            msg: `布局容器内两个 data-object 重叠且 z-index 与 DOM 顺序倒挂,PPTX 叠放(按 DOM 序)将与浏览器不同: "${(b.el.textContent || "").trim().slice(0, 16)}" 会被压到 "${(a.el.textContent || "").trim().slice(0, 16)}" 之下`,
            fix: "调整 DOM 顺序(想压底的放前面),不要再依赖 z-index",
          });
      }
  });

  // 4) 设计检查(2026-08-02,tier 配置后启用)
  if (tierOn) {
    // 4a) 对齐误差两种:
    //  ① 边缘离群:同父 data-object ≥3 个,某元素 left/top 与主簇(≥2 同值)差 1-6px
    //  ② 等距网格突变:同宽同行的 ≥3 个兄弟,相邻间距偏离中位间距 2-8px(卡片网格 typical 事故)
    const parents = new Set();
    document.querySelectorAll(OBJ).forEach((el) => el.parentElement && parents.add(el.parentElement));
    parents.forEach((p) => {
      const kids = Array.from(p.children).filter((c) => c.matches && c.matches(OBJ));
      if (kids.length < 3) return;
      const rects = kids.map((el) => ({ el, r: el.getBoundingClientRect() }));
      // ① 边缘离群(left/top)
      [["left", (r) => r.left], ["top", (r) => r.top]].forEach(([name, fn]) => {
        const edges = rects.map((e) => ({ el: e.el, v: fn(e.r) }));
        const clusters = [];
        edges.forEach((e) => {
          const c = clusters.find((cl) => Math.abs(cl.v - e.v) <= 0.5);
          if (c) c.items.push(e);
          else clusters.push({ v: e.v, items: [e] });
        });
        clusters.sort((a, b) => b.items.length - a.items.length);
        const main = clusters[0];
        if (!main || main.items.length < 2) return;
        clusters.slice(1).forEach((cl) => {
          const d = Math.abs(cl.v - main.v);
          if (d >= 1 && d <= 6)
            cl.items.forEach((e) =>
              issues.push({
                level: "WARN",
                msg: `元素 ${name} 边 ${Math.round(e.v)}px,与同类 ${Math.round(main.v)}px 差 ${d.toFixed(1)}px,疑似对齐误差: "${(e.el.textContent || "").trim().slice(0, 16)}"`,
                fix: `若非刻意错位,对齐到 ${Math.round(main.v)}px`,
              })
            );
        });
      });
      // ② 等距网格突变(横向行)
      const rows = new Map();
      rects.forEach((e) => {
        const key = `${Math.round(e.r.top)}|${Math.round(e.r.width)}`;
        if (!rows.has(key)) rows.set(key, []);
        rows.get(key).push(e);
      });
      rows.forEach((group) => {
        if (group.length < 3) return;
        group.sort((a, b) => a.r.left - b.r.left);
        const gaps = [];
        for (let i = 1; i < group.length; i++)
          gaps.push(group[i].r.left - (group[i - 1].r.left + group[i - 1].r.width));
        const sorted = gaps.slice().sort((a, b) => a - b);
        const median = sorted[Math.floor(sorted.length / 2)];
        gaps.forEach((g, i) => {
          const dev = g - median;
          if (Math.abs(dev) >= 2 && Math.abs(dev) <= 8)
            issues.push({
              level: "WARN",
              msg: `网格间距异常:第 ${i + 2} 个元素与前一元素间距 ${g.toFixed(1)}px(其余约 ${median.toFixed(1)}px): "${(group[i + 1].el.textContent || "").trim().slice(0, 16)}"`,
              fix: "等距网格请保持间距一致(或改用方式 B/C 由布局引擎均分)",
            });
        });
      });
    });

    // 4b) 子级溢出父对象:data-object 的直接子级矩形超出自身 >4px
    //    只查"自带视觉"的子级(背景/边框/图):纯文本子级的溢出归 dom-checks 文字适配管
    document.querySelectorAll(OBJ).forEach((el) => {
      const pr = el.getBoundingClientRect();
      Array.from(el.children).forEach((c) => {
        const cr = c.getBoundingClientRect();
        if (cr.width < 2 || cr.height < 2) return;
        const ccs = getComputedStyle(c);
        const visual =
          (ccs.backgroundColor && ccs.backgroundColor !== "rgba(0, 0, 0, 0)") ||
          (ccs.backgroundImage && ccs.backgroundImage !== "none") ||
          parseFloat(ccs.borderTopWidth) > 0 || parseFloat(ccs.borderRightWidth) > 0 ||
          parseFloat(ccs.borderBottomWidth) > 0 || parseFloat(ccs.borderLeftWidth) > 0 ||
          ["IMG", "SVG", "CANVAS", "TABLE", "VIDEO"].includes(c.tagName);
        if (!visual) return;
        const over = Math.max(cr.right - pr.right, cr.bottom - pr.bottom, pr.left - cr.left, pr.top - cr.top);
        if (over > 4)
          issues.push({
            level: "WARN",
            msg: `子元素溢出父对象 ${Math.round(over)}px: "${(c.textContent || "").trim().slice(0, 16)}"`,
            fix: "收小子元素宽高/字号,或加大父对象",
          });
      });
    });
  }

  return issues;
}

module.exports = { layoutChecks };
