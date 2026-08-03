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

async function releaseRunLock(root, runId) {
  const lock = await lockPath(root);
  if (!(await exists(lock))) return;
  const current = await readJson(lock);
  if (current.runId === runId) await fs.unlink(lock);
}

async function seedCandidateScope(root, runId) {
  const relative = BACKUP_REL + "/" + runId + "/candidate";
  const candidate = await safePath(root, relative);
  await fs.mkdir(path.join(candidate.lexical, "memory"), { recursive: true });
  const liveMemory = await safePath(root, "memory", { mustExist: true, kind: "directory" });
  const liveIndex = await safePath(root, "MEMORY.md", { mustExist: true, kind: "file", rejectSymlink: true });
  await fs.copyFile(liveIndex.real, path.join(candidate.lexical, "MEMORY.md"));
  for (const entry of await fs.readdir(liveMemory.real, { withFileTypes: true })) {
    if (!entry.isFile() || !entry.name.endsWith(".md") || DAILY_RE.test(entry.name) || entry.name.startsWith(".")) continue;
    const source = await safePath(root, "memory/" + entry.name, { mustExist: true, kind: "file", rejectSymlink: true });
    await fs.copyFile(source.real, path.join(candidate.lexical, "memory", entry.name));
  }
  return {
    relative,
    root: candidate.lexical,
    snapshot: await memoryScopeSnapshot(candidate.lexical),
  };
}

async function verifyLiveScope(root, manifest) {
  const current = await memoryScopeSnapshot(root);
  for (const [relative, hash] of Object.entries(manifest.scopeSnapshot)) {
    if (current[relative] !== hash) throw fail("LIVE_SCOPE_CHANGED", "live memory changed during candidate work: " + relative);
  }
  for (const relative of Object.keys(current)) {
    if (!(relative in manifest.scopeSnapshot)) throw fail("LIVE_SCOPE_CHANGED", "new live memory file appeared during candidate work: " + relative);
  }
}

async function verifyCommittedScope(root, manifest) {
  const expected = { ...manifest.scopeSnapshot };
  for (const relative of manifest.appliedFiles ?? []) {
    expected[relative] = manifest.candidateFiles[relative];
  }
  const current = await memoryScopeSnapshot(root);
  for (const [relative, hash] of Object.entries(expected)) {
    if (current[relative] !== hash) throw fail("COMMIT_SCOPE_CHANGED", "live memory changed during commit: " + relative);
  }
  for (const relative of Object.keys(current)) {
    if (!(relative in expected)) throw fail("COMMIT_SCOPE_CHANGED", "new live memory file appeared during commit: " + relative);
  }
}

async function candidateScopeErrors(candidateRoot, manifest, allowUnchanged = []) {
  const current = await memoryScopeSnapshot(candidateRoot);
  const base = manifest.candidateBaseSnapshot;
  const planned = new Set(manifest.plannedFiles.map((item) => item.path));
  const allowed = new Set(allowUnchanged);
  const errors = [];
  for (const [relative, hash] of Object.entries(base)) {
    if (!(relative in current)) errors.push({ code: "CANDIDATE_DELETE", message: "candidate file disappeared: " + relative, file: relative });
    else if (current[relative] !== hash && !planned.has(relative)) {
      errors.push({ code: "UNPLANNED_CANDIDATE_CHANGE", message: "unplanned candidate file changed: " + relative, file: relative });
    }
  }
  for (const relative of Object.keys(current)) {
    if (!(relative in base) && !planned.has(relative)) {
      errors.push({ code: "UNPLANNED_CANDIDATE_CREATE", message: "unplanned candidate file appeared: " + relative, file: relative });
    }
  }
  for (const item of manifest.plannedFiles) {
    if (!(item.path in current)) errors.push({ code: "PLANNED_CANDIDATE_MISSING", message: "planned candidate is missing: " + item.path, file: item.path });
    else if (item.existed && current[item.path] === item.originalSha256 && !allowed.has(item.path)) {
      errors.push({ code: "PLANNED_CANDIDATE_UNCHANGED", message: "planned candidate was not changed: " + item.path, file: item.path });
    }
  }
  return errors;
}

async function rejectCandidate(root, runId, manifest, reason, audit = null) {
  manifest.status = "candidate_rejected";
  manifest.rejectedAt = new Date().toISOString();
  manifest.rejectionReason = reason;
  if (audit) manifest.rejectionAudit = {
    memoryBytes: audit.memoryBytes,
    errors: audit.errors.map((item) => ({ code: item.code, file: item.file })),
    warnings: audit.warnings,
  };
  await writeJsonAtomic(await manifestPath(root, runId), manifest);
  await releaseRunLock(root, runId);
  return { ok: false, candidateRejected: true, audit, error: { code: reason } };
}

function mergeAuditErrors(audit, errors) {
  audit.errors.push(...errors);
  audit.ok = audit.errors.length === 0;
  return audit;
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
    if (["started", "backed_up", "staged", "ready_to_commit", "incomplete"].includes(manifest.status) && !manifest.reviewedAt) {
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
    const candidate = await seedCandidateScope(root, runId);
    manifest.candidateRoot = candidate.relative;
    manifest.candidateBaseSnapshot = candidate.snapshot;
    for (const record of manifest.plannedFiles) {
      record.candidatePath = candidate.relative + "/" + record.path;
    }
    manifest.status = "staged";
    manifest.stagedAt = new Date().toISOString();
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
  if (manifest.status !== "staged") throw fail("RUN_STATUS", "run is not ready for candidate edits");
  try {
    for (const planned of manifest.plannedFiles) {
      if (!planned.existed) continue;
      const live = await safePath(root, planned.path, { mustExist: true, kind: "file", rejectSymlink: true });
      if (await sha256File(live.real) !== planned.originalSha256) {
        throw fail("LIVE_HASH_CHANGED", "live hash changed before candidate edit: " + planned.path);
      }
    }
    for (const input of manifest.plan.selectedLogs) {
      const live = await safePath(root, input.path, { mustExist: true, kind: "file", rejectSymlink: true });
      if (await sha256File(live.real) !== input.sha256) {
        throw fail("DAILY_INPUT_CHANGED", "daily input changed before candidate edit: " + input.path);
      }
    }
    await verifyLiveScope(root, manifest);
    const candidateRoot = (await safePath(root, manifest.candidateRoot, { mustExist: true, kind: "directory", rejectSymlink: true })).real;
    const candidateScope = await memoryScopeSnapshot(candidateRoot);
    if (JSON.stringify(candidateScope) !== JSON.stringify(manifest.candidateBaseSnapshot)) {
      throw fail("CANDIDATE_BASE_CHANGED", "candidate files changed before verify-before-write");
    }
  } catch (error) {
    await rejectCandidate(root, runId, manifest, error.code ?? "VERIFY_FAILED");
    throw error;
  }
  manifest.writeCheckAt = new Date().toISOString();
  await writeJsonAtomic(file, manifest);
  return manifest;
}


export async function finalizeRun(workspaceInput, runId, entry, options = {}) {
  const root = await canonicalRoot(workspaceInput);
  const file = await manifestPath(root, runId);
  const manifest = await readJson(file);
  if (manifest.status !== "staged" || !manifest.writeCheckAt) {
    throw fail("RUN_STATUS", "verify-before-write must pass before finalize");
  }
  const touched = manifest.plannedFiles.map((item) => item.path);
  const diaryRecord = manifest.plannedFiles.find((item) => item.path === "memory/dream-log.md");
  if (!diaryRecord) throw fail("DIARY_NOT_PLANNED", "dream diary is not in the write plan");
  const candidateRoot = (await safePath(root, manifest.candidateRoot, {
    mustExist: true, kind: "directory", rejectSymlink: true,
  })).real;

  try {
    await verifyLiveScope(root, manifest);
  } catch (error) {
    return rejectCandidate(root, runId, manifest, error.code ?? "LIVE_SCOPE_CHANGED");
  }

  let preAudit = await auditWorkspace(candidateRoot, { files: touched });
  preAudit = mergeAuditErrors(preAudit, await candidateScopeErrors(candidateRoot, manifest, ["memory/dream-log.md"]));
  if (manifest.plan.index?.maintenanceRequired && manifest.plan.selectedLogs.length === 0
    && Number.isSafeInteger(preAudit.memoryBytes) && preAudit.memoryBytes >= manifest.plan.index.size) {
    preAudit = mergeAuditErrors(preAudit, [{
      code: "NO_COMPACTION_PROGRESS",
      message: "maintenance-only candidate did not reduce MEMORY.md",
      file: "MEMORY.md",
    }]);
  }
  if (!preAudit.ok) {
    return rejectCandidate(root, runId, manifest, "CANDIDATE_AUDIT_FAILED", preAudit);
  }
  if (preAudit.semanticReviewRequired.length && !options.semanticReviewConfirmed) {
    return {
      ok: false,
      audit: preAudit,
      error: { code: "SEMANTIC_REVIEW_REQUIRED", files: preAudit.semanticReviewRequired },
    };
  }

  try {
    const diary = await safePath(candidateRoot, "memory/dream-log.md", {
      mustExist: true, kind: "file", rejectSymlink: true,
    });
    await writeTextAtomic(diary.real, await renderDiary(candidateRoot, entry));
  } catch (error) {
    return rejectCandidate(root, runId, manifest, error.code ?? "DIARY_RENDER_FAILED", preAudit);
  }

  let audit = await auditWorkspace(candidateRoot, { files: touched });
  audit = mergeAuditErrors(audit, await candidateScopeErrors(candidateRoot, manifest));
  if (!audit.ok) {
    return rejectCandidate(root, runId, manifest, "FINAL_CANDIDATE_AUDIT_FAILED", audit);
  }

  try {
    await verifyLiveScope(root, manifest);
  } catch (error) {
    return rejectCandidate(root, runId, manifest, error.code ?? "LIVE_SCOPE_CHANGED", audit);
  }

  const candidateMemory = await safePath(candidateRoot, "MEMORY.md", {
    mustExist: true, kind: "file", rejectSymlink: true,
  });
  const candidateStat = await fs.stat(candidateMemory.real);
  const candidateIndex = {
    sha256: await sha256File(candidateMemory.real),
    size: candidateStat.size,
  };
  manifest.status = "ready_to_commit";
  manifest.commitStartedAt = new Date().toISOString();
  manifest.appliedFiles = [];
  manifest.candidateFiles = {};
  for (const item of manifest.plannedFiles) {
    const candidate = await safePath(candidateRoot, item.path, {
      mustExist: true, kind: "file", rejectSymlink: true,
    });
    manifest.candidateFiles[item.path] = await sha256File(candidate.real);
  }
  await writeJsonAtomic(file, manifest);

  const commitOrder = manifest.plannedFiles.toSorted((a, b) => {
    const rank = (value) => value.path === "memory/dream-log.md" ? 2 : value.path === "MEMORY.md" ? 1 : 0;
    return rank(a) - rank(b) || a.path.localeCompare(b.path);
  });
  try {
    for (const item of commitOrder) {
      const candidate = await safePath(candidateRoot, item.path, {
        mustExist: true, kind: "file", rejectSymlink: true,
      });
      const live = await safePath(root, item.path, { rejectSymlink: true });
      if (item.existed) {
        if (!live.present || await sha256File(live.real) !== item.originalSha256) {
          throw fail("LIVE_HASH_CHANGED", "planned live file changed immediately before commit: " + item.path);
        }
      } else if (live.present) {
        throw fail("NEW_TARGET_APPEARED", "planned new file appeared immediately before commit: " + item.path);
      }
      await writeTextAtomic(live.lexical, await fs.readFile(candidate.real, "utf8"));
      manifest.appliedFiles.push(item.path);
      await writeJsonAtomic(file, manifest);
    }
    for (const input of manifest.plan.selectedLogs) {
      const live = await safePath(root, input.path, { mustExist: true, kind: "file", rejectSymlink: true });
      if (await sha256File(live.real) !== input.sha256) {
        throw fail("DAILY_INPUT_CHANGED", "daily input changed during commit: " + input.path);
      }
    }
    await verifyCommittedScope(root, manifest);
    const successfulAt = options.successfulAt ?? new Date().toISOString();
    const state = nextState(manifest.plan, successfulAt, entry.number, candidateIndex);
    const statePath = (await safePath(root, STATE_REL)).lexical;
    await writeJsonAtomic(statePath, state);

    manifest.status = "committed";
    manifest.committedAt = successfulAt;
    manifest.stateSha256 = await sha256File(statePath);
    manifest.finalFiles = {};
    for (const item of manifest.plannedFiles) {
      const live = await safePath(root, item.path, {
        mustExist: true, kind: "file", rejectSymlink: true,
      });
      manifest.finalFiles[item.path] = await sha256File(live.real);
    }
    manifest.audit = {
      memoryBytes: audit.memoryBytes,
      warnings: audit.warnings,
      semanticReviewRequired: audit.semanticReviewRequired,
    };
    await writeJsonAtomic(file, manifest);
    await releaseRunLock(root, runId);
    return { ok: true, manifest, audit, state };
  } catch (error) {
    const applied = manifest.appliedFiles.join(", ");
    await markIncomplete(root, runId, "live commit failed after [" + applied + "]: " + (error.code ?? error.message));
    await releaseRunLock(root, runId);
    return { ok: false, audit, error: { code: error.code ?? "LIVE_COMMIT_FAILED" } };
  }
}


export async function failRun(workspaceInput, runId, reason) {
  const root = await canonicalRoot(workspaceInput);
  const file = await manifestPath(root, runId);
  const manifest = await readJson(file);
  if (["started", "backed_up", "staged"].includes(manifest.status) && !(manifest.appliedFiles?.length)) {
    await rejectCandidate(root, runId, manifest, reason || "CANDIDATE_FAILED");
    return;
  }
  await markIncomplete(root, runId, reason);
  await releaseRunLock(root, runId);
}

export async function acknowledgeIncomplete(workspaceInput, runId, confirm) {
  const root = await canonicalRoot(workspaceInput);
  if (confirm !== runId) throw fail("CONFIRMATION", "confirmation must exactly match run id");
  const file = await manifestPath(root, runId);
  const manifest = await readJson(file);
  if (!["started", "backed_up", "staged", "ready_to_commit", "incomplete"].includes(manifest.status)) {
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
