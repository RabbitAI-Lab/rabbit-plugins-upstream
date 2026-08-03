// preview.js — 视觉自查截图:把 slides/*.html 逐页截图为 PNG,供写页后人工/AI 自查
// 用法: node preview.js <slides目录> [--only <子串>]
// 产物: <slides目录>/.preview/<页名>.png(已 gitignore 建议);重跑覆盖同名文件
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");
const { gotoSettled } = require("./core/browser.js");
const { injectScripts, LAYOUT_SCRIPTS } = require("./core/inject.js");
const DEFAULT_CONFIG = require("./config/default.config.js");

(async () => {
  const args = process.argv.slice(2);
  const dir = args.find((a) => !a.startsWith("--"));
  const onlyIdx = args.indexOf("--only");
  const only = onlyIdx >= 0 ? args[onlyIdx + 1] : null;
  if (!dir || !fs.existsSync(dir)) {
    console.error("用法: node preview.js <slides目录> [--only <子串>]");
    process.exit(2);
  }
  const files = fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".html") && !f.startsWith("_") && (!only || f.includes(only)))
    .sort();
  if (!files.length) {
    console.error("未找到 HTML 文件");
    process.exit(2);
  }
  const outDir = path.join(dir, ".preview");
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: DEFAULT_CONFIG.viewport.width, height: DEFAULT_CONFIG.viewport.height },
  });
  for (const f of files) {
    const fp = path.resolve(dir, f);
    await gotoSettled(page, "file://" + fp);
    // 等 webfont 就绪(与 pipeline 一致,避免字体未到的截图误导判断)
    await Promise.race([
      page.evaluate(() => (document.fonts && document.fonts.ready ? document.fonts.ready.then(() => true) : true)),
      page.waitForTimeout(2000),
    ]);
    await page.waitForTimeout(DEFAULT_CONFIG.settleMs);
    // 方式 C(data-layout)页面必须先解析再截图:与 convert/validate 同一批布局脚本,
    // 否则 columns/grid/stack 子级未定位,截图呈现为纵向堆叠(假布局事故)
    await injectScripts(page, LAYOUT_SCRIPTS);
    await page.evaluate(() => window.__htmlSlides.layout.resolveAll(document));
    const out = path.join(outDir, f.replace(/\.html$/, ".png"));
    await page.screenshot({ path: out });
    console.log(`  📸 ${path.relative(process.cwd(), out)}`);
  }
  await browser.close();
  console.log(`\n共 ${files.length} 张 → ${outDir}\n逐张看图自查:填充率/字号/对齐/去 AI 味(见 SKILL.md Step 3.5)`);
})().catch((e) => {
  console.error("preview 失败:", e.message);
  process.exit(1);
});
