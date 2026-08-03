#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { LOCK_REL } from "./common.mjs";
import { assertNoSymlinkComponents, resolveInside, resolveWorkspaceRoot, safeRegularOrMissing } from "./path-guard.mjs";

const V3_MANIFEST_SCHEMA = "signal-dreaming.run-manifest.v3";

function fail(message) {
  process.stdout.write(JSON.stringify({ ok: false, mode: "audit-only", error: message }) + "\n");
  process.exit(2);
}
function readJson(root, file, label) {
  try {
    if (safeRegularOrMissing(root, file) !== "file") throw new Error(`missing ${label}`);
    return JSON.parse(fs.readFileSync(file, "utf8"));
  } catch (error) {
    fail(`cannot read ${label}: ${error?.message || error}`);
  }
}
function safeRunId(value) {
  return typeof value === "string" && /^[A-Za-z0-9._-]+$/.test(value) && value !== "." && value !== "..";
}
function safeTargets(entries, { allowDiary = false } = {}) {
  if (!Array.isArray(entries)) return null;
  const targets = [];
  for (const entry of entries) {
    const rel = entry?.path;
    if (typeof rel !== "string") return null;
    if (rel === "MEMORY.md" || (allowDiary && rel === "memory/dream-log.md")) {
      targets.push(rel);
      continue;
    }
    if (!/^memory\/[^/]+\.md$/.test(rel) || /^memory\/\d{4}-\d{2}-\d{2}.*\.md$/.test(rel) || rel === "memory/dream-log.md") return null;
    targets.push(rel);
  }
  return targets;
}
function manifestFormat(manifest) {
  if (manifest?.schema === V3_MANIFEST_SCHEMA) return "v3";
  if (manifest?.version === 2) return "v2";
  return null;
}
function manifestWorkspace(manifest, format) {
  if (format === "v3") {
    if (typeof manifest.root !== "string") return null;
    if (Object.hasOwn(manifest, "workspace") && manifest.workspace !== manifest.root) return null;
    return manifest.root;
  }
  if (format === "v2") {
    if (typeof manifest.workspace !== "string") return null;
    if (Object.hasOwn(manifest, "root") && manifest.root !== manifest.workspace) return null;
    return manifest.workspace;
  }
  return null;
}
function manifestTargets(manifest, format) {
  if (format === "v3") return safeTargets(manifest.plannedFiles, { allowDiary: true });
  if (format === "v2") return safeTargets(manifest.entries);
  return null;
}
function isUnfinished(format, status, reviewedAt) {
  if (format === "v2") return status === "planned" || status === "committing";
  if (reviewedAt) return false;
  return ["started", "backed_up", "staged", "ready_to_commit", "incomplete"].includes(status);
}
function recovery(format, status, locked, reviewedAt) {
  if (format === "v2") {
    if (status === "planned") return locked ? "abort" : "manual-inspection";
    if (status === "committing") return "rollback";
    if (status === "committed") return "rollback-available";
    return "none";
  }
  if (reviewedAt) return "none";
  if (status === "incomplete") return "manual-reconciliation";
  if (["started", "backed_up", "staged", "ready_to_commit"].includes(status)) return "manual-inspection";
  return "none";
}
function recoveryCommand(format, status, locked, runId) {
  if (format !== "v2") return null;
  if (status === "planned" && locked) {
    return `memory-transaction.mjs abort <WORKSPACE_ROOT> ${runId} --confirm ${runId}`;
  }
  if (status === "committing" || status === "committed") {
    return `memory-transaction.mjs rollback <WORKSPACE_ROOT> ${runId} --confirm ${runId}`;
  }
  return null;
}

try {
  const [rootArg] = process.argv.slice(2);
  const root = resolveWorkspaceRoot(rootArg);
  const base = resolveInside(root, ".backup/memory-dreams", { allowMissing: true, label: "backup root" });
  const baseExists = fs.existsSync(base);
  if (baseExists) {
    const baseStat = fs.lstatSync(base);
    if (baseStat.isSymbolicLink() || !baseStat.isDirectory()) fail("backup root must be a real directory");
    assertNoSymlinkComponents(root, base, false);
  }

  const v2Lock = path.join(base, ".curation-lock");
  const v3Lock = resolveInside(root, LOCK_REL, { allowMissing: true, label: "V3 transaction lock" });
  const presentLocks = [
    fs.existsSync(v2Lock) ? { format: "v2", path: v2Lock } : null,
    fs.existsSync(v3Lock) ? { format: "v3", path: v3Lock } : null,
  ].filter(Boolean);
  if (presentLocks.length > 1) fail("multiple transaction locks are present");
  let activeLock = null;
  if (presentLocks.length === 1) {
    const currentLock = presentLocks[0];
    const lockStat = fs.lstatSync(currentLock.path);
    let owner;
    if (lockStat.isSymbolicLink()) fail("transaction lock must not be a symlink");
    if (currentLock.format === "v3" && lockStat.isFile()) {
      assertNoSymlinkComponents(root, currentLock.path, false);
      owner = readJson(root, currentLock.path, "V3 lock");
    } else if (currentLock.format === "v2" && lockStat.isDirectory()) {
      assertNoSymlinkComponents(root, currentLock.path, false);
      owner = readJson(root, path.join(currentLock.path, "owner.json"), "V2 lock owner");
    } else {
      fail(`${currentLock.format.toUpperCase()} transaction lock has the wrong type`);
    }
    if (!safeRunId(owner?.runId)) fail("unsafe lock owner run id");
    activeLock = {
      format: currentLock.format,
      runId: owner.runId,
      acquiredAt: typeof owner.startedAt === "string"
        ? owner.startedAt
        : typeof owner.acquiredAt === "string" ? owner.acquiredAt : null,
      recovery: owner.recovery === true,
    };
  }

  const transactions = [];
  const legacySnapshots = [];
  const backupEntries = baseExists ? fs.readdirSync(base, { withFileTypes: true }) : [];
  for (const entry of backupEntries) {
    if (entry.name === ".curation-lock") continue;
    if (!safeRunId(entry.name)) fail("unsafe transaction directory name");
    if (entry.isSymbolicLink() || !entry.isDirectory()) fail(`unsafe transaction entry: ${entry.name}`);
    const snapshot = resolveInside(root, `.backup/memory-dreams/${entry.name}`, { allowMissing: false, label: "transaction snapshot" });
    const manifestPath = path.join(snapshot, "manifest.json");
    if (!fs.existsSync(manifestPath)) {
      legacySnapshots.push(entry.name);
      continue;
    }
    const manifest = readJson(root, manifestPath, `manifest ${entry.name}`);
    const format = manifestFormat(manifest);
    if (!format || manifest.runId !== entry.name || manifestWorkspace(manifest, format) !== root) {
      fail(`manifest identity mismatch: ${entry.name}`);
    }
    const targets = manifestTargets(manifest, format);
    if (!targets || !targets.includes("MEMORY.md")) fail(`unsafe manifest targets: ${entry.name}`);
    const status = typeof manifest.status === "string" ? manifest.status : "unknown";
    const locked = activeLock?.runId === entry.name;
    if (locked && activeLock.format !== format) fail(`lock/manifest format mismatch: ${entry.name}`);
    const reviewedAt = typeof manifest.reviewedAt === "string" ? manifest.reviewedAt : null;
    const unfinished = isUnfinished(format, status, reviewedAt);
    const action = recovery(format, status, locked, reviewedAt);
    transactions.push({
      runId: entry.name,
      format,
      status,
      createdAt: typeof manifest.startedAt === "string"
        ? manifest.startedAt
        : typeof manifest.createdAt === "string" ? manifest.createdAt : null,
      reviewedAt,
      locked,
      unfinished,
      targets,
      recovery: action,
      command: recoveryCommand(format, status, locked, entry.name),
    });
  }
  transactions.sort((a, b) => a.runId.localeCompare(b.runId));
  const lockedTransaction = activeLock
    ? transactions.find((item) => item.runId === activeLock.runId)
    : null;
  if (activeLock && !lockedTransaction) fail("active lock has no matching transaction manifest");
  const unfinished = transactions.filter(item => item.unfinished);
  console.log(JSON.stringify({ ok: true, workspace: root, activeLock, unfinished, transactions, legacySnapshots }, null, 2));
} catch (error) {
  fail(error?.message || String(error));
}
