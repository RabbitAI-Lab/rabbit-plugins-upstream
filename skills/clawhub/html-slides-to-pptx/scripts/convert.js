// convert.js — 薄 CLI:参数解析 → (可选)项目级配置 → core/pipeline
// 用法: node convert.js ./slides ./slides/playlist.json out.pptx
// 项目级覆盖:在 playlist 同级目录放 slides.config.json(键见 config/default.config.js,未知键报错)
const fs = require("fs");
const path = require("path");
const { convert } = require("./core/pipeline.js");

function loadProjectConfig(playlistFile) {
  const cfgPath = path.join(path.dirname(path.resolve(playlistFile)), "slides.config.json");
  if (!fs.existsSync(cfgPath)) return undefined;
  let parsed;
  try {
    parsed = JSON.parse(fs.readFileSync(cfgPath, "utf-8"));
  } catch (e) {
    throw new Error(`slides.config.json 解析失败: ${e.message}`);
  }
  if (parsed === null || typeof parsed !== "object" || Array.isArray(parsed))
    throw new Error("slides.config.json 必须是 JSON 对象(键见 config/default.config.js)");
  return parsed;
}

(async () => {
  const [, , baseDir, playlistFile, outFile = "out.pptx"] = process.argv;
  if (!baseDir || !playlistFile) {
    console.error("用法: node convert.js <slides目录> <playlist.json> [输出.pptx]");
    process.exit(2);
  }
  const overrides = loadProjectConfig(playlistFile);
  await convert(baseDir, playlistFile, outFile, overrides);
})().catch((e) => {
  console.error(e.message || e);
  process.exit(1);
});
