#!/usr/bin/env node
// 盯同行：取一批账号最新的一页内容，和上一次存下的结果比，写出“新增了什么、互动最高的是哪几条、哪里没取到”。
// Watch competitors: fetch each account's newest page, compare with the last saved run, write what is new,
// what got the most engagement and what could not be fetched.
//
//   node watch.mjs [--dir dataxapi-watch] [--plan] [--max-spend 1] [--metrics-per-account 5]
//
// <dir>/watchlist.json lists the accounts: {"accounts":[{"platform":"douyin","id":"MS4w…","name":"36氪"}]}
// platform is one of wechat_mp, douyin, xiaohongshu, wechat_channels. Every run saves <dir>/runs/<time>.json
// and <dir>/report-<time>.md, and points <dir>/latest.json at the run, which the next run compares against.
// Calls go through the dataxapi command line, with the key from DATAXAPI_API_KEY (never printed).
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, writeFileSync, rmSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";

const SOURCE = "skill.watch-competitors-weekly";
const LIST = {
  wechat_mp: "wechat_mp.accounts.articles.list",
  douyin: "douyin.users.videos.list",
  xiaohongshu: "xiaohongshu.users.notes.list",
  wechat_channels: "wechat_channels.users.videos.list",
};
const PLATFORM_ZH = { wechat_mp: "公众号", douyin: "抖音", xiaohongshu: "小红书", wechat_channels: "视频号" };
const METRICS = "wechat_mp.articles.metrics";

const args = process.argv.slice(2);
const flag = (name, fallback) => {
  const i = args.indexOf(`--${name}`);
  return i === -1 ? fallback : args[i + 1];
};
const DIR = flag("dir", "dataxapi-watch");
const PLAN = args.includes("--plan");
const MAX_SPEND = Number(flag("max-spend", "1"));
const METRICS_PER_ACCOUNT = Number(flag("metrics-per-account", "5"));

const cli = (() => {
  const found = spawnSync("dataxapi", ["--help"], { encoding: "utf8" });
  return found.error ? ["npx", "-y", "dataxapi"] : ["dataxapi"];
})();
const run = (argv) => spawnSync(cli[0], [...cli.slice(1), ...argv], { encoding: "utf8", env: process.env });

// The price is read from the live catalog before anything is called, never written down here.
const priceCache = new Map();
function priceOf(capability) {
  if (!priceCache.has(capability)) {
    const shown = run(["show", capability, "--json"]);
    if (shown.status !== 0) throw new Error(`cannot read the price of ${capability}: ${shown.stderr || shown.stdout}`);
    const pricing = JSON.parse(shown.stdout).capability.pricing;
    priceCache.set(capability, Number(pricing.max_charge));
  }
  return priceCache.get(capability);
}

function call(capability, params) {
  const out = join(tmpdir(), `dataxapi-watch-${process.pid}-${Date.now()}-${Math.random().toString(36).slice(2)}.json`);
  const argv = ["call", capability, ...Object.entries(params).map(([k, v]) => `${k}=${v}`),
    "--max-price", String(priceOf(capability)), "--source", SOURCE, "--out", out];
  let done = run(argv);
  // A failure that says one retry may help (exit 3, nothing charged) is tried once more after 5 seconds.
  if (done.status === 3 && /Retry: once/.test(`${done.stderr}${done.stdout}`)) {
    spawnSync("sleep", ["5"]);
    done = run(argv);
  }
  const said = `${done.stderr ?? ""}${done.stdout ?? ""}`.trim();
  if (done.status === 0 && existsSync(out)) {
    const body = JSON.parse(readFileSync(out, "utf8"));
    rmSync(out, { force: true });
    return { ok: true, body, charged: Number(body.meta?.billing?.amount ?? 0) };
  }
  rmSync(out, { force: true });
  // 2: refused before running, not charged. 3: ran and failed. 4: not known whether charged.
  const lines = said.split("\n");
  const zh = lines.find((l) => l.startsWith("中文："));
  const code = lines.find((l) => l.startsWith("Error "))?.split(":")[0].replace("Error ", "");
  return { ok: false, exit: done.status, message: zh ? `${zh.replace("中文：", "")}${code ? `（${code}）` : ""}` : lines.slice(0, 3).join(" ") };
}

const engagement = (m = {}) => (m.likes ?? 0) + (m.comments ?? 0) + (m.shares ?? 0) + (m.favorites ?? 0);
const short = (s, n = 40) => (s ?? "").replace(/\s+/g, " ").trim().slice(0, n);
const cell = (s) => String(s ?? "").replace(/\|/g, "／");
const day = (iso) => (iso ? iso.slice(0, 16).replace("T", " ") : "");
// WeChat links keep only what names the article (__biz, mid, idx, sn).
const tidy = (url) => url?.replace(/^http:/, "https:").replace(/&chksm=.*$/, "");
const linkOf = (platform, item) => tidy(item.url)
  ?? (platform === "douyin" ? `https://www.douyin.com/video/${item.id}` : null)
  ?? (platform === "xiaohongshu" ? `https://www.xiaohongshu.com/explore/${item.id}` : null);

// ---------- read the list and the last run ----------
const watchlistPath = join(DIR, "watchlist.json");
if (!existsSync(watchlistPath)) {
  console.error(`没有 ${watchlistPath}。先建它：{"accounts":[{"platform":"douyin","id":"MS4w…","name":"某某"}]}`);
  process.exit(2);
}
const accounts = JSON.parse(readFileSync(watchlistPath, "utf8")).accounts ?? [];
// douyin and xiaohongshu also take a profile link as url instead of id.
const bad = accounts.filter((a) => !LIST[a.platform] || !(a.id || (a.url && ["douyin", "xiaohongshu"].includes(a.platform))));
for (const a of accounts) a.key = a.id ?? a.url;
if (bad.length) {
  console.error(`watchlist 里这些账号写得不对（platform 只能是 ${Object.keys(LIST).join("、")}；id 必填，抖音、小红书也可以填主页链接 url）：${JSON.stringify(bad)}`);
  process.exit(2);
}
const latestPath = join(DIR, "latest.json");
const previous = existsSync(latestPath)
  ? JSON.parse(readFileSync(join(DIR, JSON.parse(readFileSync(latestPath, "utf8")).run), "utf8"))
  : null;
// An account that was not fetched last time keeps the posts of the run before (carried), so it is compared with those.
const prevOf = (a) => {
  const p = previous?.accounts.find((x) => x.platform === a.platform && (x.key ?? x.id) === a.key);
  if (!p) return undefined;
  if (p.status === "failed") return p.carried ? { ...p, items: p.carried.items, fetched_at: p.carried.fetched_at, carried: true } : undefined;
  return p;
};

// ---------- the plan: the most it can cost ----------
let most = 0;
for (const a of accounts) {
  most += priceOf(LIST[a.platform]);
  if (a.platform === "wechat_mp") most += METRICS_PER_ACCOUNT * priceOf(METRICS);
}
most = Math.round(most * 10000) / 10000;
console.log(`计划：${accounts.length} 个号，每个号取最新一页${accounts.some((a) => a.platform === "wechat_mp") ? `，公众号每号最多再取 ${METRICS_PER_ACCOUNT} 篇新文章的阅读数` : ""}。最多花 $${most}（价格读自线上目录）。`);
if (PLAN) process.exit(0);
if (most > MAX_SPEND) {
  console.error(`最多可能花 $${most}，超过 --max-spend ${MAX_SPEND}。告诉用户这个数，他同意后用 --max-spend ${most} 再跑。`);
  process.exit(2);
}

// ---------- fetch ----------
const startedAt = new Date().toISOString();
let spent = 0;
const results = [];
for (const a of accounts) {
  const name = a.name ?? a.key;
  const got = call(LIST[a.platform], a.id ? { id: a.id } : { url: a.url });
  if (!got.ok) {
    const before = prevOf(a);
    results.push({ ...a, name, status: "failed", exit: got.exit, message: got.message, items: [],
      carried: before ? { items: before.items, fetched_at: before.fetched_at } : null });
    if (got.exit === 2 && /no API key|insufficient_balance|key_budget_exceeded|余额/.test(got.message)) {
      console.error(`停下：${got.message}`);
      break;
    }
    continue;
  }
  spent += got.charged;
  const items = (got.body.data?.items ?? []).map((x) => ({
    id: x.id, url: linkOf(a.platform, x), title: x.title ?? null, text: short(x.text, 120), type: x.type ?? null,
    published_at: x.published_at ?? null, metrics: x.metrics ?? null,
  }));
  const prev = prevOf(a);
  const seen = new Set((prev?.items ?? []).map((x) => x.id));
  // WeChat article lists carry no counts: read the newest unseen articles' reads, up to the cap.
  if (a.platform === "wechat_mp") {
    const fresh = items.filter((x) => !seen.has(x.id)).sort((x, y) => (y.published_at ?? "").localeCompare(x.published_at ?? ""));
    for (const x of fresh.slice(0, METRICS_PER_ACCOUNT)) {
      const m = call(METRICS, { url: x.url });
      if (m.ok) { spent += m.charged; x.metrics = m.body.data?.metrics ?? m.body.data?.item?.metrics ?? null; }
      else x.metrics_error = m.message;
    }
    // Counts read last time stay with articles seen again.
    for (const x of items) if (!x.metrics) x.metrics = prev?.items.find((p) => p.id === x.id)?.metrics ?? null;
  }
  results.push({ ...a, name, status: items.length ? "ok" : "empty", fetched_at: got.body.meta?.fetched_at ?? null, items });
}

// ---------- compare ----------
const finishedAt = new Date().toISOString();
const rows = [];
const fresh = [];
const problems = [];
for (const r of results) {
  const prev = prevOf(r);
  const seen = new Set((prev?.items ?? []).map((x) => x.id));
  const newOnes = prev && r.status !== "failed" ? r.items.filter((x) => !seen.has(x.id)) : [];
  const newest = r.items.map((x) => x.published_at).filter(Boolean).sort().at(-1) ?? "";
  rows.push({ r, prev, newOnes, newest });
  for (const x of newOnes) fresh.push({ r, x });
  if (r.status === "failed") problems.push(`${PLATFORM_ZH[r.platform]}「${r.name}」没取到：${r.message}（退出码 ${r.exit}${r.exit === 4 ? "，不确定是否扣费，先用 dataxapi more 查，不要重发" : "，没扣费"}）`);
  if (r.status === "empty") problems.push(`${PLATFORM_ZH[r.platform]}「${r.name}」返回空：号不存在、编号不对，或这个号没有公开内容`);
  for (const x of r.items) if (x.metrics_error) problems.push(`公众号「${r.name}」《${short(x.title, 24)}》阅读数没取到：${x.metrics_error}`);
}
for (const { r, prev, newOnes } of rows) if (r.platform === "wechat_mp" && r.status === "ok") {
  const noCount = (prev ? newOnes : r.items).filter((x) => !x.metrics).length;
  if (noCount) problems.push(`公众号「${r.name}」${prev ? "新增的" : "这一页"}有 ${noCount} 篇没取阅读数（每号每次只取最新 ${METRICS_PER_ACCOUNT} 篇新文章的，要多取用 --metrics-per-account 调大）`);
}

// Engagement is ranked within each account (a big account's ordinary post is not a hit): of the new posts, or on a
// first run of the posts of the last 7 days.
const weekAgo = new Date(Date.parse(startedAt) - 7 * 864e5).toISOString();
const ranked = [];
for (const { r, newOnes } of rows) {
  const pool = (previous ? newOnes : r.items.filter((x) => (x.published_at ?? "") >= weekAgo)).filter((x) => x.metrics);
  pool.sort((p, q) => engagement(q.metrics) - engagement(p.metrics)).slice(0, 3).forEach((x, i) => ranked.push({ r, x, i: i + 1 }));
}

// ---------- write ----------
const stamp = startedAt.replace(/[:.]/g, "-");
mkdirSync(join(DIR, "runs"), { recursive: true });
const runFile = join("runs", `${stamp}.json`);
writeFileSync(join(DIR, runFile), JSON.stringify({ started_at: startedAt, finished_at: finishedAt, spent, accounts: results }, null, 2));
const anyOk = results.some((r) => r.status === "ok");
if (anyOk) writeFileSync(latestPath, JSON.stringify({ run: runFile, at: startedAt }, null, 2));

const L = [];
L.push(`# 盯同行周报 · ${day(startedAt)} UTC`, "");
L.push(previous
  ? `比的是上一期：${day(previous.started_at)} UTC 那次（${previous.accounts.length} 个号）。`
  : `这是第一次运行，没有上一期可比：下面是各号现在最新的一页，存为基准，下次运行起报“新增了什么”。`);
L.push(`查了 ${results.length} 个号，取到 ${results.filter((r) => r.status === "ok").length} 个，新增内容 ${fresh.length} 条。本次花费 $${Math.round(spent * 10000) / 10000}。`, "");
L.push("## 各号情况", "", "| 平台 | 账号 | 结果 | 这页条数 | 新增 | 最新一条发于 (UTC) |", "|---|---|---|---:|---:|---|");
for (const { r, prev, newOnes, newest } of rows) {
  const state = r.status === "ok" ? "取到" : r.status === "empty" ? "空" : "没取到";
  const compared = r.status === "failed" ? "—" : prev ? `${newOnes.length}${prev.carried ? "（和更早一期比）" : ""}` : "（基准）";
  L.push(`| ${PLATFORM_ZH[r.platform]} | ${cell(r.name)} | ${state} | ${r.items.length} | ${compared} | ${day(newest)} |`);
}
L.push("");
if (previous) {
  L.push("## 新增了什么", "");
  if (!fresh.length) L.push(`和上一期比，取到的号都没有新内容。`, "");
  else {
    L.push("| 平台 | 账号 | 发布 (UTC) | 标题/文案 | 赞 | 评 | 转 | 藏 | 阅读/播放 | 链接 |", "|---|---|---|---|---:|---:|---:|---:|---:|---|");
    for (const { r, x } of fresh.sort((p, q) => (q.x.published_at ?? "").localeCompare(p.x.published_at ?? ""))) {
      const m = x.metrics ?? {};
      L.push(`| ${PLATFORM_ZH[r.platform]} | ${cell(r.name)} | ${day(x.published_at)} | ${cell(short(x.title || x.text, 36))} | ${m.likes ?? ""} | ${m.comments ?? ""} | ${m.shares ?? ""} | ${m.favorites ?? ""} | ${m.views ?? ""} | ${x.url ?? "—"} |`);
    }
    L.push("");
  }
}
L.push(previous ? "## 新增里互动最高的（每个号前 3）" : "## 近 7 天互动最高的（每个号前 3）", "");
if (!ranked.length) L.push(previous && !fresh.length ? "没有新增，所以这一项为空。" : "没有带互动数的内容。", "");
else {
  L.push("| 平台 | 账号 | 名次 | 发布 (UTC) | 标题/文案 | 互动合计（赞+评+转+藏） | 阅读/播放 | 链接 |", "|---|---|---:|---|---|---:|---:|---|");
  ranked.forEach(({ r, x, i }) => L.push(`| ${PLATFORM_ZH[r.platform]} | ${cell(r.name)} | ${i} | ${day(x.published_at)} | ${cell(short(x.title || x.text, 36))} | ${engagement(x.metrics)} | ${x.metrics.views ?? ""} | ${x.url ?? "—"} |`));
  L.push("");
}
L.push("## 没取到、没比上的", "");
L.push(problems.length ? problems.map((p) => `- ${p}`).join("\n") : "- 没有：每个号都取到了。", "");
if (!anyOk) L.push("这次一个号都没取到，latest.json 没动：下次仍和上一期比。", "");
L.push(`数据来源：DataXAPI，取数时间 ${finishedAt}`);
const report = L.join("\n");
const reportFile = join(DIR, `report-${stamp}.md`);
writeFileSync(reportFile, report);
console.log(report);
console.log(`\n（周报存在 ${reportFile}；这次的结果存在 ${join(DIR, runFile)}，下次和它比）`);
