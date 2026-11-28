#!/usr/bin/env node
// 公众号最新文章和阅读数：一个或一批公众号，最近 N 天（或最新 N 篇）的文章，每篇的阅读、点赞、在看、转发、收藏、评论。
// The newest articles of one or more WeChat Official Accounts with each article's reads, likes, recommends, shares,
// saves and comments, as a table (printed as Markdown, saved as CSV).
//
//   node latest.mjs --ids gh_a:名字,gh_b [--names 36氪,虎嗅] [--days 7] [--per-account 10] [--plan] [--max-spend 1] [--out reads.csv]
import { spawnSync } from "node:child_process";
import { existsSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";

const SOURCE = "skill.wechat-latest-reads";
const args = process.argv.slice(2);
const flag = (name, fallback) => { const i = args.indexOf(`--${name}`); return i === -1 ? fallback : args[i + 1]; };
const list = (v) => (v ? v.split(/[,，]/).map((s) => s.trim()).filter(Boolean) : []);
const IDS = list(flag("ids"));
const NAMES = list(flag("names"));
const DAYS = Number(flag("days", "7"));
const PER = Number(flag("per-account", "10"));
const PLAN = args.includes("--plan");
const MAX_SPEND = Number(flag("max-spend", "1"));
const OUT = flag("out", `wechat-reads-${new Date().toISOString().slice(0, 10)}.csv`);
if (!IDS.length && !NAMES.length) { console.error("给 --ids gh_…（原始 ID）或 --names 公众号名字，逗号隔开"); process.exit(2); }

const cli = spawnSync("dataxapi", ["--help"]).error ? ["npx", "-y", "dataxapi"] : ["dataxapi"];
const run = (argv) => spawnSync(cli[0], [...cli.slice(1), ...argv], { encoding: "utf8" });
const prices = new Map();
function priceOf(cap) {
  if (!prices.has(cap)) {
    const r = run(["show", cap, "--json"]);
    if (r.status !== 0) throw new Error(`读不到 ${cap} 的价格：${r.stderr}`);
    prices.set(cap, Number(JSON.parse(r.stdout).capability.pricing.max_charge));
  }
  return prices.get(cap);
}
let spent = 0;
function call(cap, params) {
  const out = join(tmpdir(), `dx-${process.pid}-${Math.random().toString(36).slice(2)}.json`);
  const argv = ["call", cap, ...Object.entries(params).map(([k, v]) => `${k}=${v}`), "--max-price", String(priceOf(cap)), "--source", SOURCE, "--out", out];
  let r = run(argv);
  if (r.status === 3 && /Retry: once/.test(`${r.stderr}${r.stdout}`)) { spawnSync("sleep", ["5"]); r = run(argv); }
  if (r.status === 0 && existsSync(out)) {
    const body = JSON.parse(readFileSync(out, "utf8")); rmSync(out, { force: true });
    spent += Number(body.meta?.billing?.amount ?? 0);
    return { ok: true, body };
  }
  rmSync(out, { force: true });
  const lines = `${r.stderr}${r.stdout}`.split("\n");
  const zh = lines.find((l) => l.startsWith("中文："))?.replace("中文：", "");
  const code = lines.find((l) => l.startsWith("Error "))?.split(":")[0].replace("Error ", "");
  const fatal = r.status === 2 && /no API key|insufficient_balance|key_budget_exceeded/.test(lines.join(" "));
  return { ok: false, exit: r.status, fatal, message: zh ? `${zh}${code ? `（${code}）` : ""}` : lines.slice(0, 3).join(" ") };
}

const LIST = "wechat_mp.accounts.articles.list", METRICS = "wechat_mp.articles.metrics", SEARCH = "wechat.accounts.search";
const most = Math.round(((IDS.length + NAMES.length) * (priceOf(LIST) + PER * priceOf(METRICS)) + NAMES.length * priceOf(SEARCH)) * 10000) / 10000;
console.log(`计划：${IDS.length + NAMES.length} 个公众号${NAMES.length ? `（其中 ${NAMES.length} 个先按名字查原始 ID）` : ""}，每号取最新一页文章，最近 ${DAYS} 天内最多 ${PER} 篇各取一次阅读数。最多花 $${most}（价格读自线上目录）。`);
if (PLAN) process.exit(0);
if (most > MAX_SPEND) { console.error(`最多可能花 $${most}，超过 --max-spend ${MAX_SPEND}：告诉用户，他同意后用 --max-spend ${most} 再跑。`); process.exit(2); }

// --ids takes gh_xxx or gh_xxx:名字 (the list does not say the account's name).
const accounts = IDS.map((v) => { const [id, name] = v.split(":"); return { id, name: name || id }; });
const problems = [];
for (const name of NAMES) {
  const r = call(SEARCH, { query: name });
  if (!r.ok) { problems.push(`「${name}」查 ID 没成功：${r.message}`); if (r.fatal) break; continue; }
  const items = r.body.data?.items ?? [];
  const exact = items.filter((x) => x.name === name);
  if (exact.length === 1) accounts.push({ id: exact[0].id, name });
  else problems.push(`「${name}」${exact.length ? "有好几个同名号" : "没有名字完全一样的号"}，候选：${items.slice(0, 5).map((x) => `${x.name}（${x.id}）`).join("、") || "无"}。请用户选定后用 --ids 再跑`);
}

const since = new Date(Date.now() - DAYS * 864e5).toISOString();
const rows = [];
for (const a of accounts) {
  const r = call(LIST, { id: a.id, view: "full" });
  if (!r.ok) { problems.push(`「${a.name}」文章列表没取到：${r.message}（退出码 ${r.exit}${r.exit === 4 ? "，不确定是否扣费，先 dataxapi more 查" : "，没扣费"}）`); if (r.fatal) break; continue; }
  const items = (r.body.data?.items ?? []).filter((x) => (x.published_at ?? "") >= since)
    .sort((x, y) => (y.published_at ?? "").localeCompare(x.published_at ?? "")).slice(0, PER);
  if (!items.length) problems.push(`「${a.name}」最近 ${DAYS} 天没有发文（列表最新一篇发于 ${(r.body.data?.items ?? [])[0]?.published_at ?? "未知"}）`);
  for (const x of items) {
    const m = call(METRICS, { url: x.url, view: "full" });
    const got = m.ok ? (m.body.data?.item ?? m.body.data ?? {}) : {};
    const metrics = got.metrics ?? {};
    const recommends = got.ext?.recommends ?? "";
    if (!m.ok) problems.push(`「${a.name}」《${x.title}》阅读数没取到：${m.message}`);
    rows.push({ account: a.name, account_id: a.id, published_at: x.published_at, position: x.ext?.position ?? "", title: x.title,
      views: metrics.views ?? "", likes: metrics.likes ?? "", recommends, shares: metrics.shares ?? "", favorites: metrics.favorites ?? "",
      comments: metrics.comments ?? "", url: x.url.replace(/^http:/, "https:").replace(/&chksm=.*$/, "") });
    if (m.fatal) break;
  }
}

const cols = ["account", "account_id", "published_at", "position", "title", "views", "likes", "recommends", "shares", "favorites", "comments", "url"];
const esc = (v) => (/[",\n]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : String(v));
writeFileSync(OUT, "﻿" + [cols.join(","), ...rows.map((r) => cols.map((c) => esc(r[c] ?? "")).join(","))].join("\n"));
const fetched = new Date().toISOString();
const cell = (s) => String(s ?? "").replace(/\|/g, "／");
const L = [`# 公众号最新文章和阅读数（最近 ${DAYS} 天）`, "", `${accounts.length} 个号，${rows.length} 篇文章。本次花费 $${Math.round(spent * 10000) / 10000}。表格也存成了 ${OUT}（Excel 可直接打开）。`, "",
  "| 公众号 | 发布 (UTC) | 位置 | 标题 | 阅读 | 点赞 | 在看 | 转发 | 收藏 | 评论 |", "|---|---|---|---|---:|---:|---:|---:|---:|---:|"];
for (const r of rows) L.push(`| ${cell(r.account)} | ${(r.published_at ?? "").slice(0, 16).replace("T", " ")} | ${r.position === 1 ? "头条" : r.position ? `第${r.position}条` : ""} | [${cell(r.title)}](${r.url}) | ${r.views} | ${r.likes} | ${r.recommends} | ${r.shares} | ${r.favorites} | ${r.comments} |`);
L.push("", "阅读数到 10 万以上时平台只给“10万+”，表里 100000 及以上的数是下限。", "");
if (problems.length) L.push("## 没取到的", "", ...problems.map((p) => `- ${p}`), "");
L.push(`数据来源：DataXAPI，取数时间 ${fetched}`);
console.log(L.join("\n"));
