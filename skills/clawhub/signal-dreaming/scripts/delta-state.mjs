#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import {
  STATE_REL,
  canonicalRoot,
  exists,
  fail,
  listDailyLogs,
  parseDreamLog,
  readJson,
  safePath,
  sha256File,
  trimAndAppendDream,
} from "./common.mjs";

export const PLAN_SCHEMA = "signal-dreaming.delta-plan.v3";
export const STATE_SCHEMA_VERSION = 3;
export const DEFAULT_BOOTSTRAP_DAYS = 7;
export const MAX_LOGS_PER_RUN = 32;
export const MAX_INPUT_BYTES = 512 * 1024;

function dateOf(relative) {
  return relative.slice("memory/".length, "memory/".length + 10);
}

function cutoffDate(now, days) {
  const value = new Date(now);
  if (Number.isNaN(value.valueOf())) throw fail("INVALID_TIME", `invalid time: ${now}`);
  value.setUTCDate(value.getUTCDate() - (days - 1));
  return value.toISOString().slice(0, 10);
}

async function readState(root) {
  const statePath = (await safePath(root, STATE_REL)).lexical;
  if (!(await exists(statePath))) return { state: null, mode: "bootstrap" };
  let state;
  try {
    state = await readJson(statePath, STATE_REL);
  } catch (error) {
    throw fail("STATE_INVALID", "state is corrupt; review it, then use quarantine-state with its exact SHA-256 to enter bounded bootstrap");
  }
  if (state.schemaVersion !== STATE_SCHEMA_VERSION || typeof state.dailyLogs !== "object" || Array.isArray(state.dailyLogs)) {
    throw fail("STATE_SCHEMA_UNSUPPORTED", "state schema is unknown; no automatic migration is allowed; review it, then use quarantine-state with its exact SHA-256");
  }
  return { state, mode: "incremental" };
}

function bounded(files, options) {
  const selected = [];
  let bytes = 0;
  for (const file of files) {
    if (file.size > options.maxBytes) {
      throw fail("LOG_TOO_LARGE", `${file.path} exceeds the per-run input byte ceiling`);
    }
    if (selected.length >= options.maxLogs || bytes + file.size > options.maxBytes) break;
    selected.push(file);
    bytes += file.size;
  }
  return {
    selected,
    bytes,
    deferred: files.slice(selected.length),
  };
}

export async function buildDeltaPlan(workspaceInput, options = {}) {
  const root = await canonicalRoot(workspaceInput);
  const limits = {
    bootstrapDays: options.bootstrapDays ?? DEFAULT_BOOTSTRAP_DAYS,
    maxLogs: options.maxLogs ?? MAX_LOGS_PER_RUN,
    maxBytes: options.maxBytes ?? MAX_INPUT_BYTES,
  };
  const now = options.now ?? new Date().toISOString();
  const bootstrapCutoff = cutoffDate(now, limits.bootstrapDays);
  const { state, mode } = await readState(root);
  const allLogs = await listDailyLogs(root);
  const diary = await safePath(root, "memory/dream-log.md", { mustExist: true, kind: "file", rejectSymlink: true });
  const parsedDiary = parseDreamLog(await fs.readFile(diary.real, "utf8"));
  if (parsedDiary.malformed.length || parsedDiary.duplicates.length || parsedDiary.descending.length) {
    throw fail("DIARY_INVALID", "dream diary must be repaired before planning a write");
  }

  let candidates;
  if (mode === "bootstrap") {
    if (options.fullHistory) candidates = allLogs;
    else candidates = allLogs.filter((file) => dateOf(file.path) >= bootstrapCutoff);
  } else {
    const missing = Object.keys(state.dailyLogs).filter((relative) => !allLogs.some((file) => file.path === relative));
    if (missing.length) throw fail("DAILY_LOG_MISSING", "tracked daily logs are missing; daily logs must never be moved or deleted", { missing });
    candidates = allLogs.filter((file) => {
      const previous = state.dailyLogs[file.path];
      if (previous) return previous.sha256 !== file.sha256;
      return Boolean(options.fullHistory) || dateOf(file.path) >= (state.bootstrapCutoff ?? bootstrapCutoff);
    });
  }

  candidates = candidates.toSorted((a, b) => a.path.localeCompare(b.path));
  const batch = bounded(candidates, limits);
  return {
    schema: PLAN_SCHEMA,
    createdAt: now,
    root,
    mode,
    fullHistory: Boolean(options.fullHistory),
    limits,
    bootstrapCutoff: state?.bootstrapCutoff ?? bootstrapCutoff,
    discoveredLogs: allLogs.length,
    selectedLogs: batch.selected,
    deferredLogs: batch.deferred.map((file) => file.path),
    selectedBytes: batch.bytes,
    batchCapped: batch.deferred.length > 0,
    noop: batch.selected.length === 0,
    stateBefore: state,
    diary: {
      entryCount: parsedDiary.entries.length,
      lastDreamNumber: parsedDiary.max,
      nextDreamNumber: parsedDiary.max + 1,
      gaps: parsedDiary.gaps,
    },
  };
}

export function nextState(plan, successfulAt, dreamNumber) {
  if (plan.schema !== PLAN_SCHEMA) throw fail("PLAN_SCHEMA", "unsupported delta plan");
  if (dreamNumber !== plan.diary.nextDreamNumber) throw fail("DIARY_NUMBER", "dream number does not match the plan");
  const previous = plan.stateBefore?.dailyLogs ?? {};
  const dailyLogs = { ...previous };
  for (const file of plan.selectedLogs) {
    dailyLogs[file.path] = {
      sha256: file.sha256,
      size: file.size,
      mtimeMs: file.mtimeMs,
    };
  }
  return {
    schemaVersion: STATE_SCHEMA_VERSION,
    lastSuccessfulRun: successfulAt,
    lastDreamNumber: dreamNumber,
    bootstrapCutoff: plan.stateBefore?.bootstrapCutoff ?? plan.bootstrapCutoff,
    dailyLogs: Object.fromEntries(Object.entries(dailyLogs).toSorted(([a], [b]) => a.localeCompare(b))),
  };
}

export async function renderDiary(workspaceInput, entry) {
  const root = await canonicalRoot(workspaceInput);
  const diary = await safePath(root, "memory/dream-log.md", { mustExist: true, kind: "file", rejectSymlink: true });
  return trimAndAppendDream(await fs.readFile(diary.real, "utf8"), entry);
}

export async function inspectState(workspaceInput) {
  const root = await canonicalRoot(workspaceInput);
  const state = await safePath(root, STATE_REL, { mustExist: true, kind: "file", rejectSymlink: true });
  const stat = await fs.stat(state.real);
  return {
    schema: "signal-dreaming.state-inspection.v3",
    path: STATE_REL,
    sha256: await sha256File(state.real),
    bytes: stat.size,
  };
}

export async function quarantineState(workspaceInput, confirmation, options = {}) {
  const root = await canonicalRoot(workspaceInput);
  const state = await safePath(root, STATE_REL, { mustExist: true, kind: "file", rejectSymlink: true });
  const hash = await sha256File(state.real);
  if (confirmation !== hash) throw fail("CONFIRMATION", "confirmation must exactly match the current state SHA-256");
  const now = options.now ?? new Date().toISOString();
  const stamp = new Date(now);
  if (Number.isNaN(stamp.valueOf())) throw fail("INVALID_TIME", `invalid time: ${now}`);
  const digits = stamp.toISOString().replace(/\D/g, "").slice(0, 17);
  const run = `${digits.slice(0, 8)}-${digits.slice(8, 14)}-${digits.slice(14)}-${hash.slice(0, 8)}`;
  const backupRelative = `.backup/memory-dreams/state-recovery/${run}/state.json.bak`;
  const backup = await safePath(root, backupRelative);
  if (await exists(backup.lexical)) throw fail("BACKUP_EXISTS", `state recovery backup already exists: ${backupRelative}`);
  await fs.mkdir(path.dirname(backup.lexical), { recursive: true });
  await fs.copyFile(state.real, backup.lexical);
  if (await sha256File(backup.lexical) !== hash) throw fail("BACKUP_HASH", "state recovery backup hash mismatch");
  if (await sha256File(state.real) !== hash) throw fail("LIVE_HASH_CHANGED", "state changed during recovery; original was not removed");
  await fs.unlink(state.real);
  return {
    schema: "signal-dreaming.state-quarantine.v3",
    ok: true,
    original: STATE_REL,
    backup: backupRelative,
    sha256: hash,
    next: "rerun plan for bounded bootstrap",
  };
}

function parseArgs(argv) {
  const command = argv.shift();
  const workspace = argv.shift();
  if (!command || !workspace) {
    throw fail("USAGE", "usage: delta-state.mjs plan|render-diary|inspect-state|quarantine-state <workspace-root> [options]");
  }
  return { command, workspace, rest: argv };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.command === "plan") {
    const options = {};
    while (args.rest.length) {
      const arg = args.rest.shift();
      if (arg === "--full-history") options.fullHistory = true;
      else if (arg === "--now") options.now = args.rest.shift();
      else throw fail("USAGE", `unknown argument: ${arg}`);
    }
    process.stdout.write(`${JSON.stringify(await buildDeltaPlan(args.workspace, options), null, 2)}\n`);
    return;
  }
  if (args.command === "render-diary") {
    const input = args.rest.shift();
    if (!input || args.rest.length) throw fail("USAGE", "render-diary requires one entry JSON file");
    const entry = JSON.parse(await fs.readFile(path.resolve(input), "utf8"));
    process.stdout.write(await renderDiary(args.workspace, entry));
    return;
  }
  if (args.command === "quarantine-state") {
    if (args.rest.shift() !== "--confirm") throw fail("USAGE", "quarantine-state requires --confirm <state-sha256>");
    const confirmation = args.rest.shift();
    if (!confirmation || args.rest.length) throw fail("USAGE", "quarantine-state requires exactly one SHA-256 confirmation");
    process.stdout.write(`${JSON.stringify(await quarantineState(args.workspace, confirmation), null, 2)}\n`);
    return;
  }
  if (args.command === "inspect-state") {
    if (args.rest.length) throw fail("USAGE", "inspect-state does not accept extra arguments");
    process.stdout.write(`${JSON.stringify(await inspectState(args.workspace), null, 2)}\n`);
    return;
  }
  throw fail("USAGE", `unknown command: ${args.command}`);
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? "").href) {
  main().catch((error) => {
    process.stderr.write(`${JSON.stringify({ ok: false, code: error.code ?? "ERROR", message: error.message })}\n`);
    process.exitCode = 2;
  });
}
