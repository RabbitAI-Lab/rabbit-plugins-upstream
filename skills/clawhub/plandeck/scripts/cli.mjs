#!/usr/bin/env node
// cli.mjs — `plandeck <command>`.
//
// Dispatches the zero-dependency CLI and keeps human and JSON output aligned.
//   plandeck board <dir> [--once] [--json] [--port N] [--host H] [--actor NAME]
//   plandeck check <dir> [--json]
//   plandeck archive <dir> [--json] [--actor NAME]
//   plandeck next <dir> [--write] [--json] [--since HASH] [--actor NAME]
//   plandeck journal <dir> [--since ISO] [--limit N] [--json]
//   plandeck doctor <dir> [--restore TIMESTAMP|latest] [--json] [--actor NAME]
//   plandeck init [dir]
//   plandeck --help

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { createHash } from "node:crypto";
import { basename, dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { runBoard, PORT } from "./board.mjs";
import { checkPlan } from "./check-plan.mjs";
import { runDoctor } from "./doctor.mjs";
import { archiveDoneCards, atomicWriteFile, buildPayload, PlanError } from "./lib/deck.mjs";
import { observe } from "./lib/continuity.mjs";
import { describeEntry, readJournal, recentForNext } from "./lib/journal.mjs";
import { nextMarkdown } from "./lib/render.mjs";

const __dirname = dirname(fileURLToPath(import.meta.url));
const templatesDir = join(__dirname, "..", "templates");

async function dispatch(args) {
  const [command, ...rest] = args;
  const flags = parseFlags(rest);

  switch (command) {
    case "board":
      await runBoard({
        planDir: flags._[0] || ".",
        once: flags.once,
        json: flags.json,
        port: flags.port,
        host: flags.host,
        actor: flags.actor,
      });
      return;
    case "check": {
      const result = checkPlan(flags._[0] || ".", { json: flags.json });
      return result.ok ? 0 : 1;
    }
    case "archive":
      archivePlan(flags._[0] || ".", flags);
      return;
    case "next":
      printNext(flags._[0] || ".", flags);
      return;
    case "journal":
      printJournal(flags._[0] || ".", flags);
      return;
    case "doctor": {
      const result = runDoctor(flags._[0] || ".", { restore: flags.restore, json: flags.json, actor: flags.actor });
      return result.ok ? 0 : 1;
    }
    case "init":
      initPlan(flags._[0] || ".");
      return;
    case undefined:
    case "help":
    case "-h":
    case "--help":
      usage();
      return;
    default:
      console.error(`Unknown command: ${command}\n`);
      usage();
      return 1;
  }
}

function archivePlan(planDir, flags = {}) {
  const result = archiveDoneCards(planDir, Date.now(), { actor: flags.actor });
  if (flags.json) {
    console.log(JSON.stringify(result, null, 2));
    return;
  }
  if (!result.archived) {
    console.log("No done cards to archive.");
    return;
  }
  console.log(`Archived ${result.archived} card${result.archived === 1 ? "" : "s"} to ${result.archivePath}.`);
}

function printNext(planDir, flags = {}) {
  const root = resolve(planDir);
  const payload = buildPayload(root);
  observe(root, payload.cards, { actor: flags.actor });
  const stateHash = computeStateHash(payload.cards);
  if (flags.since === stateHash) {
    if (flags.json) console.log(JSON.stringify({ unchanged: true, stateHash }, null, 2));
    else console.log("unchanged");
    return;
  }
  const n = payload.nextAction;

  if (flags.write) {
    const dest = join(root, "NEXT.md");
    atomicWriteFile(dest, nextMarkdown(
      payload,
      `http://plandeck.localhost:${PORT}/${payload.plan.slug}/`,
      recentForNext(root, 5),
    ));
    console.log(`+ ${dest}`);
    return;
  }
  if (flags.json) {
    console.log(JSON.stringify({ next: n, criticalPath: payload.criticalPath.chain, pct: payload.rollup.pct, stateHash }, null, 2));
    return;
  }
  if (n?.reason === "complete") {
    console.log("✓ Every card is done. Run `plandeck check` for the completion audit.");
    return;
  }
  if (!n || n.reason === "empty") {
    console.log("→ No cards yet. Add the first card to plan.yaml.");
    return;
  }
  console.log(n.cardId ? `→ ${n.cardId}: ${n.title}` : "→ (no card)");
  console.log(`  ${n.detail}`);
  const ready = payload.cards.filter((c) => c.column === "ready").map((c) => c.id);
  if (ready.length) console.log(`  ready now: ${ready.join(", ")}`);
}

function printJournal(planDir, flags = {}) {
  const root = resolve(planDir);
  const since = flags.since === undefined ? undefined : requireIso(flags.since);
  const limit = flags.limit ?? (since === undefined ? 20 : undefined);
  const entries = readJournal(root, { since, limit });
  if (flags.json) {
    console.log(JSON.stringify({ planDir: root, count: entries.length, entries }, null, 2));
    return;
  }
  console.log(`Plandeck journal · ${basename(root)} (${entries.length} entries)`);
  for (const entry of entries) console.log(describeEntry(entry));
}

function computeStateHash(cards) {
  const tuples = (Array.isArray(cards) ? cards : [])
    .map((card) => [String(card.id), card.column ?? null, card.status ?? null])
    .sort((a, b) => a[0].localeCompare(b[0], undefined, { numeric: true }));
  return createHash("sha256").update(JSON.stringify(tuples)).digest("hex").slice(0, 12);
}

function initPlan(dir) {
  const target = resolve(dir);
  mkdirSync(join(target, "cards"), { recursive: true });
  for (const name of ["plan.yaml", "plan.md"]) {
    const dest = join(target, name);
    if (existsSync(dest)) { console.log(`· kept existing ${name}`); continue; }
    copyFileSync(join(templatesDir, name), dest);
    console.log(`+ ${name}`);
  }
  console.log(`\nPlan scaffolded in ${target}\nNext:  plandeck board ${dir}`);
}

function parseFlags(args) {
  const flags = {
    _: [], once: false, json: false, write: false,
    port: undefined, host: undefined, actor: undefined, since: undefined, limit: undefined, restore: undefined,
  };
  for (let i = 0; i < args.length; i += 1) {
    const a = args[i];
    if (a === "--once") flags.once = true;
    else if (a === "--write") flags.write = true;
    else if (a === "--json") flags.json = true;
    else if (a === "--port") flags.port = requirePort(takeValue(args, ++i, "--port"));
    else if (a.startsWith("--port=")) flags.port = requirePort(a.slice(7));
    else if (a === "--host") flags.host = takeValue(args, ++i, "--host");
    else if (a.startsWith("--host=")) flags.host = a.slice(7);
    else if (a === "--actor") flags.actor = takeValue(args, ++i, "--actor");
    else if (a.startsWith("--actor=")) flags.actor = a.slice(8);
    else if (a === "--since") flags.since = takeValue(args, ++i, "--since");
    else if (a.startsWith("--since=")) flags.since = a.slice(8);
    else if (a === "--limit") flags.limit = requireLimit(takeValue(args, ++i, "--limit"));
    else if (a.startsWith("--limit=")) flags.limit = requireLimit(a.slice(8));
    else if (a === "--restore") flags.restore = takeValue(args, ++i, "--restore");
    else if (a.startsWith("--restore=")) flags.restore = a.slice(10);
    else if (!a.startsWith("-")) flags._.push(a);
  }
  return flags;
}

function takeValue(args, i, flag) {
  const v = args[i];
  if (v === undefined || v.startsWith("-")) throw new Error(`${flag} needs a value.`);
  return v;
}

function requirePort(v) {
  const n = Number(v);
  if (!Number.isInteger(n) || n < 0 || n > 65535) {
    throw new Error(`--port needs a number 0..65535, got "${v}".`);
  }
  return n;
}

function requireLimit(v) {
  const n = Number(v);
  if (!Number.isInteger(n) || n < 1) {
    throw new Error(`--limit needs a positive integer, got "${v}".`);
  }
  return n;
}

function requireIso(v) {
  if (Number.isNaN(Date.parse(v))) throw new Error(`--since needs an ISO timestamp, got "${v}".`);
  return v;
}

function usage() {
  console.log(`Plandeck: a live visual Kanban for long-running AI agents.

Usage:
  plandeck board <dir> [--once] [--json] [--port N] [--host H] [--actor NAME]
  plandeck check <dir> [--json]
  plandeck archive <dir> [--json] [--actor NAME]
  plandeck next <dir> [--write] [--json] [--since HASH] [--actor NAME]
  plandeck journal <dir> [--since ISO] [--limit N] [--json]
  plandeck doctor <dir> [--restore TIMESTAMP|latest] [--json] [--actor NAME]
  plandeck init [dir]

Flags:
  --json            Machine-readable output
  --write           Write the generated NEXT.md atomically
  --port <n>        Board port (default ${PORT})
  --host <h>        Bind host (default 127.0.0.1)
  --actor <name>    Journal actor (or set PLANDECK_ACTOR)
  --since <value>   Journal ISO timestamp or next state hash
  --limit <n>       Maximum journal entries
  --restore <value> Snapshot timestamp or latest

Notes:
  Active hubs publish a verified temporary breadcrumb, including for ephemeral ports.
  Hub POST and DELETE requests require JSON and an approved loopback Host header.
  An unset velocity is observed after 3 dated completions spanning at least 1 day.`);
}

/** Run the CLI dispatcher. Exported so the zero-dependency suite can test it without child processes. */
export async function runCli(args = process.argv.slice(2), { setExitCode = false } = {}) {
  let code = 0;
  try {
    code = (await dispatch(args)) ?? 0;
  } catch (error) {
    const message = error.message || String(error);
    const hint = error instanceof PlanError ? "\nRun `plandeck doctor <dir>` to see recovery options." : "";
    console.error(`${message}${hint}`);
    code = 1;
  }
  if (setExitCode) process.exitCode = code;
  return code;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  void runCli(process.argv.slice(2), { setExitCode: true });
}
