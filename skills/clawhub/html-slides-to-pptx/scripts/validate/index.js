// validate/index.js — CLI 编排:静态检查 + 浏览器 DOM 检查
// 退出码:有 ERROR → 1,否则 0(WARN 不阻断);用法错误 → 2
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");
const { staticChecks } = require("./static-checks.js");
const { domChecks } = require("./dom-checks.js");
const { layoutChecks } = require("./layout-checks.js");
const { injectScripts, LAYOUT_SCRIPTS } = require("../core/inject.js");
const { gotoSettled } = require("../core/browser.js");
const DEFAULT_CONFIG = require("../config/default.config.js");

// 画布尺寸从默认配置取(唯一事实源);项目级覆盖只影响 convert,validate 始终按默认画布断言
const CANVAS_W = DEFAULT_CONFIG.canvas.width, CANVAS_H = DEFAULT_CONFIG.canvas.height;

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

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: CANVAS_W, height: CANVAS_H } });
  let errCount = 0, warnCount = 0;

  for (const file of files) {
    const src = fs.readFileSync(file, "utf-8");
    let issues = staticChecks(file, src);
    try {
      await gotoSettled(page, "file://" + path.resolve(file));
      // data-layout 先校验后解析(与 convert 注入同一批文件):
      // 有 ERROR 时不改写 DOM,让后续检查看到作者原始写法;无 ERROR 时解析后再查,避免误报
      await injectScripts(page, LAYOUT_SCRIPTS);
      const dlIssues = await page.evaluate(() => window.__htmlSlides.layout.validateAll(document));
      if (!dlIssues.some((i) => i.level === "ERROR"))
        await page.evaluate(() => window.__htmlSlides.layout.resolveAll(document));
      issues = issues.concat(dlIssues, await page.evaluate(domChecks, { w: CANVAS_W, h: CANVAS_H }), await page.evaluate(layoutChecks));
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
  console.log(`\n──────────────────────────────`);
  console.log(`共 ${files.length} 个文件: ${errCount} 个 ERROR, ${warnCount} 个 WARN`);
  process.exit(errCount > 0 ? 1 : 0);
}

module.exports = { run };
