// 生成指定来源的索引文件（index/<source>.json），并更新 README.md 中对应的统计区。
// 用法: node scripts/build-index.mjs <clawhub|skills-sh|hermes>
// 设计为按源独立运行，配合三个并行 workflow job，互不冲突。
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const source = process.argv[2];
if (!source) {
  console.error("用法: node scripts/build-index.mjs <clawhub|skills-sh|hermes>");
  process.exit(1);
}

function walkSkills(sourceDir) {
  const entries = [];
  if (!fs.existsSync(sourceDir)) return entries;
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
  entries.sort((a, b) => a.id.localeCompare(b.id));
  return entries;
}

function updateReadme(blockName, lines) {
  const readmePath = path.join(ROOT, "README.md");
  let readme = fs.readFileSync(readmePath, "utf8");
  const start = `<!-- INDEX:${blockName}:START -->`;
  const end = `<!-- INDEX:${blockName}:END -->`;
  const block = `${start}\n${lines}\n${end}`;
  if (readme.includes(start)) {
    readme = readme.replace(new RegExp(`${start.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}[\\s\\S]*?${end.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}`), block);
  } else {
    readme += `\n${block}\n`;
  }
  fs.writeFileSync(readmePath, readme);
}

function main() {
  const generatedAt = new Date().toISOString();
  fs.mkdirSync(path.join(ROOT, "index"), { recursive: true });

  if (source === "hermes") {
    // Hermes 只镜像元数据索引，统计直接读 _meta.json
    const metaFile = path.join(ROOT, "skills", "hermes", "_index", "_meta.json");
    if (!fs.existsSync(metaFile)) {
      console.log("[index] hermes 尚未同步，跳过");
      return;
    }
    const meta = JSON.parse(fs.readFileSync(metaFile, "utf8"));
    const index = { generatedAt, source, skillCount: meta.skill_count, upstreamGeneratedAt: meta.generated_at, bySource: meta.bySource };
    fs.writeFileSync(path.join(ROOT, "index", "hermes.json"), JSON.stringify(index, null, 2) + "\n");
    const lines = [
      `最后同步：${generatedAt}（上游索引生成于 ${meta.generated_at}）`,
      "",
      "| 上游来源 | skill 数（仅元数据） |",
      "|---|---|",
      ...Object.entries(meta.bySource || {}).map(([s, n]) => `| ${s} | ${n} |`),
      "",
      "明细见 `skills/hermes/_index/`。",
    ].join("\n");
    updateReadme(source, lines);
    console.log(`[index] index/hermes.json: ${meta.skill_count} 个 skill（仅元数据）`);
    return;
  }

  const entries = walkSkills(path.join(ROOT, "skills", source));
  const index = { generatedAt, source, total: entries.length, skills: entries };
  fs.writeFileSync(path.join(ROOT, "index", `${source}.json`), JSON.stringify(index, null, 2) + "\n");
  const lines = [`最后同步：${generatedAt}`, "", `已镜像完整内容：**${entries.length}** 个 skill，明细见 \`index/${source}.json\` 与 \`skills/${source}/\`。`].join("\n");
  updateReadme(source, lines);
  console.log(`[index] index/${source}.json: ${entries.length} 个已镜像 skill`);
}

main();
