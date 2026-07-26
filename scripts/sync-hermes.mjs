// 同步 Hermes Agent 聚合索引（hermes-agent.nousresearch.com）。
// 数据源: https://hermes-agent.nousresearch.com/docs/api/skills-index.json（约 35MB，每日两次重建）
// 两个阶段：
//   1) 索引镜像：全量索引按 source 拆分成独立 JSON（skills/hermes/_index/），保证 PR diff 可审查。
//   2) 内容镜像：索引中带 repo+path 的条目（official / github 等来源），从 GitHub 拉取完整
//      skill 内容到 skills/hermes/<id>/。clawhub / skills.sh 来源的条目内容由各自 syncer 覆盖，不在此重复。
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { fetchJson, createLimiter } from "./lib/http.mjs";
import { loadState, saveState } from "./lib/state.mjs";
import { writeSkill, removeSkill, collectFiles, contentHash } from "./lib/writer.mjs";
import { getRepoInfo, fetchRepoDir } from "./lib/github.mjs";
import { SyncStats } from "./lib/summary.mjs";
import { MAX_ITEMS, CONCURRENCY, safeName } from "./lib/config.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const SOURCE = "hermes";
const INDEX_URL = "https://hermes-agent.nousresearch.com/docs/api/skills-index.json";
const TOKEN = process.env.GITHUB_TOKEN || "";

// 索引镜像：全量拉取，按来源拆分写入 skills/hermes/_index/
async function syncIndex(data, state, stats) {
  if (state.generatedAt === data.generated_at) {
    console.log("[hermes] 索引未变化，跳过索引重写");
    return;
  }
  const outDir = path.join(ROOT, "skills", SOURCE, "_index");
  fs.rmSync(outDir, { recursive: true, force: true });
  fs.mkdirSync(outDir, { recursive: true });

  // 按来源分组（identifier 排序保证 diff 稳定）
  const groups = new Map();
  for (const s of data.skills) {
    const key = s.source || "unknown";
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(s);
  }

  // meta 文件（含各来源计数，供 build-index 直接使用）
  const meta = {
    source: SOURCE,
    url: INDEX_URL,
    version: data.version,
    generated_at: data.generated_at,
    skill_count: data.skill_count,
    bySource: Object.fromEntries([...groups.entries()].sort().map(([k, v]) => [k, v.length])),
    fetchedAt: new Date().toISOString(),
  };
  fs.writeFileSync(path.join(outDir, "_meta.json"), JSON.stringify(meta, null, 2) + "\n");

  for (const [source, list] of [...groups.entries()].sort()) {
    list.sort((a, b) => String(a.identifier).localeCompare(String(b.identifier)));
    fs.writeFileSync(path.join(outDir, `${safeName(source)}.json`), JSON.stringify(list, null, 2) + "\n");
    console.log(`[hermes]   ${source}: ${list.length}`);
  }
  stats.added += data.skills.length; // 索引整体替换，统一计为新增/更新
}

// clawhub / skills.sh 来源的条目由各自 syncer 覆盖，不在此重复拉取
const COVERED_SOURCES = new Set(["clawhub", "skills.sh", "skills-sh"]);

// 内容镜像：带 repo+path 的条目从 GitHub 拉完整内容
async function syncContent(data, state, stats) {
  const wanted = new Map(); // id -> {identifier, repo, path, name}
  for (const s of data.skills) {
    if (!s.repo || !s.path || COVERED_SOURCES.has(s.source)) continue;
    const id = safeName(String(s.identifier).replace(/\//g, "--"));
    wanted.set(id, { identifier: s.identifier, repo: s.repo, path: s.path, name: s.name });
  }
  console.log(`[hermes] 索引中可拉取内容的条目: ${wanted.size} 个`);

  // 下架删除
  for (const [id, meta] of Object.entries(state.content)) {
    if (!wanted.has(id)) {
      if (removeSkill(ROOT, SOURCE, id)) {
        delete state.content[id];
        stats.removed++;
        console.log(`[hermes] 删除已下架: ${id}`);
      }
    }
  }

  // 按仓库分组，新仓库优先
  const byRepo = new Map();
  for (const [id, w] of wanted) {
    if (!byRepo.has(w.repo)) byRepo.set(w.repo, []);
    byRepo.get(w.repo).push({ id, ...w });
  }
  const repoKeys = [...byRepo.keys()].sort(
    (a, b) => Number(state.repos[a] != null) - Number(state.repos[b] != null)
  );
  console.log(`[hermes] 涉及 ${repoKeys.length} 个仓库`);

  let fetched = 0;
  let stopped = false;
  const limit = createLimiter(CONCURRENCY);
  await Promise.all(
    repoKeys.map((key) =>
      limit(async () => {
        if (stopped) return;
        const entries = byRepo.get(key);
        try {
          const { pushedAt, branch } = await getRepoInfo(key);
          // 仓库无变化且这批条目都处理过 → 跳过
          if (
            state.repos[key]?.pushedAt === pushedAt &&
            entries.every((e) => state.repos[key].ids?.includes(e.id))
          ) {
            entries.forEach((e) => state.content[e.id] && stats.record("unchanged"));
            return;
          }
          const { dir: repoDir, cleanup } = await fetchRepoDir(key, branch);
          fetched += entries.length;
          if (fetched >= MAX_ITEMS) stopped = true;
          try {
            for (const e of entries) {
              const subDir = path.join(repoDir, e.path);
              if (!fs.existsSync(subDir) || !fs.statSync(subDir).isDirectory()) {
                stats.fail(e.id, new Error(`仓库中未找到路径 ${e.path}`));
                continue;
              }
              const files = collectFiles(subDir);
              const result = writeSkill(ROOT, SOURCE, e.id, files, {
                source: SOURCE,
                url: `https://github.com/${key}/tree/${branch}/${e.path}`,
                identifier: e.identifier,
                repo: key,
                path: e.path,
                branch,
                pushedAt,
              });
              stats.record(result);
              state.content[e.id] = { repo: key, path: e.path, pushedAt, contentHash: contentHash(files) };
            }
            state.repos[key] = { defaultBranch: branch, pushedAt, ids: entries.map((e) => e.id) };
          } finally {
            cleanup();
          }
        } catch (e) {
          if (e.status === 404) {
            for (const en of entries) {
              if (removeSkill(ROOT, SOURCE, en.id)) {
                delete state.content[en.id];
                stats.removed++;
              }
            }
            delete state.repos[key];
            console.log(`[hermes] 仓库 404，移除其 skill: ${key}`);
          } else {
            for (const en of entries) stats.fail(en.id, e);
          }
        }
      })
    )
  );
}

async function main() {
  if (!TOKEN) console.warn("[hermes] 未设置 GITHUB_TOKEN，GitHub API 限流 60 次/小时，仅适合小批量试跑");
  const state = loadState(ROOT, SOURCE);
  state.repos ??= {};
  state.content ??= {};
  const stats = new SyncStats(SOURCE);

  console.log("[hermes] 下载聚合索引…");
  const data = await fetchJson(INDEX_URL, { timeoutMs: 300_000 });
  if (!data || !Array.isArray(data.skills)) throw new Error("索引格式异常：缺少 skills 数组");
  console.log(`[hermes] 索引生成于 ${data.generated_at}，共 ${data.skills.length} 个 skill`);

  await syncIndex(data, state, stats);
  await syncContent(data, state, stats);

  state.generatedAt = data.generated_at;
  state.skillCount = data.skill_count;
  saveState(ROOT, SOURCE, state);
  stats.report();
  if (stats.failed > 50 && stats.failed > (stats.added + stats.updated + stats.unchanged) * 0.2) {
    process.exitCode = 1;
  }
}

main().catch((e) => {
  console.error(`[hermes] 同步失败:`, e);
  process.exit(1);
});
