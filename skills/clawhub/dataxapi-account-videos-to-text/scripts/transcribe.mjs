#!/usr/bin/env node
// 某个号的视频全部转成文字稿：翻这个号的作品列表，按时长估好钱，再一条条转文字，每条存一个 .md，另出一张索引表和一份合集。
// Turn an account's videos into transcripts: list its videos, estimate the cost from their lengths, then transcribe each,
// one .md a video, an index CSV and one combined file. Videos over 5 minutes come back as a job that is fetched later.
//
//   node transcribe.mjs --platform douyin|wechat_channels|xiaohongshu|kuaishou (--id <账号编号> | --url <主页链接>)
//                       [--max-videos 20] [--since 2026-01-01] [--max-spend 1] [--out <目录>] [--wait-minutes 30] [--plan]
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";

const SOURCE = "skill.account-videos-to-text";
const P = {
  douyin: { list: "douyin.users.videos.list", tr: "douyin.videos.transcript.get", byUrl: true },
  wechat_channels: { list: "wechat_channels.users.videos.list", tr: "wechat_channels.videos.transcript.get", byUrl: false },
  xiaohongshu: { list: "xiaohongshu.users.notes.list", tr: "xiaohongshu.videos.transcript.get", byUrl: true },
  kuaishou: { list: "kuaishou.users.videos.list", tr: "kuaishou.videos.transcript.get", byUrl: false },
};
const args = process.argv.slice(2);
const flag = (name, fallback) => { const i = args.indexOf(`--${name}`); return i === -1 ? fallback : args[i + 1]; };
const PLATFORM = flag("platform"), ID = flag("id"), URL_ = flag("url");
const MAX_VIDEOS = Number(flag("max-videos", "20"));
const SINCE = flag("since", "");
const MAX_SPEND = Number(flag("max-spend", "1"));
const WAIT_MIN = Number(flag("wait-minutes", "30"));
const PLAN = args.includes("--plan");
if (!P[PLATFORM] || !(ID || (URL_ && P[PLATFORM].byUrl))) { console.error("要 --platform douyin|wechat_channels|xiaohongshu|kuaishou 和 --id <账号编号>（抖音、小红书也可 --url <主页链接>）"); process.exit(2); }
const OUT = flag("out", `transcripts-${PLATFORM}-${(ID ?? "account").slice(-8)}`);
const { list: LIST, tr: TR } = P[PLATFORM];

const cli = spawnSync("dataxapi", ["--help"]).error ? ["npx", "-y", "dataxapi"] : ["dataxapi"];
const run = (argv) => spawnSync(cli[0], [...cli.slice(1), ...argv], { encoding: "utf8" });
const pricing = new Map();
const priceOf = (cap) => {
  if (!pricing.has(cap)) {
    const r = run(["show", cap, "--json"]);
    if (r.status !== 0) throw new Error(`读不到 ${cap} 的价格：${r.stderr}`);
    pricing.set(cap, JSON.parse(r.stdout).capability.pricing);
  }
  return pricing.get(cap);
};
let spent = 0;
function call(cap, params, maxPrice) {
  const out = join(tmpdir(), `dx-${process.pid}-${Math.random().toString(36).slice(2)}.json`);
  const argv = ["call", cap, ...Object.entries(params).map(([k, v]) => `${k}=${v}`), "--max-price", String(maxPrice), "--source", SOURCE, "--out", out];
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
  return { ok: false, exit: r.status, fatal: r.status === 2 && /no API key|insufficient_balance|key_budget_exceeded/.test(lines.join(" ")),
    message: `${zh ?? lines[0]}（退出码 ${r.status}${r.status === 4 ? "，不确定是否扣费：先 dataxapi more 查，不要重发" : "，没扣费"}）` };
}

// ---------- 1. the videos ----------
const listPrice = Number(priceOf(LIST).max_charge);
const videos = [];
let cursor = null, listCalls = 0, stopped = "";
while (videos.length < MAX_VIDEOS) {
  const r = call(LIST, { ...(ID ? { id: ID } : { url: URL_ }), view: "full", ...(cursor ? { cursor } : {}) }, listPrice);
  listCalls += 1;
  if (!r.ok) { stopped = `作品列表第 ${listCalls} 页没取到：${r.message}`; break; }
  let old = false;
  for (const x of r.body.data?.items ?? []) {
    if (PLATFORM === "xiaohongshu" && x.type !== "video") continue;
    if (SINCE && (x.published_at ?? "") < SINCE) { old = true; continue; }
    videos.push({ id: x.id, title: (x.title || x.text || "").replace(/\s+/g, " ").slice(0, 60), published_at: x.published_at ?? "",
      duration: Number(x.ext?.duration ?? 0), url: x.url ?? (PLATFORM === "douyin" ? `https://www.douyin.com/video/${x.id}` : "") });
  }
  cursor = r.body.page?.has_more && !old ? r.body.page.next_cursor : null;
  if (!cursor) break;
}
// Pinned old videos come first in a list: newest first, then the cap.
videos.sort((a, b) => b.published_at.localeCompare(a.published_at));
videos.splice(MAX_VIDEOS);
if (!videos.length) { console.error(stopped || "这个号没有取到视频（编号不对、没有公开视频，或 --since 太晚）"); process.exit(stopped ? 3 : 0); }

// ---------- 2. what it will cost ----------
// A transcript is charged a call (price) plus by the minute of speech (per_minute); a video up to 5 minutes comes
// back at once, capped at max_charge; a longer one is a job, charged by its actual minutes when the text is delivered.
const tp = priceOf(TR);
const base = Number(tp.price), perMin = Number(tp.per_minute ?? 0), cap = Number(tp.max_charge);
const est = (v) => (v.duration ? base + perMin * Math.ceil(v.duration / 60) : cap);
const known = videos.filter((v) => v.duration).length;
const most = Math.round(videos.reduce((s, v) => s + (!v.duration ? cap : v.duration <= 300 ? Math.min(est(v), cap) : est(v)), 0) * 10000) / 10000;
const minutes = Math.round(videos.reduce((s, v) => s + v.duration, 0) / 60);
console.log(`计划：${videos.length} 条视频${known < videos.length ? `（${videos.length - known} 条列表没给时长，按单次上限 $${cap} 估）` : ""}，共约 ${minutes} 分钟。` +
  `转文字每条 $${base} 起，识别语音另按每分钟 $${perMin} 计（5 分钟以内一条最多 $${cap}；更长的按实际分钟数）。` +
  `估计 $${most}，另加已花的作品列表 $${Math.round(spent * 10000) / 10000}（价格读自线上目录）。`);
if (PLAN) process.exit(0);
if (most > MAX_SPEND) { console.error(`估计要 $${most}，超过 --max-spend ${MAX_SPEND}：告诉用户，他同意后用 --max-spend ${Math.ceil(most * 100) / 100} 再跑，或用 --max-videos 少转几条。`); process.exit(2); }

// ---------- 3. transcribe ----------
mkdirSync(OUT, { recursive: true });
const pending = [];
const problems = stopped ? [stopped] : [];
const save = (v, item) => {
  v.text = item.text ?? ""; v.status = "done";
  v.file = `${(v.published_at || "").slice(0, 10)}-${v.id}.md`;
  writeFileSync(join(OUT, v.file), `# ${v.title || v.id}\n\n- 发布：${v.published_at}\n- 时长：${Math.round(item.duration ?? v.duration)} 秒\n- 链接：${v.url || "—"}\n\n${v.text || "（这条视频里没有人说话）"}\n`);
};
for (const v of videos) {
  const limit = v.duration && v.duration <= 300 ? cap : Math.max(cap, est(v) + perMin);
  const r = call(TR, { id: v.id, view: "standard" }, Math.round(limit * 10000) / 10000);
  if (!r.ok && /没有人说话|no speech/i.test(r.message)) { v.status = "no_speech"; continue; } // not charged
  if (!r.ok) { v.status = "failed"; problems.push(`《${v.title}》没转成：${r.message}`); if (r.fatal) break; continue; }
  const item = r.body.data?.item ?? r.body.data ?? {};
  if (item.status === "done") save(v, item);
  else if (item.job) { v.status = "pending"; v.job = item.job; v.retry = Number(item.retry_after_seconds ?? 30); pending.push(v); }
  else { v.status = "failed"; problems.push(`《${v.title}》返回了 ${item.status ?? "未知状态"}`); }
}
// Long videos: fetch each job when it says, until --wait-minutes runs out (a job is kept 24 hours).
const deadline = Date.now() + WAIT_MIN * 60e3;
while (pending.length && Date.now() < deadline) {
  const wait = Math.min(...pending.map((v) => v.retry), 120);
  spawnSync("sleep", [String(wait)]);
  for (const v of [...pending]) {
    const r = call(TR, { job: v.job, view: "standard" }, Math.round((base + perMin * 125) * 10000) / 10000);
    if (!r.ok) { v.retry = 60; continue; }
    const item = r.body.data?.item ?? r.body.data ?? {};
    if (item.status === "done") { save(v, item); pending.splice(pending.indexOf(v), 1); } else v.retry = Number(item.retry_after_seconds ?? 60);
  }
}
for (const v of pending) problems.push(`《${v.title}》还在识别：24 小时内运行 dataxapi call ${TR} job=${v.job} 取文字（取到才扣费）`);

// ---------- 4. index and combined file ----------
const esc = (s) => (/[",\n]/.test(String(s ?? "")) ? `"${String(s).replace(/"/g, '""')}"` : String(s ?? ""));
const cols = ["published_at", "title", "duration_seconds", "status", "characters", "file", "url", "job"];
writeFileSync(join(OUT, "index.csv"), "﻿" + [cols.join(","), ...videos.map((v) => [v.published_at, v.title, v.duration, v.status ?? "skipped", (v.text ?? "").length, v.file ?? "", v.url, v.job ?? ""].map(esc).join(","))].join("\n"));
const done = videos.filter((v) => v.status === "done");
writeFileSync(join(OUT, "all.md"), done.map((v) => `## ${v.published_at.slice(0, 10)} ${v.title}\n\n${v.text || "（没有人说话）"}\n`).join("\n"));
console.log([
  `# 视频转文字稿 · ${PLATFORM} ${ID ?? URL_}`, "",
  `- ${videos.length} 条视频：转好 ${done.length} 条，没人说话（只有音乐或静音，不收费）${videos.filter((v) => v.status === "no_speech").length} 条，还在识别 ${pending.length} 条，失败 ${videos.filter((v) => v.status === "failed").length} 条。`,
  `- 每条一个文件，在 ${OUT}/；索引表 ${OUT}/index.csv；全部合在 ${OUT}/all.md。`,
  `- 本次花费 $${Math.round(spent * 10000) / 10000}（作品列表 + 转文字）。`,
  ...(problems.length ? ["", "## 没转成的", "", ...problems.map((p) => `- ${p}`)] : []),
  "", `数据来源：DataXAPI，取数时间 ${new Date().toISOString()}`,
].join("\n"));
