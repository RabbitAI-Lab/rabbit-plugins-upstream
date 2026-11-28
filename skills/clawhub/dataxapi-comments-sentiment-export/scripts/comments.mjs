#!/usr/bin/env node
// 导出评论做口碑分析：一条或几条抖音视频、小红书笔记、公众号文章下面的评论，连同回复，存成 CSV。
// Export the comments, with replies, under Douyin videos, Xiaohongshu notes or WeChat articles to one CSV.
//
//   node comments.mjs --platform douyin|xiaohongshu|wechat_mp --posts <链接或编号>[,<链接或编号>…]
//                     [--pages 5] [--replies 10] [--sort latest|popular] [--max-spend 1] [--out comments.csv] [--plan]
// --pages: pages of top-level comments per post; --replies: the replies of the K comments with the most replies.
import { spawnSync } from "node:child_process";
import { existsSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";

const SOURCE = "skill.comments-sentiment-export";
const CAPS = {
  douyin: { list: "douyin.videos.comments.list", replies: "douyin.comments.replies.list" },
  xiaohongshu: { list: "xiaohongshu.notes.comments.list", replies: "xiaohongshu.comments.replies.list" },
  wechat_mp: { list: "wechat_mp.articles.comments.list", replies: "wechat_mp.comments.replies.list" },
};
const args = process.argv.slice(2);
const flag = (name, fallback) => { const i = args.indexOf(`--${name}`); return i === -1 ? fallback : args[i + 1]; };
const PLATFORM = flag("platform");
const POSTS = (flag("posts") ?? "").split(/\s*,\s*(?=https?:|\d|[0-9a-f]{24})/).map((s) => s.trim()).filter(Boolean);
const PAGES = Number(flag("pages", "5"));
const REPLIES = Number(flag("replies", "10"));
const SORT = flag("sort", "");
const MAX_SPEND = Number(flag("max-spend", "1"));
const OUT = flag("out", `comments-${PLATFORM}-${new Date().toISOString().slice(0, 10)}.csv`);
const PLAN = args.includes("--plan");
if (!CAPS[PLATFORM] || !POSTS.length) { console.error("要 --platform douyin|xiaohongshu|wechat_mp 和 --posts <链接或编号>（几条用逗号隔开）"); process.exit(2); }
const { list: LIST, replies: REPLY } = CAPS[PLATFORM];

const cli = spawnSync("dataxapi", ["--help"]).error ? ["npx", "-y", "dataxapi"] : ["dataxapi"];
const run = (argv) => spawnSync(cli[0], [...cli.slice(1), ...argv], { encoding: "utf8" });
const prices = new Map();
const priceOf = (cap) => {
  if (!prices.has(cap)) {
    const r = run(["show", cap, "--json"]);
    if (r.status !== 0) throw new Error(`读不到 ${cap} 的价格：${r.stderr}`);
    prices.set(cap, Number(JSON.parse(r.stdout).capability.pricing.max_charge));
  }
  return prices.get(cap);
};
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
  return { ok: false, exit: r.status, fatal: r.status === 2 && /no API key|insufficient_balance|key_budget_exceeded/.test(lines.join(" ")),
    message: `${zh ?? lines[0]}（退出码 ${r.status}${r.status === 4 ? "，不确定是否扣费：先 dataxapi more 查，不要重发" : "，没扣费"}）` };
}

// A post is given as a link (url) or an ID; WeChat articles only by link.
const postParams = (p) => (/^https?:|\s/.test(p) || PLATFORM === "wechat_mp" ? { url: p } : { id: p });
const most = Math.round(POSTS.length * (PAGES * priceOf(LIST) + REPLIES * priceOf(REPLY)) * 10000) / 10000;
console.log(`计划：${POSTS.length} 条内容，每条最多 ${PAGES} 页评论（约 ${PLATFORM === "xiaohongshu" ? 10 : 20} 条一页），回复最多的 ${REPLIES} 条评论各取一次回复。最多花 $${most}（价格读自线上目录）。`);
if (PLAN) process.exit(0);
if (most > MAX_SPEND) { console.error(`最多可能花 $${most}，超过 --max-spend ${MAX_SPEND}：告诉用户，他同意后用 --max-spend ${most} 再跑。`); process.exit(2); }

const rows = [];
const problems = [];
const row = (post, c, level) => ({
  post, level, comment_id: c.id, parent_id: level === "回复" ? (c.parent_id ?? c.root_id ?? "") : "",
  author: c.author?.name ?? "", text: (c.text ?? "").replace(/\s+/g, " "), likes: c.metrics?.likes ?? "",
  replies: c.metrics?.comments ?? "", published_at: c.published_at ?? "", ip_location: c.ext?.ip_location ?? "",
});
outer: for (const post of POSTS) {
  const top = [];
  let cursor = null;
  for (let page = 0; page < PAGES; page += 1) {
    const r = call(LIST, { ...postParams(post), view: "full", ...(SORT && PLATFORM === "xiaohongshu" ? { sort: SORT } : {}), ...(cursor ? { cursor } : {}) });
    if (!r.ok) { problems.push(`${post} 第 ${page + 1} 页评论没取到：${r.message}`); if (r.fatal) break outer; break; }
    const items = r.body.data?.items ?? [];
    if (!items.length && page === 0) problems.push(`${post} 没有评论，或链接/编号不对`);
    top.push(...items);
    cursor = r.body.page?.has_more ? r.body.page.next_cursor : null;
    if (!cursor) break;
  }
  if (cursor) problems.push(`${post} 还有更多评论没取（只取了 ${PAGES} 页，要更多用 --pages 调大）`);
  for (const c of top) rows.push(row(post, c, "评论"));
  const withReplies = top.filter((c) => (c.metrics?.comments ?? 0) > 0).sort((a, b) => b.metrics.comments - a.metrics.comments).slice(0, REPLIES);
  for (const c of withReplies) {
    // The replies endpoints take the comment's ID and the post it is under: its post_id, or for WeChat the article link.
    const r = call(REPLY, { id: c.id, post_id: PLATFORM === "wechat_mp" ? post : (c.post_id ?? post), view: "full" });
    if (!r.ok) { problems.push(`评论 ${c.id} 的回复没取到：${r.message}`); if (r.fatal) break outer; continue; }
    for (const x of r.body.data?.items ?? []) rows.push(row(post, { ...x, parent_id: x.parent_id ?? c.id }, "回复"));
  }
}

const cols = ["post", "level", "comment_id", "parent_id", "author", "text", "likes", "replies", "published_at", "ip_location"];
const esc = (v) => (/[",\n]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : String(v));
writeFileSync(OUT, "﻿" + [cols.join(","), ...rows.map((r) => cols.map((c) => esc(r[c] ?? "")).join(","))].join("\n"));
const n = (lvl) => rows.filter((r) => r.level === lvl).length;
console.log([
  `# 评论导出 · ${PLATFORM}`, "",
  `- ${POSTS.length} 条内容，评论 ${n("评论")} 条、回复 ${n("回复")} 条，存在 ${OUT}（Excel 可直接打开；列：内容、层级、评论编号、回复的是哪条、作者、正文、点赞、回复数、时间、IP 属地）。`,
  `- 本次花费 $${Math.round(spent * 10000) / 10000}。`,
  ...(problems.length ? ["", "## 没取全的", "", ...problems.map((p) => `- ${p}`)] : []),
  "", `数据来源：DataXAPI，取数时间 ${new Date().toISOString()}`,
].join("\n"));
