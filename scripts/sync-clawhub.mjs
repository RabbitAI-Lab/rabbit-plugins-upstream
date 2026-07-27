// 同步 ClawHub (clawhub.ai) 全量 skills。
// 枚举: GET /api/v1/skills?limit=100&cursor=...（游标分页，含 version/updatedAt 用于增量判断）
// 下载: GET /api/v1/download?slug=<slug>[&ownerHandle=<owner>] → zip
// slug 跨 owner 撞名时按 <owner>--<slug> 分目录存储（通过 /api/v1/search 解析 owner 列表）。
import path from "node:path";
import { fileURLToPath } from "node:url";
import { fetchJson, fetchBuffer, createLimiter } from "./lib/http.mjs";
import { loadState, saveState } from "./lib/state.mjs";
import { writeSkill, removeSkill, contentHash } from "./lib/writer.mjs";
import { unzip } from "./lib/unzip.mjs";
import { SyncStats } from "./lib/summary.mjs";
import { MAX_ITEMS, CONCURRENCY, safeName } from "./lib/config.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const API = "https://clawhub.ai/api/v1";
const SOURCE = "clawhub";
// 镜像格式版本：写入/解析逻辑修复后递增，强制重下旧格式条目
const FORMAT = 2;

async function enumerateAll() {
  const maxPages = process.env.SYNC_ENUM_PAGES ? Number(process.env.SYNC_ENUM_PAGES) : Infinity; // 限页调试/每日增量模式
  const items = new Map(); // slug -> {version, updatedAt}
  let cursor = null;
  let page = 0;
  for (;;) {
    const url = `${API}/skills?limit=100` + (cursor ? `&cursor=${encodeURIComponent(cursor)}` : "");
    const data = await fetchJson(url, { timeoutMs: 120_000 });
    for (const it of data.items || []) {
      items.set(it.slug, {
        version: it.latestVersion?.version || null,
        updatedAt: it.updatedAt || null,
      });
    }
    page++;
    if (page % 20 === 0) console.log(`[clawhub] 已枚举 ${items.size} 个 skill（${page} 页）`);
    cursor = data.nextCursor;
    if (!cursor || !data.items?.length || page >= maxPages) break;
  }
  const truncated = page >= maxPages && cursor;
  if (truncated) console.warn(`[clawhub] 枚举被 SYNC_ENUM_PAGES=${maxPages} 截断（调试模式，跳过下架删除）`);
  return { items, truncated };
}

async function resolveOwners(slug) {
  const data = await fetchJson(`${API}/search?q=${encodeURIComponent(slug)}`);
  const owners = (data.results || []).filter((r) => r.slug === slug).map((r) => r.ownerHandle).filter(Boolean);
  return [...new Set(owners)];
}

async function downloadOne(slug, ownerHandle) {
  const qs = `slug=${encodeURIComponent(slug)}` + (ownerHandle ? `&ownerHandle=${encodeURIComponent(ownerHandle)}` : "");
  const buf = await fetchBuffer(`${API}/download?${qs}`, { timeoutMs: 180_000 });
  return unzip(buf);
}

async function main() {
  const state = loadState(ROOT, SOURCE);
  state.skills ??= {};
  const stored = state.skills;
  const stats = new SyncStats(SOURCE);

  console.log("[clawhub] 开始全量枚举…");
  const { items: upstream, truncated } = await enumerateAll();
  console.log(`[clawhub] 上游共 ${upstream.size} 个 skill`);

  // 1) 下架删除：state 中存在但上游枚举已没有该 slug（枚举被截断时跳过，防止误删）
  const upstreamSlugs = new Set(upstream.keys());
  if (!truncated) {
    for (const [id, meta] of Object.entries(stored)) {
      if (!upstreamSlugs.has(meta.slug)) {
        if (removeSkill(ROOT, SOURCE, id)) {
          delete stored[id];
          stats.removed++;
          console.log(`[clawhub] 删除已下架: ${id}`);
        }
      }
    }
  }

  // 2) 找出需要（重新）下载的 slug
  const bySlug = new Map(); // slug -> [state 里的 dirName]
  for (const [id, meta] of Object.entries(stored)) {
    (bySlug.get(meta.slug) ?? bySlug.set(meta.slug, []).get(meta.slug)).push(id);
  }
  const todo = [];
  for (const [slug, info] of upstream) {
    const existing = bySlug.get(slug) || [];
    const fresh =
      existing.length > 0 &&
      existing.every(
        (id) =>
          stored[id].format === FORMAT &&
          stored[id].version === info.version &&
          stored[id].updatedAt === info.updatedAt
      );
    if (!fresh) todo.push({ slug, ...info });
  }
  console.log(`[clawhub] 待下载 ${todo.length} 个（本轮上限 ${MAX_ITEMS}）`);
  const batch = todo.slice(0, MAX_ITEMS);

  const limit = createLimiter(CONCURRENCY);
  let done = 0;
  await Promise.all(
    batch.map(({ slug, version, updatedAt }) =>
      limit(async () => {
        try {
          let filesById;
          try {
            filesById = new Map([[slug, await downloadOne(slug, null)]]);
          } catch (e) {
            if ((e.status === 400 || e.status === 409) && /Ambiguous/i.test(e.body || "")) {
              const owners = await resolveOwners(slug);
              filesById = new Map();
              for (const owner of owners) {
                filesById.set(`${safeName(owner)}--${safeName(slug)}`, {
                  owner,
                  files: await downloadOne(slug, owner),
                });
              }
            } else {
              throw e;
            }
          }
          // 写入所有变体，并清理不再存在的变体目录
          const newIds = new Set(filesById.keys());
          for (const [id, entry] of filesById) {
            const files = entry.files ?? entry;
            const owner = entry.owner ?? null;
            const result = writeSkill(ROOT, SOURCE, id, files, {
              source: SOURCE,
              url: `https://clawhub.ai/skills/${slug}`,
              slug,
              ownerHandle: owner,
              version,
              updatedAt,
            });
            stats.record(result);
            stored[id] = { slug, ownerHandle: owner, version, updatedAt, contentHash: contentHash(files), format: FORMAT };
          }
          for (const oldId of bySlug.get(slug) || []) {
            if (!newIds.has(oldId)) {
              removeSkill(ROOT, SOURCE, oldId);
              delete stored[oldId];
              stats.removed++;
            }
          }
        } catch (e) {
          stats.fail(slug, e);
        } finally {
          done++;
          if (done % 200 === 0) console.log(`[clawhub] 进度 ${done}/${batch.length}`);
        }
      })
    )
  );

  saveState(ROOT, SOURCE, state);
  stats.report();
  // 枚举或大面积失败视为失败：失败率 >20% 且数量可观时非零退出，阻断 PR
  if (stats.failed > 50 && stats.failed > (stats.added + stats.updated + stats.unchanged) * 0.2) {
    process.exitCode = 1;
  }
}

main().catch((e) => {
  console.error(`[clawhub] 同步失败:`, e);
  process.exit(1);
});
