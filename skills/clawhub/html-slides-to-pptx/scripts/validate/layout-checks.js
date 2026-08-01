// validate/layout-checks.js — 布局检查(Phase 2 新增;浏览器端自包含函数)
// 规则设计约束:对旧 29 页(纯绝对定位写法)零命中 —— 已由 test/survey.js 预扫描证实:
//   嵌套标记 0 处、未标记流式可见元素 0 处、布局容器内重叠倒挂 0 对。
function layoutChecks() {
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

  return issues;
}

module.exports = { layoutChecks };
