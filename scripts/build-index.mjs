// 扫描 skills/ 目录，生成 INDEX.json，并更新 README.md 中的统计区。
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const SKILLS_DIR = path.join(ROOT, "skills");

function walkSkills() {
  const entries = [];
  if (!fs.existsSync(SKILLS_DIR)) return entries;
  for (const source of fs.readdirSync(SKILLS_DIR)) {
    const sourceDir = path.join(SKILLS_DIR, source);
    if (!fs.statSync(sourceDir).isDirectory()) continue;
    for (const id of fs.readdirSync(sourceDir)) {
      const dir = path.join(sourceDir, id);
      if (!fs.statSync(dir).isDirectory()) continue;
      let meta = null;
      try {
        meta = JSON.parse(fs.readFileSync(path.join(dir, ".upstream.json"), "utf8"));
      } catch {
        continue;
      }
      entries.push({
        id: `${source}/${id}`,
        source,
        url: meta.url || null,
        version: meta.version || null,
        contentHash: meta.contentHash || null,
        fetchedAt: meta.fetchedAt || null,
      });
    }
  }
  entries.sort((a, b) => a.id.localeCompare(b.id));
  return entries;
}

function hermesIndexStats() {
  const metaFile = path.join(SKILLS_DIR, "hermes", "_index", "_meta.json");
  if (!fs.existsSync(metaFile)) return null;
  try {
    return JSON.parse(fs.readFileSync(metaFile, "utf8"));
  } catch {
    return null;
  }
}

function main() {
  const entries = walkSkills();
  const bySource = {};
  for (const e of entries) bySource[e.source] = (bySource[e.source] || 0) + 1;

  const index = {
    generatedAt: new Date().toISOString(),
    totalMirrored: entries.length,
    bySource,
    skills: entries,
  };
  fs.writeFileSync(path.join(ROOT, "INDEX.json"), JSON.stringify(index, null, 2) + "\n");
  console.log(`[index] INDEX.json: ${entries.length} 个已镜像 skill`, bySource);

  // README 统计区
  const readmePath = path.join(ROOT, "README.md");
  let readme = fs.readFileSync(readmePath, "utf8");
  const hermes = hermesIndexStats();
  const lines = [
    `最后同步：${index.generatedAt}`,
    "",
    "| 来源 | 已镜像（完整内容） |",
    "|---|---|",
    ...Object.entries(bySource)
      .sort()
      .map(([s, n]) => `| ${s} | ${n} |`),
    "",
    hermes
      ? `Hermes 聚合索引（仅元数据）：${hermes.skill_count} 个 skill，索引生成于 ${hermes.generated_at}，见 \`skills/hermes/_index/\`。`
      : "Hermes 聚合索引：尚未同步。",
  ].join("\n");
  const block = `<!-- INDEX:START -->\n${lines}\n<!-- INDEX:END -->`;
  if (readme.includes("<!-- INDEX:START -->")) {
    readme = readme.replace(/<!-- INDEX:START -->[\s\S]*?<!-- INDEX:END -->/, block);
  } else {
    readme += `\n## 索引统计\n\n${block}\n`;
  }
  fs.writeFileSync(readmePath, readme);
  console.log("[index] README.md 统计区已更新");
}

main();
