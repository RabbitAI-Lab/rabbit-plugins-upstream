#!/usr/bin/env node
import crypto from "node:crypto";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";
import {
  BACKUP_REL,
  DAILY_RE,
  LOCK_REL,
  STATE_REL,
  canonicalRoot,
  exists,
  fail,
  memoryScopeSnapshot,
  readJson,
  safePath,
  sha256File,
  writeJsonAtomic,
  writeTextAtomic,
} from "./common.mjs";
import { PLAN_SCHEMA, nextState, renderDiary } from "./delta-state.mjs";
import { auditWorkspace } from "./dream-audit.mjs";

export const MANIFEST_SCHEMA = "signal-dreaming.run-manifest.v3";
const RUN_ID_RE = /^\d{8}-\d{6}-[a-f0-9]{6}$/;

export function createRunId(now = new Date()) {
  const stamp = now.toISOString().replace(/\D/g, "").slice(0, 14);
  return `${stamp.slice(0, 8)}-${stamp.slice(8)}-${crypto.randomBytes(3).toString("hex")}`;
}

export function validateWritePath(input) {
  const relative = input.replaceAll("\\", "/");
  if (relative === "MEMORY.md" || relative === "memory/dream-log.md") return relative;
  const match = relative.match(/^memory\/([^/]+\.md)$/);
  if (!match || DAILY_RE.test(match[1])) {
    throw fail("INVALID_WRITE_TARGET", `not an allowed memory write target: ${input}`);
  }
  return relative;
}

async function manifestPath(root, runId) {
  return (await safePath(root, `${BACKUP_REL}/${runId}/manifest.json`)).lexical;
}

async function lockPath(root) {
  return (await safePath(root, LOCK_REL)).lexical;
}

function processAlive(pid) {
  if (!Number.isSafeInteger(pid) || pid <= 0) return false;
  try {
    process.kill(pid, 0);
    return true;
  } catch {
    return false;
  }
}

async function listUnreviewedRuns(root) {
  const backup = (await safePath(root, BACKUP_REL)).lexical;
  if (!(await exists(backup))) return [];
  const blocked = [];
  for (const entry of await fs.readdir(backup, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const file = path.join(backup, entry.name, "manifest.json");
    if (!(await exists(file))) continue;
    const manifest = await readJson(file);
    if (["started", "backed_up", "incomplete"].includes(manifest.status) && !manifest.reviewedAt) {
      blocked.push({ runId: manifest.runId, status: manifest.status });
    }
  }
  return blocked;
}

async function assertNoLock(root) {
  const file = await lockPath(root);
  if (!(await exists(file))) return;
  const lock = await readJson(file, LOCK_REL);
  if (lock.hostname === os.hostname() && processAlive(lock.pid)) {
    throw fail("RUN_ACTIVE", `run ${lock.runId} is active`);
  }
  throw fail("STALE_LOCK", `stale lock for ${lock.runId}: inspect its manifest/backups, restore or reconcile live files, then acknowledge that exact run id`);
}

async function markIncomplete(root, runId, reason) {
  const file = await manifestPath(root, runId);
  if (!(await exists(file))) return;
  const manifest = await readJson(file);
  manifest.status = "incomplete";
  manifest.incompleteAt = new Date().toISOString();
  manifest.incompleteReason = reason;
  await writeJsonAtomic(file, manifest);
}

export async function beginRun(workspaceInput, runId, plan, writePaths, dependencies = {}) {
  const root = await canonicalRoot(workspaceInput);
  if (!RUN_ID_RE.test(runId)) throw fail("RUN_ID", "run id must be YYYYMMDD-HHMMSS-xxxxxx");
  if (plan?.schema !== PLAN_SCHEMA || plan.root !== root || plan.noop) {
    throw fail("PLAN_INVALID", "a non-noop delta plan for this workspace is required");
  }
  if (!Array.isArray(writePaths) || writePaths.length === 0) throw fail("WRITE_PLAN_EMPTY", "write plan is empty");
  const normalized = [...new Set(writePaths.map(validateWritePath))];
  if (!normalized.includes("memory/dream-log.md")) {
    throw fail("DIARY_NOT_PLANNED", "every successful dream must plan memory/dream-log.md");
  }
  await assertNoLock(root);
  const unfinished = await listUnreviewedRuns(root);
  if (unfinished.length) throw fail("INCOMPLETE_RUN", "an earlier run requires manual review", { unfinished });
  const scopeSnapshot = await memoryScopeSnapshot(root);

  const file = await manifestPath(root, runId);
  if (await exists(file)) throw fail("RUN_EXISTS", `run id already exists: ${runId}`);
  const lock = await lockPath(root);
  await fs.mkdir(path.dirname(lock), { recursive: true });
  const lockBody = {
    schema: "signal-dreaming.run-lock.v3",
    runId,
    pid: process.pid,
    hostname: os.hostname(),
    startedAt: new Date().toISOString(),
  };
  await fs.writeFile(lock, `${JSON.stringify(lockBody, null, 2)}\n`, { flag: "wx", mode: 0o600 });

  const runDir = path.dirname(file);
  const copyFile = dependencies.copyFile ?? fs.copyFile;
  const manifest = {
    schema: MANIFEST_SCHEMA,
    runId,
    status: "started",
    startedAt: lockBody.startedAt,
    root,
    plan,
    plannedFiles: [],
    scopeSnapshot,
  };
  await writeJsonAtomic(file, manifest);
  try {
    for (const relative of normalized) {
      const resolved = await safePath(root, relative, { rejectSymlink: true });
      const record = {
        path: relative,
        existed: resolved.present,
        originalSha256: resolved.present ? await sha256File(resolved.real) : null,
        backupPath: resolved.present ? `${BACKUP_REL}/${runId}/files/${relative}.bak` : null,
      };
      if (resolved.present) {
        const backup = await safePath(root, record.backupPath);
        await fs.mkdir(path.dirname(backup.lexical), { recursive: true });
        await copyFile(resolved.real, backup.lexical);
        if (await sha256File(backup.lexical) !== record.originalSha256) {
          throw fail("BACKUP_HASH", `backup verification failed for ${relative}`);
        }
      }
      manifest.plannedFiles.push(record);
    }
    manifest.status = "backed_up";
    manifest.backedUpAt = new Date().toISOString();
    await writeJsonAtomic(file, manifest);
    return manifest;
  } catch (error) {
    await markIncomplete(root, runId, `backup failed: ${error.code ?? error.message}`);
    throw error;
  }
}

export async function verifyBeforeWrite(workspaceInput, runId) {
  const root = await canonicalRoot(workspaceInput);
  const file = await manifestPath(root, runId);
  const manifest = await readJson(file);
  if (manifest.status !== "backed_up") throw fail("RUN_STATUS", "run is not ready for writes");
  for (const planned of manifest.plannedFiles) {
    if (!planned.existed) continue;
    const live = await safePath(root, planned.path, { mustExist: true, kind: "file", rejectSymlink: true });
    if (await sha256File(live.real) !== planned.originalSha256) {
      await markIncomplete(root, runId, `live hash changed before write: ${planned.path}`);
      throw fail("LIVE_HASH_CHANGED", `live hash changed before write: ${planned.path}`);
    }
  }
  for (const input of manifest.plan.selectedLogs) {
    const live = await safePath(root, input.path, { mustExist: true, kind: "file", rejectSymlink: true });
    if (await sha256File(live.real) !== input.sha256) {
      await markIncomplete(root, runId, `daily input changed before write: ${input.path}`);
      throw fail("DAILY_INPUT_CHANGED", `daily input changed before write: ${input.path}`);
    }
  }
  manifest.writeCheckAt = new Date().toISOString();
  await writeJsonAtomic(file, manifest);
  return manifest;
}

export async function finalizeRun(workspaceInput, runId, entry, options = {}) {
  const root = await canonicalRoot(workspaceInput);
  const file = await manifestPath(root, runId);
  const manifest = await readJson(file);
  if (manifest.status !== "backed_up" || !manifest.writeCheckAt) {
    throw fail("RUN_STATUS", "verify-before-write must pass before finalize");
  }
  const touched = manifest.plannedFiles.map((item) => item.path);
  const diaryRecord = manifest.plannedFiles.find((item) => item.path === "memory/dream-log.md");
  if (!diaryRecord) throw fail("DIARY_NOT_PLANNED", "dream diary is not in the write plan");
  const preAudit = await auditWorkspace(root, {
    manifest,
    files: touched,
    allowUnchanged: ["memory/dream-log.md"],
  });
  if (!preAudit.ok) {
    await markIncomplete(root, runId, `pre-diary audit failed: ${preAudit.errors.map((item) => item.code).join(",")}`);
    return { ok: false, audit: preAudit };
  }
  if (!entry || entry.number !== manifest.plan.diary.nextDreamNumber) {
    await markIncomplete(root, runId, "dream number mismatch");
    return { ok: false, audit: preAudit, error: { code: "DIARY_NUMBER" } };
  }
  if (preAudit.semanticReviewRequired.length && !options.semanticReviewConfirmed) {
    return {
      ok: false,
      audit: preAudit,
      error: { code: "SEMANTIC_REVIEW_REQUIRED", files: preAudit.semanticReviewRequired },
    };
  }

  const diary = await safePath(root, "memory/dream-log.md", { mustExist: true, kind: "file", rejectSymlink: true });
  if (diaryRecord.existed && await sha256File(diary.real) !== diaryRecord.originalSha256) {
    await markIncomplete(root, runId, "dream diary changed before guarded append");
    return { ok: false, audit: preAudit, error: { code: "DIARY_LIVE_HASH_CHANGED" } };
  }
  try {
    await writeTextAtomic(diary.real, await renderDiary(root, entry));
  } catch (error) {
    await markIncomplete(root, runId, `diary render/write failed: ${error.code ?? error.message}`);
    return { ok: false, audit: preAudit, error: { code: error.code ?? "DIARY_WRITE_FAILED" } };
  }
  const audit = await auditWorkspace(root, { manifest, files: touched });
  if (!audit.ok) {
    if (diaryRecord.existed) {
      const backup = await safePath(root, diaryRecord.backupPath, { mustExist: true, kind: "file", rejectSymlink: true });
      await fs.copyFile(backup.real, diary.real);
    }
    await markIncomplete(root, runId, `final audit failed: ${audit.errors.map((item) => item.code).join(",")}`);
    return { ok: false, audit };
  }
  const dreamNumber = entry.number;
  const successfulAt = options.successfulAt ?? new Date().toISOString();
  const state = nextState(manifest.plan, successfulAt, dreamNumber);
  const statePath = (await safePath(root, STATE_REL)).lexical;
  await writeJsonAtomic(statePath, state);
  manifest.status = "committed";
  manifest.committedAt = successfulAt;
  manifest.stateSha256 = await sha256File(statePath);
  manifest.finalFiles = {};
  for (const planned of manifest.plannedFiles) {
    const live = await safePath(root, planned.path, { mustExist: true, kind: "file", rejectSymlink: true });
    manifest.finalFiles[planned.path] = await sha256File(live.real);
  }
  manifest.audit = {
    memoryBytes: audit.memoryBytes,
    warnings: audit.warnings,
    semanticReviewRequired: audit.semanticReviewRequired,
  };
  await writeJsonAtomic(file, manifest);
  const lock = await lockPath(root);
  if (await exists(lock)) {
    const lockBody = await readJson(lock);
    if (lockBody.runId === runId) await fs.unlink(lock);
  }
  return { ok: true, manifest, audit, state };
}

export async function failRun(workspaceInput, runId, reason) {
  const root = await canonicalRoot(workspaceInput);
  await markIncomplete(root, runId, reason);
  const lock = await lockPath(root);
  if (await exists(lock)) {
    const current = await readJson(lock);
    if (current.runId === runId) await fs.unlink(lock);
  }
}

export async function acknowledgeIncomplete(workspaceInput, runId, confirm) {
  const root = await canonicalRoot(workspaceInput);
  if (confirm !== runId) throw fail("CONFIRMATION", "confirmation must exactly match run id");
  const file = await manifestPath(root, runId);
  const manifest = await readJson(file);
  if (!["started", "backed_up", "incomplete"].includes(manifest.status)) {
    throw fail("RUN_STATUS", "only unfinished runs can be acknowledged");
  }
  const lock = await lockPath(root);
  if (await exists(lock)) {
    const current = await readJson(lock);
    if (current.runId === runId && current.hostname === os.hostname() && processAlive(current.pid)) {
      throw fail("RUN_ACTIVE", "cannot acknowledge a live run");
    }
    if (current.runId === runId) await fs.unlink(lock);
  }
  manifest.status = "incomplete";
  manifest.reviewedAt = new Date().toISOString();
  await writeJsonAtomic(file, manifest);
  return manifest;
}

async function main() {
  const [command, workspace, ...args] = process.argv.slice(2);
  if (!command || !workspace) {
    throw fail("USAGE", "usage: run-guard.mjs create-run-id|begin|verify-before-write|finalize|fail|ack-incomplete ...");
  }
  if (command === "create-run-id") {
    process.stdout.write(`${createRunId()}\n`);
    return;
  }
  if (command === "begin") {
    const [runId, planFile, ...writePaths] = args;
    const plan = await readJson(path.resolve(planFile), planFile);
    process.stdout.write(`${JSON.stringify(await beginRun(workspace, runId, plan, writePaths), null, 2)}\n`);
    return;
  }
  if (command === "verify-before-write") {
    process.stdout.write(`${JSON.stringify(await verifyBeforeWrite(workspace, args[0]), null, 2)}\n`);
    return;
  }
  if (command === "finalize") {
    const runId = args.shift();
    const entryFile = args.shift();
    if (!entryFile) throw fail("USAGE", "finalize requires an entry JSON file");
    const entry = await readJson(path.resolve(entryFile), entryFile);
    const semanticReviewConfirmed = args.shift() === "--semantic-review-confirmed";
    const result = await finalizeRun(workspace, runId, entry, { semanticReviewConfirmed });
    process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
    if (!result.ok) process.exitCode = 2;
    return;
  }
  if (command === "fail") {
    await failRun(workspace, args.shift(), args.join(" ") || "manual failure");
    return;
  }
  if (command === "ack-incomplete") {
    const runId = args.shift();
    if (args.shift() !== "--confirm") throw fail("USAGE", "ack-incomplete requires --confirm <run-id>");
    process.stdout.write(`${JSON.stringify(await acknowledgeIncomplete(workspace, runId, args.shift()), null, 2)}\n`);
    return;
  }
  throw fail("USAGE", `unknown command: ${command}`);
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? "").href) {
  main().catch((error) => {
    process.stderr.write(`${JSON.stringify({ ok: false, code: error.code ?? "ERROR", message: error.message })}\n`);
    process.exitCode = 2;
  });
}
