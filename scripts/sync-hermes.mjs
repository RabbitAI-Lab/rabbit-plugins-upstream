// 同步 Hermes Agent 聚合索引（hermes-agent.nousresearch.com）。
// 数据源: https://hermes-agent.nousresearch.com/docs/api/skills-index.json（约 35MB，每日两次重建）
// Hermes 是聚合站（含 ClawHub / skills.sh / lobehub 等），此处只镜像其元数据索引，
// 按 source 拆分成独立 JSON 文件，保证 PR diff 可审查。
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { fetchJson } from "./lib/http.mjs";
import { loadState, saveState } from "./lib/state.mjs";
import { SyncStats } from "./lib/summary.mjs";
import { safeName } from "./lib/config.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const SOURCE = "hermes";
const INDEX_URL = "https://hermes-agent.nousresearch.com/docs/api/skills-index.json";

async function main() {
  const state = loadState(ROOT);
  state[SOURCE] ??= {};
  const stats = new SyncStats(SOURCE);

  console.log("[hermes] 下载聚合索引…");
  const data = await fetchJson(INDEX_URL, { timeoutMs: 300_000 });
  if (!data || !Array.isArray(data.skills)) throw new Error("索引格式异常：缺少 skills 数组");
  console.log(`[hermes] 索引生成于 ${data.generated_at}，共 ${data.skills.length} 个 skill`);

  if (state[SOURCE].generatedAt === data.generated_at) {
    console.log("[hermes] 索引未变化，跳过");
    stats.unchanged = data.skills.length;
    stats.report();
    return;
  }

  const outDir = path.join(ROOT, "skills", SOURCE, "_index");
  fs.rmSync(outDir, { recursive: true, force: true });
  fs.mkdirSync(outDir, { recursive: true });

  // meta 文件
  const meta = {
    source: SOURCE,
    url: INDEX_URL,
    version: data.version,
    generated_at: data.generated_at,
    skill_count: data.skill_count,
    fetchedAt: new Date().toISOString(),
  };
  fs.writeFileSync(path.join(outDir, "_meta.json"), JSON.stringify(meta, null, 2) + "\n");

  // 按来源拆分，identifier 排序保证 diff 稳定
  const groups = new Map();
  for (const s of data.skills) {
    const key = s.source || "unknown";
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(s);
  }
  for (const [source, list] of [...groups.entries()].sort()) {
    list.sort((a, b) => String(a.identifier).localeCompare(String(b.identifier)));
    fs.writeFileSync(path.join(outDir, `${safeName(source)}.json`), JSON.stringify(list, null, 2) + "\n");
    console.log(`[hermes]   ${source}: ${list.length}`);
  }

  stats.added = data.skills.length; // 索引整体替换，统一计为新增/更新
  state[SOURCE].generatedAt = data.generated_at;
  state[SOURCE].skillCount = data.skill_count;
  saveState(ROOT, state);
  stats.report();
}

main().catch((e) => {
  console.error(`[hermes] 同步失败:`, e);
  process.exit(1);
});
