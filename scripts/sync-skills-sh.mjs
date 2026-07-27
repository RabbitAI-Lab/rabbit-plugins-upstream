// 同步 skills.sh (www.skills.sh) 全量 skills。
// 枚举: sitemap.xml → sitemap-skills-*.xml → /<owner>/<repo>/<skillId>
// 内容: 按 owner/repo 分组，用 GitHub API 拉仓库 tarball，扫描 SKILL.md 定位 skill 目录。
// 增量: 以仓库 pushed_at 为准，仓库无变化则其下所有 skill 跳过。
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { fetchJson, fetchBuffer, fetchText, createLimiter } from "./lib/http.mjs";
import { loadState, saveState } from "./lib/state.mjs";
import { writeSkill, removeSkill, collectFiles, contentHash } from "./lib/writer.mjs";
import { resolveLfsFiles } from "./lib/lfs.mjs";
import { SyncStats } from "./lib/summary.mjs";
import { MAX_ITEMS, CONCURRENCY, safeName } from "./lib/config.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const SOURCE = "skills-sh";
const TOKEN = process.env.GITHUB_TOKEN || "";

function ghHeaders() {
  const h = { accept: "application/vnd.github+json" };
  if (TOKEN) h.authorization = `Bearer ${TOKEN}`;
  return h;
}

async function enumerateAll() {
  const index = await fetchText("https://www.skills.sh/sitemap.xml");
  const sitemapUrls = [...index.matchAll(/<loc>(https:\/\/www\.skills\.sh\/sitemap-skills-\d+\.xml)<\/loc>/g)].map(
    (m) => m[1]
  );
  console.log(`[skills-sh] 发现 ${sitemapUrls.length} 个 skills sitemap`);
  const entries = new Map(); // id -> {owner, repo, skillId}
  for (const url of sitemapUrls) {
    const xml = await fetchText(url, { timeoutMs: 120_000 });
    for (const m of xml.matchAll(/<loc>https:\/\/www\.skills\.sh\/([^/<]+)\/([^/<]+)\/([^/<]+)<\/loc>/g)) {
      const [, owner, repo, skillId] = m;
      const id = `${safeName(owner)}--${safeName(repo)}--${safeName(skillId)}`;
      entries.set(id, { owner, repo, skillId });
    }
  }
  return entries;
}

function parseFrontmatterName(skillMd) {
  const m = skillMd.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return null;
  const n = m[1].match(/^name:\s*["']?([^"'\n]+?)["']?\s*$/m);
  return n ? n[1].trim() : null;
}

// 在解压的仓库目录中定位某个 skill 的目录
function locateSkillDir(repoDir, skillId) {
  const candidates = []; // SKILL.md 路径
  const walk = (d, depth) => {
    if (depth > 10) return;
    let list;
    try {
      list = fs.readdirSync(d, { withFileTypes: true });
    } catch {
      return;
    }
    for (const e of list) {
      if (e.name === "node_modules" || e.name === ".git") continue;
      const full = path.join(d, e.name);
      if (e.isDirectory()) walk(full, depth + 1);
      else if (e.isFile() && e.name.toLowerCase() === "skill.md") candidates.push(full);
    }
  };
  walk(repoDir, 0);
  // 优先：父目录名 == skillId
  for (const f of candidates) {
    if (path.basename(path.dirname(f)) === skillId) return path.dirname(f);
  }
  // 其次：frontmatter name == skillId
  for (const f of candidates) {
    try {
      if (parseFrontmatterName(fs.readFileSync(f, "utf8")) === skillId) return path.dirname(f);
    } catch {}
  }
  return null;
}

async function main() {
  if (!TOKEN) console.warn("[skills-sh] 未设置 GITHUB_TOKEN，GitHub API 限流 60 次/小时，仅适合小批量试跑");
  const state = loadState(ROOT, SOURCE);
  state.repos ??= {};
  state.skills ??= {};
  const { repos, skills } = state;
  const stats = new SyncStats(SOURCE);

  console.log("[skills-sh] 开始全量枚举…");
  const entries = await enumerateAll();
  console.log(`[skills-sh] 上游共 ${entries.size} 个 skill`);

  // 下架删除
  for (const [id, meta] of Object.entries(skills)) {
    if (!entries.has(id)) {
      if (removeSkill(ROOT, SOURCE, id)) {
        delete skills[id];
        stats.removed++;
        console.log(`[skills-sh] 删除已下架: ${id}`);
      }
    }
  }

  // 按仓库分组
  const byRepo = new Map(); // "owner/repo" -> [{id, skillId}]
  for (const [id, e] of entries) {
    const key = `${e.owner}/${e.repo}`;
    if (!byRepo.has(key)) byRepo.set(key, []);
    byRepo.get(key).push({ id, skillId: e.skillId });
  }
  console.log(`[skills-sh] 涉及 ${byRepo.size} 个仓库`);

  // 处理顺序：新仓库优先，其余按枚举顺序；只有实际发生下载的 skill 才消耗本轮额度
  const repoKeys = [...byRepo.keys()].sort((a, b) => Number(repos[a] != null) - Number(repos[b] != null));
  let fetched = 0; // 本轮已实际下载的 skill 数
  let stopped = false;

  const limit = createLimiter(CONCURRENCY);
  let done = 0;
  await Promise.all(
    repoKeys.map((key) =>
      limit(async () => {
        if (stopped) return;
        const wanted = byRepo.get(key);
        try {
          const info = await fetchJson(`https://api.github.com/repos/${key}`, { headers: ghHeaders() });
          const pushedAt = info.pushed_at;
          const branch = info.default_branch;
          // 仓库无变化且这批 skill 都处理过（含确认缺失的）→ 全部跳过
          if (
            repos[key]?.pushedAt === pushedAt &&
            wanted.every((w) => repos[key].skillIds?.includes(w.id))
          ) {
            wanted.forEach((w) => skills[w.id] && stats.record("unchanged"));
            return;
          }
          const tarBuf = await fetchBuffer(`https://api.github.com/repos/${key}/tarball/${branch}`, {
            headers: ghHeaders(),
            timeoutMs: 300_000,
          });
          fetched += wanted.length;
          if (fetched >= MAX_ITEMS) stopped = true;
          const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "skills-sh-"));
          try {
            const tarFile = path.join(tmp, "repo.tar.gz");
            fs.writeFileSync(tarFile, tarBuf);
            execFileSync("tar", ["-xzf", tarFile, "-C", tmp], { stdio: "pipe" });
            fs.rmSync(tarFile);
            const top = fs.readdirSync(tmp).find((d) => fs.statSync(path.join(tmp, d)).isDirectory());
            if (!top) throw new Error("tarball 解压后为空");
            const repoDir = path.join(tmp, top);
            for (const w of wanted) {
              const dir = locateSkillDir(repoDir, w.skillId);
              if (!dir) {
                stats.fail(w.id, new Error(`仓库中未找到 skill 目录 (skillId=${w.skillId})`));
                continue;
              }
              const files = collectFiles(dir);
              await resolveLfsFiles(key, files, ghHeaders());
              const result = writeSkill(ROOT, SOURCE, w.id, files, {
                source: SOURCE,
                url: `https://www.skills.sh/${key}/${w.skillId}`,
                repo: key,
                skillId: w.skillId,
                branch,
                pushedAt,
              });
              stats.record(result);
              skills[w.id] = { repo: key, skillId: w.skillId, pushedAt, contentHash: contentHash(files) };
            }
            repos[key] = { defaultBranch: branch, pushedAt, skillIds: wanted.map((w) => w.id) };
          } finally {
            fs.rmSync(tmp, { recursive: true, force: true });
          }
        } catch (e) {
          if (e.status === 404) {
            // 仓库删除或转私有 → 移除其下 skill
            for (const w of wanted) {
              if (removeSkill(ROOT, SOURCE, w.id)) {
                delete skills[w.id];
                stats.removed++;
              }
            }
            delete repos[key];
            console.log(`[skills-sh] 仓库 404，移除其 skill: ${key}`);
          } else {
            for (const w of wanted) stats.fail(w.id, e);
          }
        } finally {
          done++;
          if (done % 100 === 0) console.log(`[skills-sh] 进度 ${done}/${repoKeys.length} 仓库，已下载 ${fetched} 个 skill`);
        }
      })
    )
  );

  saveState(ROOT, SOURCE, state);
  stats.report();
  if (stats.failed > 50 && stats.failed > (stats.added + stats.updated + stats.unchanged) * 0.2) {
    process.exitCode = 1;
  }
}

main().catch((e) => {
  console.error(`[skills-sh] 同步失败:`, e);
  process.exit(1);
});
