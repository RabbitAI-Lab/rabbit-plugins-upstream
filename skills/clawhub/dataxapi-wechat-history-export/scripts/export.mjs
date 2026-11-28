#!/usr/bin/env node
// 导出某公众号全部历史文章到表格：一页一页往回翻文章列表，边翻边写进 CSV，到最早一篇、到 --since 那天、到页数或花费上限为止。
// Export a WeChat Official Account's article history to CSV, page by page, newest first, until the first article,
// the --since day, or the page or money cap. Within the hour a page cursor lasts, --continue goes on from where it stopped.
//
//   node export.mjs --id gh_xxx [--name 36氪] [--since 2025-01-01] [--max-pages 20] [--max-spend 1] [--tab articles]
//                   [--out 36kr.csv] [--continue] [--plan]
import { spawnSync } from "node:child_process";
import { appendFileSync, existsSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";

const SOURCE = "skill.wechat-history-export";
const CAP = "wechat_mp.accounts.articles.list";
const args = process.argv.slice(2);
const flag = (name, fallback) => { const i = args.indexOf(`--${name}`); return i === -1 ? fallback : args[i + 1]; };
const ID = flag("id");
const NAME = flag("name", ID);
const SINCE = flag("since", "");
const MAX_PAGES = Number(flag("max-pages", "20"));
const MAX_SPEND = Number(flag("max-spend", "1"));
const TAB = flag("tab", "articles");
const OUT = flag("out", `${(NAME ?? "wechat").replace(/[\\/:*?"<>|\s]/g, "_")}-articles.csv`);
const STATE = `${OUT}.state.json`;
const CONTINUE = args.includes("--continue");
const PLAN = args.includes("--plan");
if (!ID) { console.error("给 --id 公众号原始 ID（gh_ 开头居多）；只知道名字先查：dataxapi call wechat.accounts.search query=<名字>"); process.exit(2); }

const cli = spawnSync("dataxapi", ["--help"]).error ? ["npx", "-y", "dataxapi"] : ["dataxapi"];
const run = (argv) => spawnSync(cli[0], [...cli.slice(1), ...argv], { encoding: "utf8" });
const shown = run(["show", CAP, "--json"]);
if (shown.status !== 0) { console.error(`读不到价格：${shown.stderr}`); process.exit(1); }
const price = Number(JSON.parse(shown.stdout).capability.pricing.max_charge);
const pages = Math.min(MAX_PAGES, Math.floor(MAX_SPEND / price + 1e-9));
console.log(`计划：最多翻 ${pages} 页（每页约 30 篇），每页 $${price}，最多花 $${Math.round(pages * price * 10000) / 10000}（价格读自线上目录）。${SINCE ? `翻到 ${SINCE} 之前的文章就停。` : "翻到最早一篇就停。"}`);
if (PLAN) process.exit(0);

let cursor = null;
let seen = new Set();
const cols = ["account", "account_id", "published_at", "position", "content_type", "title", "digest", "url", "cover_url"];
if (CONTINUE) {
  if (!existsSync(STATE)) { console.error(`没有 ${STATE}：上次没留下翻页位置，去掉 --continue 从头导出`); process.exit(2); }
  const st = JSON.parse(readFileSync(STATE, "utf8"));
  if (st.id !== ID) { console.error(`${STATE} 是 ${st.id} 的，不是 ${ID}`); process.exit(2); }
  if (!st.cursor) { console.log("上次已经翻到头了，不用继续。"); process.exit(0); }
  if (Date.parse(st.cursor_expires_at) < Date.now()) { console.error(`翻页位置 ${st.cursor_expires_at} 已过期（一小时有效）：只能去掉 --continue 从头再导一次，已有的行会按编号去重`); process.exit(2); }
  cursor = st.cursor;
}
if (existsSync(OUT)) for (const line of readFileSync(OUT, "utf8").split("\n").slice(1)) { const id = line.match(/__biz=[^&]+&mid=\d+&idx=\d+/)?.[0]; if (id) seen.add(id); }
else writeFileSync(OUT, "﻿" + cols.join(",") + "\n");

const esc = (v) => (/[",\n]/.test(String(v ?? "")) ? `"${String(v).replace(/"/g, '""')}"` : String(v ?? ""));
let spent = 0, done = 0, added = 0, oldest = "", stop = "";
while (done < pages) {
  const out = join(tmpdir(), `dx-${process.pid}-${done}.json`);
  const argv = ["call", CAP, `id=${ID}`, `tab=${TAB}`, "view=full", ...(cursor ? [`cursor=${cursor}`] : []), "--max-price", String(price), "--source", SOURCE, "--out", out];
  let r = run(argv);
  if (r.status === 3 && /Retry: once/.test(`${r.stderr}${r.stdout}`)) { spawnSync("sleep", ["5"]); r = run(argv); }
  if (r.status !== 0 || !existsSync(out)) {
    const lines = `${r.stderr}${r.stdout}`.split("\n");
    stop = `第 ${done + 1} 页没取到（退出码 ${r.status}${r.status === 4 ? "，不确定是否扣费：先 dataxapi more 查，不要重发" : "，没扣费"}）：${lines.find((l) => l.startsWith("中文：")) ?? lines[0]}`;
    break;
  }
  const body = JSON.parse(readFileSync(out, "utf8")); rmSync(out, { force: true });
  spent += Number(body.meta?.billing?.amount ?? 0); done += 1;
  let reachedSince = false;
  for (const x of body.data?.items ?? []) {
    if (SINCE && (x.published_at ?? "") < SINCE) { reachedSince = true; continue; }
    const url = (x.url ?? "").replace(/^http:/, "https:").replace(/&chksm=.*$/, "");
    const key = url.match(/__biz=[^&]+&mid=\d+&idx=\d+/)?.[0] ?? x.id;
    if (seen.has(key)) continue;
    seen.add(key); added += 1;
    oldest = x.published_at ?? oldest;
    appendFileSync(OUT, [NAME, ID, x.published_at, x.ext?.position ?? "", x.ext?.content_type ?? "", x.title, x.text, url, x.ext?.cover_url ?? ""].map(esc).join(",") + "\n");
  }
  cursor = body.page?.has_more && !reachedSince ? body.page.next_cursor : null;
  writeFileSync(STATE, JSON.stringify({ id: ID, cursor, cursor_expires_at: body.page?.cursor_expires_at ?? null, pages_done: done, oldest }, null, 2));
  if (reachedSince) { stop = `已经翻到 ${SINCE} 之前。`; break; }
  if (!cursor) { stop = "已经翻到这个号最早的一篇。"; break; }
}
if (!stop) stop = `到了页数或花费上限（${done} 页）。还有更早的：一小时内用同样的参数加 --continue 接着翻。`;
const total = existsSync(OUT) ? readFileSync(OUT, "utf8").trim().split("\n").length - 1 : 0;
console.log([
  `# 公众号「${NAME}」历史文章导出`, "",
  `- 这次翻了 ${done} 页，新写入 ${added} 篇，表里共 ${total} 篇；最早一篇发于 ${oldest || "—"}。`,
  `- 停下的原因：${stop}`,
  `- 本次花费 $${Math.round(spent * 10000) / 10000}。表格：${OUT}（Excel 可直接打开；列：账号、发布时间、头条/次条位置、类型、标题、摘要、链接、封面）。`,
  "", `数据来源：DataXAPI，取数时间 ${new Date().toISOString()}`,
].join("\n"));
