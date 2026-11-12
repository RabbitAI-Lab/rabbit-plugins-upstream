#!/usr/bin/env node
// deadline-radar: upcoming deadlines from a deadlines.md file, joined with the state of the git repo each deadline
// belongs to, so an agent can warn "due in 3 days and the repo has uncommitted changes". Read-only: it runs only
// `git status`, `git log` and `git rev-parse` in repos inside --root, and makes no network calls.
//
// deadlines.md lines:  - <when> | <course or project> | <what> | repo: <path>      (repo is optional)
// <when> is "YYYY-MM-DD HH:MM" or "every <Weekday> HH:MM" for weekly work, in the --tz time zone.
//
// Usage: node deadline_radar.mjs [--file deadlines.md] [--root .] [--days 7] [--alert-days 3] [--tz America/Los_Angeles]
// Prints JSON: { timezone, deadlines: [{ course, what, due, daysLeft, weekly, repo? }], alerts: [text] }
//
// Same logic as the deadline_radar tool in the author's CSCI 599 A3 assistant (a3-skills/radar.mjs); a parity
// test there keeps the two in step. Self-contained here so it runs on a fresh OpenClaw install.
import { execFile } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";

const run = promisify(execFile);
const WEEKDAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"];

// --- time-zone helpers (wall-clock times in an IANA zone, DST-safe) ---
function offsetMinutes(tz, date) {
  const name = new Intl.DateTimeFormat("en-US", { timeZone: tz, timeZoneName: "longOffset" }).formatToParts(date)
    .find((p) => p.type === "timeZoneName").value;                       // e.g. "GMT-08:00"
  const m = /GMT([+-])(\d{2}):(\d{2})/.exec(name);
  return m ? (m[1] === "-" ? -1 : 1) * (Number(m[2]) * 60 + Number(m[3])) : 0;
}
export function zonedTime(tz, day, hhmm) {                                // the instant of <day> <hh:mm> in tz
  const guess = new Date(`${day}T${hhmm}:00Z`);
  let t = new Date(guess.getTime() - offsetMinutes(tz, guess) * 60_000);
  const second = offsetMinutes(tz, t);                                    // correct across a DST change
  if (second !== offsetMinutes(tz, guess)) t = new Date(guess.getTime() - second * 60_000);
  return t;
}
const zonedDate = (tz, date) => date.toLocaleDateString("en-CA", { timeZone: tz });   // YYYY-MM-DD
const addDays = (day, n) => new Date(Date.parse(`${day}T12:00:00Z`) + n * 86_400_000).toISOString().slice(0, 10);

export function parseDeadlines(text) {
  const out = [];
  for (const line of String(text).split("\n")) {
    const m = /^\s*-\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*(?:\|\s*repo:\s*(\S+)\s*)?\|?\s*$/.exec(line);
    if (!m) continue;
    const [, when, course, what, repo] = m;
    const weekly = /^every\s+(\w+)\s+(\d{1,2}:\d{2})$/i.exec(when);
    const fixed = /^(\d{4}-\d{2}-\d{2})\s+(\d{1,2}:\d{2})$/.exec(when);
    if (weekly && WEEKDAYS.includes(weekly[1].toLowerCase())) out.push({ weekday: WEEKDAYS.indexOf(weekly[1].toLowerCase()), time: weekly[2].padStart(5, "0"), course, what, repo: repo || null });
    else if (fixed) out.push({ day: fixed[1], time: fixed[2].padStart(5, "0"), course, what, repo: repo || null });
  }
  return out;
}

// The next due moment of a deadline at or after `now` (a weekly one rolls to the next week once passed).
export function nextDue(d, now, tz) {
  if (d.day) return zonedTime(tz, d.day, d.time);
  const today = zonedDate(tz, now);
  for (let i = 0; i < 8; i++) {
    const day = addDays(today, i);
    if (new Date(`${day}T12:00:00Z`).getUTCDay() !== d.weekday) continue;
    const due = zonedTime(tz, day, d.time);
    if (due >= now) return due;
  }
  return null;
}

async function repoState(repoRoot, rel) {
  const root = path.resolve(repoRoot);
  const dir = path.resolve(root, rel);
  if (!dir.startsWith(root + path.sep) || !fs.existsSync(path.join(dir, ".git"))) return { path: rel, found: false };
  const git = (...args) => run("git", ["-C", dir, ...args], { timeout: 10_000, env: { PATH: process.env.PATH, HOME: process.env.HOME } })
    .then((r) => r.stdout.trim());
  const status = await git("status", "--porcelain=v1");
  const last = await git("log", "-1", "--format=%cI|%s").catch(() => "");
  const [lastAt, lastMsg] = last.split("|");
  return {
    path: rel, found: true, branch: await git("rev-parse", "--abbrev-ref", "HEAD").catch(() => "?"),
    uncommittedFiles: status ? status.split("\n").length : 0,
    lastCommit: lastAt ? { at: lastAt, message: lastMsg, daysAgo: Math.floor((Date.now() - new Date(lastAt)) / 86_400_000) } : null,
  };
}

export async function radar({ deadlinesFile, repoRoot, days = 7, alertDays = 3, now = new Date(), tz = "America/Los_Angeles" }) {
  if (!deadlinesFile || !fs.existsSync(deadlinesFile)) return { timezone: tz, deadlines: [], alerts: [], note: "no deadlines file found" };
  const horizon = now.getTime() + days * 86_400_000;
  const items = [];
  for (const d of parseDeadlines(fs.readFileSync(deadlinesFile, "utf8"))) {
    const due = nextDue(d, now, tz);
    if (!due || due < now || due.getTime() > horizon) continue;
    const item = {
      course: d.course, what: d.what, weekly: d.weekday !== undefined,
      due: due.toLocaleString("en-US", { timeZone: tz, weekday: "short", month: "short", day: "numeric", hour: "numeric", minute: "2-digit" }),
      daysLeft: Math.round(((due - now) / 86_400_000) * 10) / 10,
    };
    if (d.repo) item.repo = await repoState(repoRoot, d.repo);
    items.push(item);
  }
  items.sort((a, b) => a.daysLeft - b.daysLeft);
  const alerts = items.filter((i) => i.daysLeft <= alertDays && i.repo?.uncommittedFiles > 0)
    .map((i) => `${i.course}: "${i.what}" is due ${i.due} (in ${i.daysLeft} days) and ${i.repo.path} has ${i.repo.uncommittedFiles} uncommitted change(s)` +
                (i.repo.lastCommit ? `; last commit ${i.repo.lastCommit.daysAgo} day(s) ago` : ""));
  return { timezone: tz, deadlines: items, alerts };
}

// --- command line ---
if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const args = process.argv.slice(2);
  const opt = (name, dflt) => { const i = args.indexOf(name); return i >= 0 && args[i + 1] ? args[i + 1] : dflt; };
  const num = (name, dflt) => { const n = Number(opt(name, dflt)); return Number.isFinite(n) && n > 0 && n <= 365 ? n : dflt; };
  const root = opt("--root", ".");
  radar({ deadlinesFile: path.resolve(opt("--file", path.join(root, "deadlines.md"))), repoRoot: root,
          days: num("--days", 7), alertDays: num("--alert-days", 3), tz: opt("--tz", "America/Los_Angeles") })
    .then((r) => console.log(JSON.stringify(r, null, 2)))
    .catch((err) => { console.error(JSON.stringify({ error: err.message })); process.exit(1); });
}
