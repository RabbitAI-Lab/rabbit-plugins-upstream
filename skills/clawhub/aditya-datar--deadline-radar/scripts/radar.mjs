#!/usr/bin/env node
// deadline-radar: deadlines due soon + repo activity -> at-risk report.
// Zero dependencies (Node >= 18). Read-only: never writes files or modifies repos.
import fs from "node:fs";
import path from "node:path";
import { execFile } from "node:child_process";
import { promisify } from "node:util";

const run = promisify(execFile);

function parseArgs(argv) {
  const out = { within: 7, json: false, alert: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--json") out.json = true;
    else if (a === "--alert") out.alert = true;
    else if (a === "--file") out.file = argv[++i];
    else if (a === "--within") out.within = Number(argv[++i]);
    else if (a === "--tz") out.tz = argv[++i];
    else if (a === "--now") out.now = argv[++i]; // testing aid: ISO instant
    else if (a === "--help" || a === "-h") out.help = true;
  }
  return out;
}

export function parseDeadlines(markdown) {
  const out = [];
  for (const line of markdown.split("\n")) {
    if (!line.trim().startsWith("|")) continue;
    const cells = line.split("|").slice(1, -1).map((c) => c.trim());
    const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(cells[0] || "");
    if (!m) continue;
    out.push({ due: cells[0], y: +m[1], mo: +m[2], d: +m[3], item: cells[1] || "", project: cells[2] || "", repo: cells[3] || "" });
  }
  return out;
}

export function daysLeft(entry, now, tz) {
  const p = Object.fromEntries(
    new Intl.DateTimeFormat("en-US", { timeZone: tz, year: "numeric", month: "2-digit", day: "2-digit" }).formatToParts(now).map((x) => [x.type, x.value]),
  );
  const today = Date.UTC(+p.year, +p.month - 1, +p.day);
  return Math.round((Date.UTC(entry.y, entry.mo - 1, entry.d) - today) / 86400000);
}

async function localRepo(repo) {
  try {
    const { stdout } = await run("git", ["-C", repo, "status", "--porcelain", "--branch"], { timeout: 10000 });
    const lines = stdout.split("\n").filter(Boolean);
    const ahead = /ahead (\d+)/.exec(lines.find((l) => l.startsWith("##")) || "");
    return { kind: "local", uncommitted: lines.filter((l) => !l.startsWith("##")).length, unpushed: ahead ? +ahead[1] : 0 };
  } catch (e) {
    return { kind: "local", error: String(e.message || e).split("\n")[0].slice(0, 120) };
  }
}

async function githubRepo(spec, now) {
  const repo = spec.slice("github:".length);
  if (!/^[\w.-]+\/[\w.-]+$/.test(repo)) return { kind: "github", error: "invalid github:owner/repo" };
  try {
    const res = await fetch(`https://api.github.com/repos/${repo}/commits?per_page=1`, {
      headers: { Accept: "application/vnd.github+json", "User-Agent": "deadline-radar" },
      signal: AbortSignal.timeout(10000),
    });
    if (!res.ok) return { kind: "github", error: `GitHub HTTP ${res.status}` };
    const [c] = await res.json();
    const when = c?.commit?.committer?.date;
    return { kind: "github", lastPushAt: when || null, hoursSincePush: when ? Math.round((now - new Date(when)) / 3600000) : null };
  } catch (e) {
    return { kind: "github", error: String(e.message || e).slice(0, 120) };
  }
}

export function assessRisk(entry) {
  const reasons = [];
  const r = entry.repoStatus;
  if (entry.daysLeft <= 3) {
    if (r?.uncommitted > 0) reasons.push(`${r.uncommitted} uncommitted change(s)`);
    if (r?.unpushed > 0) reasons.push(`${r.unpushed} unpushed commit(s)`);
    if (r?.hoursSincePush != null && r.hoursSincePush > 48) reasons.push(`no push in ${r.hoursSincePush}h`);
    if (r?.error) reasons.push(`repo check failed (${r.error})`);
    if (entry.daysLeft <= 1 && !reasons.length) reasons.push(entry.repo ? "final stretch - confirm it is submitted" : "no repo linked to verify progress");
  }
  return reasons;
}

export async function radar({ file, within = 7, tz = process.env.TZ || "UTC", now = new Date() }) {
  const md = fs.readFileSync(file, "utf8");
  const items = parseDeadlines(md)
    .map((e) => ({ ...e, daysLeft: daysLeft(e, now, tz) }))
    .filter((e) => e.daysLeft >= 0 && e.daysLeft <= within)
    .sort((a, b) => a.daysLeft - b.daysLeft);
  for (const e of items) {
    if (e.repo.startsWith("github:")) e.repoStatus = await githubRepo(e.repo, now);
    else if (e.repo) e.repoStatus = await localRepo(e.repo);
    e.risks = assessRisk(e);
    e.atRisk = e.risks.length > 0;
  }
  return items.map(({ y, mo, d, ...rest }) => rest);
}

function render(items, alertOnly) {
  const shown = alertOnly ? items.filter((i) => i.atRisk) : items;
  if (!shown.length) return alertOnly ? "NO_REPLY" : "No deadlines in the window.";
  const lines = [alertOnly ? "⏳ Deadline risk" : "⏳ Upcoming deadlines"];
  for (const i of shown) {
    const when = i.daysLeft === 0 ? "today" : i.daysLeft === 1 ? "tomorrow" : `in ${i.daysLeft} days`;
    lines.push(`${i.atRisk ? "⚠" : "•"} ${i.item}${i.project ? ` (${i.project})` : ""} — due ${when}${i.atRisk ? `: ${i.risks.join(", ")}` : ""}`);
  }
  return lines.join("\n");
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    console.log("usage: radar.mjs [--file DEADLINES.md] [--within 7] [--tz Zone] [--json] [--alert]");
    return;
  }
  const candidates = [args.file, process.env.OPENCLAW_WORKSPACE && path.join(process.env.OPENCLAW_WORKSPACE, "DEADLINES.md"), "DEADLINES.md"].filter(Boolean);
  const file = candidates.find((f) => fs.existsSync(f));
  if (!file) {
    console.error(`deadline-radar: no DEADLINES.md found (tried: ${candidates.join(", ")})`);
    process.exit(2);
  }
  const items = await radar({ file, within: args.within, tz: args.tz, now: args.now ? new Date(args.now) : new Date() });
  console.log(args.json ? JSON.stringify({ file, items }, null, 2) : render(items, args.alert));
}

if (import.meta.url === `file://${process.argv[1]}` || process.argv[1]?.endsWith("radar.mjs")) {
  main().catch((e) => {
    console.error(`deadline-radar: ${e.message}`);
    process.exit(1);
  });
}
