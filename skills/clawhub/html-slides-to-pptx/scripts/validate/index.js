// validate/index.js — CLI 编排:静态检查 + 浏览器 DOM 检查
// 退出码:有 ERROR → 1,否则 0(WARN 不阻断);用法错误 → 2
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");
const { staticChecks } = require("./static-checks.js");
const { domChecks } = require("./dom-checks.js");
const { layoutChecks } = require("./layout-checks.js");
const { formStats } = require("./form-stats.js");
const { injectScripts, LAYOUT_SCRIPTS } = require("../core/inject.js");
const { gotoSettled } = require("../core/browser.js");
const DEFAULT_CONFIG = require("../config/default.config.js");
const { resolveConfig } = require("../config/merge.js");

// 画布尺寸从配置取(唯一事实源);项目级 slides.config.json 与 convert 共用同一加载规则
let CANVAS_W = DEFAULT_CONFIG.canvas.width, CANVAS_H = DEFAULT_CONFIG.canvas.height;

function collectHtmlFiles(args) {
  const files = [];
  for (const a of args) {
    if (!fs.existsSync(a)) continue;
    const stat = fs.statSync(a);
    if (stat.isDirectory()) {
      for (const f of fs.readdirSync(a)) {
        if (f.endsWith(".html") && !path.basename(f).startsWith("_"))
          files.push(path.join(a, f));
      }
    } else if (a.endsWith(".html")) files.push(a);
  }
  return files;
}

// 项目级配置:目录参数取目录内 slides.config.json;文件参数取其父目录
// 无配置 → undefined → 走 default.config.js 的 design 缺省档(2026-08-06 起 = presentation
// + balanced,设计检查默认开启)。需要休眠的项目显式写 design:{tier:"",formProfile:""}。
function loadProjectOverrides(args) {
  const candidates = [];
  for (const a of args) {
    if (!fs.existsSync(a)) continue;
    const stat = fs.statSync(a);
    if (stat.isDirectory()) candidates.push(path.join(a, "slides.config.json"));
    else candidates.push(path.join(path.dirname(path.resolve(a)), "slides.config.json"));
  }
  for (const c of candidates) {
    if (fs.existsSync(c)) {
      try {
        return JSON.parse(fs.readFileSync(c, "utf-8"));
      } catch (e) {
        throw new Error(`slides.config.json 解析失败: ${e.message}`);
      }
    }
  }
  return undefined;
}

async function run(args) {
  if (!args.length) {
    console.error("用法: node validate.js <html文件...|目录>");
    process.exit(2);
  }
  const files = collectHtmlFiles(args);
  if (!files.length) {
    console.error("未找到 HTML 文件");
    process.exit(2);
  }

  const overrides = loadProjectOverrides(args);
  const CONFIG = resolveConfig(overrides || {});
  CANVAS_W = CONFIG.canvas.width;
  CANVAS_H = CONFIG.canvas.height;
  const DESIGN = CONFIG.design || { tier: "" };
  const designOn = !!DESIGN.tier;

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: CANVAS_W, height: CANVAS_H } });
  let errCount = 0, warnCount = 0;
  const pageStats = []; // 逐页视觉形式统计(deck 级形式检查用;2026-08-05)

  for (const file of files) {
    const src = fs.readFileSync(file, "utf-8");
    let issues = staticChecks(file, src);
    const isAiryPage = (DESIGN.airyPages || []).includes(path.basename(file));
    // hedgePages(2026-08-06 第六轮 P4):该页承载"反向验证未通过"的降级论断 →
    // 必须出现限定词。口径与 airyPages 同款(文件名精确匹配)。
    const needsHedge = (DESIGN.hedgePages || []).includes(path.basename(file));
    try {
      await gotoSettled(page, "file://" + path.resolve(file));
      // data-layout 先校验后解析(与 convert 注入同一批文件):
      // 有 ERROR 时不改写 DOM,让后续检查看到作者原始写法;无 ERROR 时解析后再查,避免误报
      await injectScripts(page, LAYOUT_SCRIPTS);
      const dlIssues = await page.evaluate(() => window.__htmlSlides.layout.validateAll(document));
      if (!dlIssues.some((i) => i.level === "ERROR"))
        await page.evaluate(() => window.__htmlSlides.layout.resolveAll(document));
      issues = issues.concat(
        dlIssues,
        await page.evaluate(domChecks, {
          w: CANVAS_W,
          h: CANVAS_H,
          design: DESIGN,
          airy: isAiryPage,
        }),
        await page.evaluate(layoutChecks, { design: DESIGN, needsHedge })
      );
      pageStats.push({ file: path.basename(file), ...(await page.evaluate(formStats, { airy: isAiryPage })) });
    } catch (e) {
      issues.push({ level: "ERROR", msg: "页面加载失败: " + e.message, fix: "检查 HTML 是否完整" });
    }
    issues.sort((a, b) => (a.level === b.level ? (a.line || 0) - (b.line || 0) : a.level === "ERROR" ? -1 : 1));
    const errs = issues.filter((i) => i.level === "ERROR");
    errCount += errs.length;
    warnCount += issues.length - errs.length;

    console.log(`\n=== ${path.basename(file)} ===`);
    if (!issues.length) console.log("  ✅ 无违规");
    for (const i of issues) {
      const loc = i.line ? `L${i.line} ` : "";
      console.log(`  ${i.level === "ERROR" ? "❌" : "⚠️ "} ${i.level} ${loc}${i.msg}`);
      if (i.fix) console.log(`     → 修复: ${i.fix}`);
    }
  }
  await browser.close();

  // ══ deck 级视觉形式检查(2026-08-05 第三轮重构;design.formProfile 驱动)══
  // 缺省 balanced(2026-08-06 起默认开启);显式 ""/text = 休眠。口径见 design-principles 第五章。
  // 阈值取自 config/default.config.js 的 design.thresholds.formLimits(唯一事实源,2026-08-06 P2)
  // 不设字面量兜底 —— 配置表恒有此键,写兜底等于又开一份事实源(threshold-parity.js 会拦)。
  const TH = DESIGN.thresholds || {};
  const FORM_LIMITS = TH.formLimits || {};
  const FORM_LABEL = { text: "文字", diagram: "图示", chart: "图表", image: "图片", mixed: "混合" };
  const formLimit = FORM_LIMITS[DESIGN.formProfile || ""];
  if (formLimit && pageStats.length) {
    const deckIssues = [];
    const content = pageStats.filter((p) => !p.airy);
    const textOnly = content.filter((p) => p.form === "text");
    const ratio = content.length ? textOnly.length / content.length : 0;
    if (content.length >= (TH.formMinPages || 4) && ratio > formLimit.ratio + 1e-9)
      deckIssues.push({
        msg: `纯文字内容页占比过高:${textOnly.length}/${content.length}(${Math.round(ratio * 100)}%)超过 ${DESIGN.formProfile} 档上限 ${formLimit.ratio * 100}%`,
        fix: "把 1-2 页并列/流程/分层/对比内容换图示原型(23 图标网格/24 chevron/26 金字塔/29 对比卡阵)——换形式,不换内容",
      });
    // 同形式连排(airy 页破连排;超过上限时报一次)
    let run = 1;
    for (let i = 1; i < pageStats.length; i++) {
      if (pageStats[i].airy) { run = 0; continue; }
      if (pageStats[i - 1].airy) { run = 1; continue; }
      if (pageStats[i].form === pageStats[i - 1].form) {
        run++;
        if (run === formLimit.streak + 1)
          deckIssues.push({
            msg: `同形式连排:${pageStats[i - run + 1].file} 起连续 ${run} 页均为「${FORM_LABEL[pageStats[i].form]}」型`,
            fix: "中间页换一种形式(并列→23/先后→24/递减→25/分层→26/循环→27/辐射→28/对比→29/分节→30)",
          });
      } else run = 1;
    }
    if (deckIssues.length) {
      console.log(`\n=== deck 视觉形式检查(formProfile: ${DESIGN.formProfile})===`);
      for (const d of deckIssues) {
        console.log(`  ⚠️  WARN ${d.msg}`);
        if (d.fix) console.log(`     → 修复: ${d.fix}`);
      }
      warnCount += deckIssues.length;
    }
  }
  console.log(`\n──────────────────────────────`);
  console.log(`共 ${files.length} 个文件: ${errCount} 个 ERROR, ${warnCount} 个 WARN${designOn ? `(design profile: ${DESIGN.tier})` : ""}`);
  process.exit(errCount > 0 ? 1 : 0);
}

module.exports = { run };
