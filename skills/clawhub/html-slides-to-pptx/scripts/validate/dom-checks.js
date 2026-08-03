// validate/dom-checks.js — 浏览器计算样式检查
// 该函数被序列化进页面执行(page.evaluate),必须保持自包含、无闭包依赖。
// 画布尺寸由调用方以单参数对象注入(page.evaluate(domChecks, {w, h});
// Playwright evaluate 只接受一个参数),勿在函数体内硬编码。
// 规则与旧 validate.js 逐字一致。
function domChecks(canvas) {
  const canvasW = canvas.w, canvasH = canvas.h;
  const issues = [];
  const container = document.querySelector(".slide-container");
  if (!container) return issues;
  const base = container.getBoundingClientRect();
  if (Math.round(base.width) !== canvasW || Math.round(base.height) !== canvasH)
    issues.push({ level: "ERROR", msg: `.slide-container 尺寸为 ${Math.round(base.width)}x${Math.round(base.height)},应为 ${canvasW}x${canvasH}`, fix: "检查容器 width/height 及缩放" });

  const INLINE = new Set(["SPAN", "BR", "B", "I", "STRONG", "EM", "A", "SUP", "SUB", "FONT"]);
  const hasBlockChild = (el) => Array.from(el.children).some((c) => !INLINE.has(c.tagName));

  // 1) 未标记 data-object 的可见元素(不在任何 data-object 之内) → 不会被提取
  //    Phase 2 起不再限绝对定位:流式/flex/grid 子级同样必须标记(测绘证实旧页零命中)
  document.querySelectorAll(".slide-container *").forEach((el) => {
    const cs = getComputedStyle(el);
    if (cs.display === "none" || cs.visibility === "hidden") return;
    if (el.closest('[data-object="true"]') !== el && el.closest('[data-object="true"]')) return; // 在被标记的祖先内,OK
    if (el.closest('[data-object="true"]')) return;
    // 布局容器的直接子级由 layout-checks 给出更具体的报错,此处不重复
    if (el.parentElement) {
      const pd = getComputedStyle(el.parentElement).display;
      if (pd.includes("flex") || pd.includes("grid")) return;
    }
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return;
    // 只看"自身"可见性:直接文本节点/自身背景。后代文字若在未标记后代里,后代会被各自检查;
    // 容器内已标记子级的文字不应让未标记容器本身误报(flex/grid 布局容器正是此形态)
    const directText = Array.from(el.childNodes).some((n) => n.nodeType === 3 && n.textContent.trim() !== "");
    const hasVisual = cs.backgroundColor !== "rgba(0, 0, 0, 0)" || (cs.backgroundImage && cs.backgroundImage !== "none") || directText;
    if (hasVisual)
      issues.push({ level: "ERROR", msg: `元素未标记 data-object="true",转换时会被忽略: <${el.tagName.toLowerCase()}> "${(el.textContent || "").trim().slice(0, 20)}"`, fix: "补上 data-object=\"true\" data-object-type=\"textbox|shape\"" });
  });

  // 2) 文本检查:多行无显式行高 / rgba 文字 / 非统一边框
  document.querySelectorAll('[data-object="true"]').forEach((el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const fs = parseFloat(cs.fontSize) || 16;
    const isTextLeaf = !hasBlockChild(el) && (el.textContent || "").trim() !== "";
    if (isTextLeaf) {
      const lh = cs.lineHeight;
      // 仅在"可能折行"时才提示:估算文本宽度超过盒宽 且 盒高超过单行
      const text = el.textContent.trim();
      const estWidth = text.length * fs * 0.95;
      const mayWrap = estWidth > r.width * 1.05 && r.height > fs * 1.6;
      if (lh === "normal" && mayWrap)
        issues.push({ level: "WARN", msg: `多行文字未设显式 line-height,行距将不可控: "${text.slice(0, 20)}"`, fix: "给该文本加 line-height(如 1.5 或 31px)" });
      const m = /rgba\(([^)]+)\)/.exec(cs.color);
      if (m && parseFloat(m[1].split(",")[3]) < 1)
        issues.push({ level: "WARN", msg: `文字颜色带透明度,转换后变为纯色: "${el.textContent.trim().slice(0, 20)}" (${cs.color})`, fix: "改用不透明的混合色值(手算与底色的混合结果)" });
    }
    const bw = [cs.borderTopWidth, cs.borderRightWidth, cs.borderBottomWidth, cs.borderLeftWidth];
    const nonZero = bw.filter((w) => parseFloat(w) > 0);
    const radius = parseFloat(cs.borderTopLeftRadius) || 0;
    // 非统一边框已支持(逐边细条),但与圆角共存时不贴合 → 仅此时提示
    if (nonZero.length > 0 && new Set(bw).size > 1 && radius > 0)
      issues.push({ level: "WARN", msg: `圆角卡片使用非统一边框(${bw.join("/")}),逐边细条不贴合圆角`, fix: "圆角卡改用统一边框,或强调条用独立细长 shape" });
  });

  // 3) 容器背景为渐变/图片:PPTX 幻灯片背景只支持纯色(纯色容器背景会自动导出,无需处理)
  const ccs = getComputedStyle(container);
  if (ccs.backgroundImage && ccs.backgroundImage !== "none")
    issues.push({ level: "WARN", msg: ".slide-container 使用渐变/图片背景,幻灯片背景只支持纯色,该背景会丢失", fix: "加一个 1920x1080 全画布 data-object shape 铺渐变(将被截图还原)" });

  // 4) 完全在画布外的元素:不可见(部分超出的截图元素已自动取交集,无需处理)
  document.querySelectorAll('[data-object="true"]').forEach((el) => {
    const r = el.getBoundingClientRect();
    const relX = r.left - base.left, relY = r.top - base.top;
    if (relX + r.width <= 0 || relY + r.height <= 0 || relX >= canvasW || relY >= canvasH)
      issues.push({ level: "WARN", msg: `元素完全在画布外,不会显示: <${el.tagName.toLowerCase()}> "${(el.textContent || "").trim().slice(0, 20)}"`, fix: "移入 1920x1080 画布内,或删除" });
  });

  // 5) font-weight:500 会退化为常规体(PPTX 只有常规/粗体两档)
  document.querySelectorAll(".slide-container *").forEach((el) => {
    const hasDirectText = Array.from(el.childNodes).some((n) => n.nodeType === 3 && n.textContent.trim() !== "");
    if (!hasDirectText) return;
    const cs = getComputedStyle(el);
    if (parseInt(cs.fontWeight, 10) === 500)
      issues.push({ level: "WARN", msg: `font-weight:500 在 PPTX 中退化为常规体: "${el.textContent.trim().slice(0, 20)}"`, fix: "改用 400(常规)或 600(粗体)" });
  });

  // 6) 2026-07-27 P0/P1:静默消失类元素硬提示 / P2 2.6:video/audio 已支持(addMedia)
  // <canvas> 已支持(整体截图 / data-chart 原生图表)
  // video/audio:已支持原生嵌入(addMedia);video 建议 poster 属性(否则用截屏做封面)
  document.querySelectorAll(".slide-container iframe, .slide-container form").forEach((el) => {
    issues.push({ level: "ERROR", msg: `<${el.tagName.toLowerCase()}> 不支持转换,会被整个忽略`, fix: "内容拆成原生元素;表单改用静态展示" });
  });
  document.querySelectorAll(".slide-container video").forEach((el) => {
    if (!el.getAttribute("src") && !el.querySelector("source"))
      issues.push({ level: "WARN", msg: `<video> 未指定 src,将仅用封面图展示`, fix: "加 src 属性指向本地视频文件" });
    if (!el.getAttribute("poster") && !el.getAttribute("data-poster"))
      issues.push({ level: "WARN", msg: `<video> 未设 poster,将截取浏览器渲染帧做封面(可能黑屏)`, fix: "加 poster 属性指向封面图" });
  });
  document.querySelectorAll(".slide-container audio").forEach((el) => {
    if (!el.getAttribute("src") && !el.querySelector("source"))
      issues.push({ level: "WARN", msg: `<audio> 未指定 src,将被忽略`, fix: "加 src 属性指向本地音频文件" });
  });

  // 7) 容器必须位于视口原点:截图按视口坐标、基元按容器坐标,偏移会导致截图错位
  if (Math.abs(base.left) > 1 || Math.abs(base.top) > 1)
    issues.push({ level: "ERROR", msg: `.slide-container 未位于 (0,0)(实际 ${Math.round(base.left)},${Math.round(base.top)}),截图将与原生元素错位`, fix: "html,body 设 margin:0;padding:0;容器不要加 margin/位移" });

  // 8) 视觉效果类样式:2026-07-27 P1 起整体转截图(非编辑);特效元素内文字会丢失可编辑性
  document.querySelectorAll(".slide-container *").forEach((el) => {
    const cs = getComputedStyle(el);
    if (cs.mixBlendMode && cs.mixBlendMode !== "normal")
      issues.push({ level: "WARN", msg: `mix-blend-mode:${cs.mixBlendMode} 元素整体转截图(不可编辑)`, fix: "文字放在特效元素之外的独立 textbox 叠加" });
    if (cs.filter && cs.filter !== "none")
      issues.push({ level: "WARN", msg: `filter:${cs.filter} 元素整体转截图(不可编辑)`, fix: "文字放在特效元素之外的独立 textbox 叠加" });
    if (cs.backdropFilter && cs.backdropFilter !== "none")
      issues.push({ level: "WARN", msg: `backdrop-filter:${cs.backdropFilter} 元素整体转截图(不可编辑)`, fix: "文字放在特效元素之外的独立 textbox 叠加" });
    if (cs.clipPath && cs.clipPath !== "none")
      issues.push({ level: "WARN", msg: `clip-path:${cs.clipPath} 元素整体转截图(不可编辑)`, fix: "裁剪形状内的文字改放独立 textbox" });
    if (cs.outlineStyle && cs.outlineStyle !== "none" && parseFloat(cs.outlineWidth) > 0)
      issues.push({ level: "WARN", msg: "outline 不转换", fix: "改用 border(支持逐边/虚线)或独立细条 shape" });
  });

  // 9) transform 计算样式级语义检查(静态正则只覆盖内联字面量;此处兜住 matrix/类名写法)
  document.querySelectorAll(".slide-container *").forEach((el) => {
    const cs = getComputedStyle(el);
    const t = cs.transform;
    if (!t || t === "none") return;
    const m = /^matrix\(([^)]+)\)$/.exec(t);
    if (!m) return;
    const [a, b, c, d] = m[1].split(",").map((v) => parseFloat(v.trim()));
    const eps = 1e-6;
    const identity = Math.abs(a - 1) < eps && Math.abs(d - 1) < eps && Math.abs(b) < eps && Math.abs(c) < eps;
    if (identity) return; // 纯平移:无视觉变换
    const isRot = Math.abs(a - d) < 1e-4 && Math.abs(b + c) < 1e-4 && Math.abs(a * a + b * b - 1) < 1e-3;
    if (!isRot) {
      issues.push({ level: "ERROR", msg: `transform 含缩放/斜切(${t.slice(0, 40)}…),PPTX 中丢失: <${el.tagName.toLowerCase()}>`, fix: "仅支持纯旋转 rotate();尺寸用宽高表达,斜切图形改放图片背景" });
      return;
    }
    // 纯旋转:transform-origin 必须居中(PPTX 绕中心旋转)
    // 用 offsetWidth/Height(未旋转尺寸)判定;getBoundingClientRect 是旋转后包围盒,会误报
    const ori = (cs.transformOrigin || "").split(/\s+/);
    const ox = parseFloat(ori[0]), oy = parseFloat(ori[1]);
    if ((!isNaN(ox) && Math.abs(ox - el.offsetWidth / 2) > 1) || (!isNaN(oy) && Math.abs(oy - el.offsetHeight / 2) > 1))
      issues.push({ level: "WARN", msg: `旋转元素的 transform-origin 非居中(${cs.transformOrigin}),PPTX 将绕中心旋转,位置会有偏差`, fix: "改为 transform-origin:center,或旋转后用 left/top 重新对位" });
  });

  // 10) 2026-07-27 D6:<img> 必须显式声明 object-fit
  // 缺省时 CSS 默认 fill,与"我忘了写"无法区分 → 转换器按 fill(拉伸)处理,易出现非预期变形
  // 装饰图推荐 background-image(走截图路径);<img> 定位"内容照片/产品图"(原生可编辑图片)
  document.querySelectorAll(".slide-container img").forEach((el) => {
    const cs = getComputedStyle(el);
    if (cs.objectFit === "fill" && !el.style.objectFit && !el.getAttribute("object-fit"))
      issues.push({ level: "WARN", msg: `<img> 未显式声明 object-fit,默认按 fill(拉伸)处理,可能变形`, fix: "内容照片建议 object-fit:cover 或 contain;纯装饰图改用 background-image" });
  });

  // 11) 2026-07-27 P2 2.4:data-shape 预设几何白名单校验
  // data-shape 值必须是 pptxgenjs 支持的预设形状名;非法值会导致 addShape 报错
  const PRESET_SHAPES = new Set([
    "rect", "roundRect", "ellipse", "triangle", "rtTriangle", "diamond", "parallelogram",
    "trapezoid", "pentagon", "hexagon", "heptagon", "octagon", "decagon", "dodecagon",
    "pie", "chord", "teardrop", "frame", "halfFrame", "corner", "brackets", "brace",
    "leftArrow", "rightArrow", "upArrow", "downArrow", "stripedRightArrow", "notchedRightArrow",
    "bentArrow", "quadArrow", "leftRightArrow", "upDownArrow", "leftRightUpArrow",
    "quadArrowCallout", "bentArrowCallout", "chevron", "circularArrow", "homePlate",
    "curvedRightArrow", "curvedLeftArrow", "curvedUpArrow", "curvedDownArrow", "swooshArrow",
    "cube", "can", "lightningBolt", "heart", "sun", "moon", "smileyFace", "cloud",
    "star5", "star6", "star7", "star8", "star10", "star12", "star16", "star24", "star32",
    "plus", "minus", "multiply", "divide", "equals",
    "flowchartProcess", "flowchartDecision", "flowchartTerminator", "flowchartInput",
    "flowchartOutput", "flowchartPredefined", "flowchartDocument", "flowchartManualInput",
    "flowchartManualOperation", "flowchartConnector", "flowchartPreparation",
    "flowchartInternalStorage", "flowchartSort", "flowchartExtract", "flowchartMerge",
    "flowchartOr", "flowchartPunchedCard", "flowchartSummingJunction", "flowchartCollate",
    "flowchartStoredData", "flowchartDelay", "flowchartDisplay", "flowchartOffPageConnector",
    "flowchartMagneticDisk", "flowchartDirectAccessStorage", "flowchartSequentialAccess",
    "actionButtonBlank", "actionButtonHome", "actionButtonHelp", "actionButtonInformation",
    "actionButtonForwardNext", "actionButtonBackPrevious", "actionButtonEnd",
    "actionButtonBeginning", "actionButtonReturn", "actionButtonDocument",
  ]);
  document.querySelectorAll(".slide-container [data-shape]").forEach((el) => {
    const v = el.getAttribute("data-shape");
    if (!PRESET_SHAPES.has(v))
      issues.push({ level: "ERROR", msg: `data-shape="${v}" 不是 pptxgenjs 支持的预设形状名`, fix: "查 html-spec.md 5.4 节预设形状表,改用合法形状名(如 triangle/rightArrow/chevron/diamond)" });
  });

  // ══ 设计质量检查(2026-08-02 重构 D 期)══
  // 仅在 slides.config.json 配置 design.tier 后启用;未配置 = 全部休眠(旧项目零新增 WARN)
  const design = canvas.design || {};
  const tierOn = !!design.tier;

  // 12) 文字适配:仅查"作者固定高度"的盒子(inline style.height;方式 B/C 解析后也会写入 inline)。
  //    自动高度的 textbox 在浏览器里随内容生长,无溢出语义;CJK 字形超出 line-height 盒是常态(度量差),
  //    若对自动高度盒也查会系统性误报(封面大标题盒是典型)。
  //    溢出用 scrollHeight;欠载用"内容实际底边"(子级矩形/文本 Range 推算,绕开 scrollHeight 下界钳制)
  if (tierOn) {
    const contentBottomOf = (el, elTop) => {
      let bottom = 0;
      const push = (b) => { if (b > bottom) bottom = b; };
      Array.from(el.childNodes).forEach((n) => {
        if (n.nodeType === 1) {
          const r = n.getBoundingClientRect();
          if (r.height >= 1) push(r.bottom - elTop);
        } else if (n.nodeType === 3 && n.textContent.trim() !== "") {
          const range = document.createRange();
          range.selectNodeContents(n);
          const r = range.getBoundingClientRect();
          if (r.height >= 1) push(r.bottom - elTop);
        }
      });
      return bottom;
    };
    document.querySelectorAll('[data-object="true"]').forEach((el) => {
      const cs = getComputedStyle(el);
      if (cs.display === "none" || cs.visibility === "hidden") return;
      if (!el.style || !el.style.height) return; // 仅固定高度盒
      const text = (el.textContent || "").trim();
      if (!text) return;
      if (el.querySelector("table")) return; // 表格高度自适应,跳过
      const sh = el.scrollHeight, ch = el.clientHeight;
      if (ch < 10) return;
      // 溢出余量随字号缩放:CJK 字形超出 line-height 盒 ≈ 字号的 10-12%
      let maxFs = parseFloat(cs.fontSize) || 16;
      el.querySelectorAll("*").forEach((d) => {
        const f = parseFloat(getComputedStyle(d).fontSize) || 0;
        if (f > maxFs) maxFs = f;
      });
      const tolerance = Math.max(8, maxFs * 0.12);
      if (sh > ch + tolerance)
        issues.push({ level: "WARN", msg: `文字可能溢出容器(内容高约 ${Math.round(sh)}px > 盒高 ${Math.round(ch)}px): "${text.slice(0, 18)}"`, fix: "加高容器/减字/放大盒宽;PPT 端不会自动缩字" });
      else if (el.getAttribute("data-object-type") === "textbox" && ch >= 120) {
        const contentH = contentBottomOf(el, el.getBoundingClientRect().top);
        if (contentH > 0 && contentH < ch * 0.55)
          issues.push({ level: "WARN", msg: `文字欠载(内容高约 ${Math.round(contentH)}px < 盒高 ${Math.round(ch)}px 的 55%): "${text.slice(0, 18)}"`, fix: "放大字号/行距撑满(scale-to-fill),或收小盒高" });
      }
    });
  }

  // 13) 字号下限:绝对下限(默认 14px)+ 档内正文下限(启发:>20 字视为正文;
  //    底部注释区(top ≥ 840)且字号 ≥ 档内注释下限 → 豁免,那是来源标注不是正文)
  if (tierOn) {
    const TIER_BODY_MIN = { presentation: 22, mixed: 18, reading: 16 };
    const TIER_NOTE_MIN = { presentation: 16, mixed: 15, reading: 14 };
    const bodyMin = TIER_BODY_MIN[design.tier] || 16;
    const noteMin = TIER_NOTE_MIN[design.tier] || 14;
    const floor = design.minBodyPx || 14;
    document.querySelectorAll(".slide-container *").forEach((el) => {
      const hasDirectText = Array.from(el.childNodes).some((n) => n.nodeType === 3 && n.textContent.trim() !== "");
      if (!hasDirectText) return;
      const cs = getComputedStyle(el);
      if (cs.display === "none" || cs.visibility === "hidden") return;
      const fs = parseFloat(cs.fontSize) || 16;
      const text = (el.textContent || "").trim();
      if (fs < floor - 0.01)
        issues.push({ level: "WARN", msg: `字号 ${fs}px 低于绝对下限 ${floor}px: "${text.slice(0, 18)}"`, fix: "任何文字(含页码/来源标注)不得小于绝对下限" });
      else if (fs < bodyMin - 0.01 && text.length > 20) {
        const elTop = el.getBoundingClientRect().top - base.top;
        if (fs >= noteMin - 0.01 && elTop >= 840) return; // 底部注释区豁免
        issues.push({ level: "WARN", msg: `正文疑似过小:${fs}px 低于 ${design.tier} 档正文下限 ${bodyMin}px: "${text.slice(0, 18)}"`, fix: "升字号到档内区间;若它不是正文(标签/注释),精简到 20 字内" });
      }
    });
  }

  // 14) 画布填充:内容带底边过低且非 airy 页 → 底部留白过大
  // 页脚区(top ≥ 980)元素不计入内容带;airy 豁免:配置 airyPages / 深底页 / 超大字少元素页
  if (tierOn && !canvas.airy) {
    let maxBottom = 0, maxFs = 0, textObjCount = 0;
    document.querySelectorAll('[data-object="true"]').forEach((el) => {
      const cs = getComputedStyle(el);
      if (cs.display === "none" || cs.visibility === "hidden") return;
      const r = el.getBoundingClientRect();
      if (r.width < 2 || r.height < 2) return;
      if (r.top - base.top >= 980) return; // 页脚区不计
      const relBottom = r.bottom - base.top;
      if (relBottom <= canvasH + 2) maxBottom = Math.max(maxBottom, relBottom);
      if ((el.textContent || "").trim()) {
        textObjCount++;
        maxFs = Math.max(maxFs, parseFloat(cs.fontSize) || 0);
      }
    });
    const bgm = /rgba?\(([^)]+)\)/.exec(ccs.backgroundColor || "");
    let dark = false;
    if (bgm) {
      const ch = bgm[1].split(",").map((v) => parseFloat(v));
      dark = (0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]) / 255 < 0.35;
    }
    const airyHeuristic = dark || (maxFs >= 64 && textObjCount <= 5);
    const fillLine = 320 + 620 * (design.fillThreshold || 0.85);
    if (!airyHeuristic && maxBottom > 0 && maxBottom < fillLine)
      issues.push({ level: "WARN", msg: `内容底边 ${Math.round(maxBottom)}px,底部留白过大(内容区 ${Math.round(fillLine)}px 线未达)`, fix: "放大字号/行距撑满(scale-to-fill),或检查是否漏排内容;若为 airy 页(封面/分隔/大字/引用),把文件名加入 design.airyPages" });
  }
  return issues;
}

module.exports = { domChecks };
