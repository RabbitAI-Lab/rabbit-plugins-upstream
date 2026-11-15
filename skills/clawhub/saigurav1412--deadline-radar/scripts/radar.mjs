#!/usr/bin/env node
/**
 * Deadline Radar: reads deadlines.md and reports what's close, including whether
 * a deadline's git repo has work that hasn't been committed or pushed.
 *
 * It has no dependencies and works in two ways: run directly from the command line,
 * or imported by a plugin tool on agents that have their shell turned off.
 */
import { execFile } from "node:child_process";
import { existsSync, readFileSync, realpathSync } from "node:fs";
import { isAbsolute, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const MS_PER_DAY = 86_400_000;
const GIT_TIMEOUT_MS = 10_000;
export const DEFAULT_WITHIN_DAYS = 3;

/** Calendar date math in UTC, so a daylight saving change can't shift the count by a day. */
function dateToUtcMs(date) {
  const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(date);
  if (!match) return null;
  const [year, month, day] = [Number(match[1]), Number(match[2]), Number(match[3])];
  const ms = Date.UTC(year, month - 1, day);
  const check = new Date(ms);
  // Date.UTC rolls over quietly, so 2026-02-31 would otherwise become March 3.
  if (check.getUTCMonth() !== month - 1 || check.getUTCDate() !== day) return null;
  return ms;
}

/** Today's date in a time zone. A server usually runs in UTC, so the zone has to be explicit. */
export function todayIn(timeZone, now = new Date()) {
  const parts = new Intl.DateTimeFormat("en-CA", { timeZone, year: "numeric", month: "2-digit", day: "2-digit" }).formatToParts(now);
  const part = (type) => parts.find((p) => p.type === type).value;
  return `${part("year")}-${part("month")}-${part("day")}`;
}

/**
 * Parse deadline lines. Only bullets that look like an attempt at a deadline count:
 * a malformed one becomes a reported problem, because silently skipping it would hide
 * a deadline the user is relying on. Headings, notes and other bullets are ignored.
 */
export function parseDeadlines(text) {
  const deadlines = [];
  const problems = [];
  text.split(/\r?\n/).forEach((rawLine, index) => {
    const bullet = /^\s*[-*]\s+(.*)$/.exec(rawLine);
    if (!bullet) return;
    const body = bullet[1].trim();
    if (!/^\d/.test(body) && !body.includes("|")) return;

    const line = index + 1;
    const [date = "", title = "", ...options] = body.split("|").map((field) => field.trim());
    if (dateToUtcMs(date) === null) {
      problems.push({ line, problem: `"${date}" is not a real date in YYYY-MM-DD form` });
      return;
    }
    if (!title) {
      problems.push({ line, problem: "the deadline has no title" });
      return;
    }

    const deadline = { line, date, title, done: false };
    for (const option of options) {
      if (option.toLowerCase() === "done") deadline.done = true;
      else if (option.toLowerCase().startsWith("repo:")) deadline.repo = option.slice(5).trim();
      else problems.push({ line, problem: `unknown option "${option}"` });
    }
    deadlines.push(deadline);
  });
  return { deadlines, problems };
}

/** Whole days from today to the date. Negative means overdue. */
export function daysUntil(date, today) {
  return Math.round((dateToUtcMs(date) - dateToUtcMs(today)) / MS_PER_DAY);
}

/** Read `git status --porcelain=v1 --branch` output into counts. */
export function parseGitStatus(output) {
  const lines = output.split("\n").filter(Boolean);
  const branchLine = lines[0]?.startsWith("## ") ? lines[0] : "";
  return {
    uncommitted: lines.length - (branchLine ? 1 : 0),
    ahead: Number(/\bahead (\d+)/.exec(branchLine)?.[1] ?? 0),
    behind: Number(/\bbehind (\d+)/.exec(branchLine)?.[1] ?? 0),
    hasUpstream: branchLine.includes("..."),
  };
}

/**
 * Resolve a repo path, refusing anything outside the workspace.
 *
 * The real path is compared, so a symlink can't lead out. deadlines.md may be edited by
 * an agent that has read untrusted content, so its paths aren't trusted either.
 */
export function resolveRepoPath(workspace, repo) {
  const root = realpathSync(workspace);
  const target = resolve(root, repo);
  if (!existsSync(target)) throw new Error("the repo path doesn't exist");
  const real = realpathSync(target);
  const fromRoot = relative(root, real);
  if (fromRoot.startsWith("..") || isAbsolute(fromRoot)) throw new Error("the repo is outside the workspace");
  // Without this check, git would walk up and silently report on a parent repo instead.
  if (!existsSync(join(real, ".git"))) throw new Error("the path isn't a git repository");
  return real;
}

/**
 * Run `git status` safely.
 *
 * A repo's own config can make `git status` run programs: core.fsmonitor names a
 * command to execute. Command-line settings override repo config, so these keep a
 * hostile repo from running code when it's only being inspected. Only counts are
 * returned, so file names never reach the model.
 */
export function readRepoStatus(repoPath) {
  const args = [
    "-c", "core.fsmonitor=false",
    "-c", "core.hooksPath=/dev/null",
    "--no-optional-locks",
    "-C", repoPath,
    "status", "--porcelain=v1", "--branch",
  ];
  const env = { PATH: process.env.PATH, HOME: process.env.HOME, GIT_TERMINAL_PROMPT: "0", GIT_OPTIONAL_LOCKS: "0" };
  return new Promise((resolvePromise, reject) => {
    execFile("git", args, { timeout: GIT_TIMEOUT_MS, env }, (error, stdout) => {
      if (error) reject(new Error("git couldn't read the repo"));
      else resolvePromise(parseGitStatus(stdout));
    });
  });
}

function plural(count, word) {
  return `${count} ${word}${count === 1 ? "" : "s"}`;
}

function describeDue(days) {
  if (days < 0) return `was due ${plural(-days, "day")} ago`;
  if (days === 0) return "is due today";
  if (days === 1) return "is due tomorrow";
  return `is due in ${days} days`;
}

/** Work that could be lost or left out of a submission, in plain words. */
function describeRepo(repo, status) {
  const issues = [];
  if (status.uncommitted) issues.push(plural(status.uncommitted, "uncommitted change"));
  if (status.ahead) issues.push(plural(status.ahead, "unpushed commit"));
  if (status.behind) issues.push(`is ${plural(status.behind, "commit")} behind its remote`);
  if (!status.hasUpstream) issues.push("no remote branch to push to");
  return issues.length ? `Repo ${repo}: ${issues.join(", ")}.` : `Repo ${repo} is clean and pushed.`;
}

/** Build the full report. The repo reader can be swapped out in tests. */
export async function buildReport({ text, workspace, today, withinDays = DEFAULT_WITHIN_DAYS, readStatus = readRepoStatus }) {
  const { deadlines, problems } = parseDeadlines(text);
  const alerts = [];
  const upcoming = [];
  const open = deadlines
    .filter((deadline) => !deadline.done)
    .sort((a, b) => a.date.localeCompare(b.date));

  for (const deadline of open) {
    const days = daysUntil(deadline.date, today);
    const entry = { date: deadline.date, title: deadline.title, daysUntil: days };
    if (days > withinDays) {
      upcoming.push(entry);
      continue;
    }
    let repoSummary = "";
    if (deadline.repo) {
      // Repos are only inspected for close deadlines, to keep each check quick.
      try {
        const status = await readStatus(resolveRepoPath(workspace, deadline.repo));
        entry.repo = { path: deadline.repo, ...status };
        repoSummary = ` ${describeRepo(deadline.repo, status)}`;
      } catch (error) {
        problems.push({ line: deadline.line, problem: `repo ${deadline.repo}: ${error.message}` });
      }
    }
    entry.message = `⏰ ${deadline.title} ${describeDue(days)} (${deadline.date}).${repoSummary}`;
    alerts.push(entry);
  }
  return { today, withinDays, alerts, upcoming, problems };
}

/** Read deadlines.md from the workspace. A missing file is normal for a new user. */
export function readDeadlinesFile(workspace) {
  const path = join(workspace, "deadlines.md");
  return existsSync(path) ? readFileSync(path, "utf8") : "";
}

function parseArgs(argv) {
  const options = { workspace: process.cwd(), within: DEFAULT_WITHIN_DAYS, timezone: Intl.DateTimeFormat().resolvedOptions().timeZone };
  for (let i = 0; i < argv.length; i += 2) {
    const [flag, value] = [argv[i], argv[i + 1]];
    if (value === undefined) throw new Error(`${flag} needs a value`);
    if (flag === "--workspace") options.workspace = value;
    else if (flag === "--within") options.within = Number(value);
    else if (flag === "--timezone") options.timezone = value;
    else throw new Error(`unknown option ${flag}`);
  }
  if (!Number.isInteger(options.within) || options.within < 0) throw new Error("--within must be a whole number of days");
  return options;
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  const report = await buildReport({
    text: readDeadlinesFile(options.workspace),
    workspace: options.workspace,
    today: todayIn(options.timezone),
    withinDays: options.within,
  });
  console.log(JSON.stringify(report, null, 2));
}

// Run only when called directly, not when imported by the plugin or tests.
if (process.argv[1] && realpathSync(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch((error) => {
    console.error(`deadline-radar: ${error.message}`);
    process.exit(2);
  });
}
