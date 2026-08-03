#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { assertNoSymlinkComponents, ensureSafeDirectory, normalizeRelativePath, resolveInside, resolveWorkspaceRoot, safeRegularOrMissing } from "./path-guard.mjs";

function die(message, code = 2) {
  const error = new Error(message);
  error.exitCode = code;
  throw error;
}
let activeRoot = null;
function rootOf(arg) {
  try { activeRoot = resolveWorkspaceRoot(arg); return activeRoot; }
  catch (error) { die(error.message); }
}
function safeRunId(id) {
  if (!id || !/^[A-Za-z0-9._-]+$/.test(id) || id === "." || id === "..") die("unsafe run id");
  return id;
}
function normalizeRel(raw) {
  try { return normalizeRelativePath(raw, "target"); }
  catch (error) { die(error.message); }
}
function allowedTarget(rel) {
  if (rel === "MEMORY.md") return true;
  if (!rel.startsWith("memory/") || !rel.endsWith(".md")) return false;
  const tail = rel.slice("memory/".length);
  if (!tail || tail.includes("/")) return false;
  if (/^\d{4}-\d{2}-\d{2}.*\.md$/.test(tail)) return false;
  if (tail === "dream-log.md") return false;
  return true;
}
function livePath(root, rel) {
  try { return resolveInside(root, rel, { allowMissing: true, label: "target" }); }
  catch (error) { die(error.message); }
}
function regularOrMissing(file) {
  try { return safeRegularOrMissing(activeRoot, file); }
  catch (error) { die(error.message); }
}
function sha(file) {
  return crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");
}
function mkdirParent(file) {
  try { ensureSafeDirectory(activeRoot, path.dirname(file)); }
  catch (error) { die(error.message); }
}
function atomicCopy(src, dest, token) {
  if (regularOrMissing(src) !== "file") die(`copy source missing: ${src}`);
  mkdirParent(dest);
  try { assertNoSymlinkComponents(activeRoot, dest, true); }
  catch (error) { die(error.message); }
  const tmp = `${dest}.tmp-${token}-${process.pid}`;
  fs.copyFileSync(src, tmp, fs.constants.COPYFILE_EXCL);
  fs.renameSync(tmp, dest);
}
function writeJson(file, value) {
  mkdirParent(file);
  try { assertNoSymlinkComponents(activeRoot, file, true); }
  catch (error) { die(error.message); }
  const tmp = `${file}.tmp-${process.pid}`;
  fs.writeFileSync(tmp, JSON.stringify(value, null, 2) + "\n", { mode: 0o600, flag: "wx" });
  fs.renameSync(tmp, file);
}
function readJson(file) {
  if (regularOrMissing(file) !== "file") die(`missing JSON file: ${file}`);
  try { return JSON.parse(fs.readFileSync(file, "utf8")); }
  catch { die(`cannot read manifest: ${file}`); }
}
function pathsFor(root, runId) {
  try {
    const base = resolveInside(root, ".backup/memory-dreams", { allowMissing: true, label: "backup root" });
    return {
      base,
      lock: resolveInside(root, ".backup/memory-dreams/.curation-lock", { allowMissing: true, label: "transaction lock" }),
      snapshot: resolveInside(root, `.backup/memory-dreams/${runId}`, { allowMissing: true, label: "snapshot" }),
      manifest: resolveInside(root, `.backup/memory-dreams/${runId}/manifest.json`, { allowMissing: true, label: "manifest" }),
    };
  } catch (error) { die(error.message); }
}
function lockOwner(lock) {
  try { assertNoSymlinkComponents(activeRoot, lock, true); }
  catch (error) { die(error.message); }
  const ownerFile = path.join(lock, "owner.json");
  if (!fs.existsSync(ownerFile)) return null;
  if (regularOrMissing(ownerFile) !== "file") return null;
  try { return JSON.parse(fs.readFileSync(ownerFile, "utf8")); }
  catch { return null; }
}
function requireOwnedLock(p, runId) {
  const owner = lockOwner(p.lock);
  if (!owner || owner.runId !== runId) die("transaction lock is absent or owned by another run");
}
function acquireRecoveryLock(p, runId) {
  if (fs.existsSync(p.lock)) {
    requireOwnedLock(p, runId);
    return false;
  }
  fs.mkdirSync(p.lock);
  writeJson(path.join(p.lock, "owner.json"), { runId, acquiredAt: new Date().toISOString(), recovery: true });
  return true;
}
function releaseLock(p, runId) {
  const owner = lockOwner(p.lock);
  if (owner?.runId === runId) {
    try { assertNoSymlinkComponents(activeRoot, p.lock, false); }
    catch (error) { die(error.message); }
    fs.rmSync(p.lock, { recursive: true, force: true });
  }
}
function loadManifest(p, root, runId) {
  const m = readJson(p.manifest);
  if (m.runId !== runId || m.workspace !== root || !Array.isArray(m.entries)) die("manifest identity mismatch");
  for (const e of m.entries) {
    e.path = normalizeRel(e.path);
    if (!allowedTarget(e.path)) die(`forbidden manifest target: ${e.path}`);
  }
  return m;
}
const secretRe = /(github_pat_[A-Za-z0-9_]{20,}|gh[opsu]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|[0-9]{8,12}:AA[A-Za-z0-9_-]{30,}|mfa\.[A-Za-z0-9_-]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----|x-access-token:[A-Za-z0-9_-]{20,}@)/;
const rawMarkerRe = /(<<<EXTERNAL_UNTRUSTED_CONTENT|<<<END_EXTERNAL_UNTRUSTED_CONTENT|^assistant:|^user:|^system:)/m;

function verify(root, p, m) {
  const warnings = [];
  for (const e of m.entries) {
    const live = livePath(root, e.path);
    const state = regularOrMissing(live);
    if (e.state === "existing") {
      if (state !== "file" || sha(live) !== e.beforeSha256) die(`concurrent live edit: ${e.path}`);
    } else if (state !== "missing") {
      die(`new target appeared concurrently: ${e.path}`);
    }
    const staged = path.join(p.snapshot, "staging", e.path);
    if (regularOrMissing(staged) !== "file") die(`missing staged file: ${e.path}`);
    const text = fs.readFileSync(staged, "utf8");
    if (!text.trim() || !/^#/m.test(text)) die(`empty or headerless staged Markdown: ${e.path}`);
    if (secretRe.test(text)) die(`suspected credential pattern in staged file: ${e.path}`);
    if (rawMarkerRe.test(text)) die(`raw transcript/untrusted marker in staged file: ${e.path}`);
    if (e.path === "MEMORY.md") {
      const bytes = fs.statSync(staged).size;
      if (bytes > 10240) die("staged MEMORY.md exceeds 10 KiB");
      if (bytes > 8192) warnings.push("MEMORY.md exceeds 8 KiB editorial target");
    }
    e.stagedSha256 = sha(staged);
  }
  return warnings;
}

try {
const [command, rootArg, runArg, ...rest] = process.argv.slice(2);
const root = rootOf(rootArg);
const runId = safeRunId(runArg);
const p = pathsFor(root, runId);

if (command === "begin") {
  const targets = [...new Set(rest.map(normalizeRel))];
  if (!targets.includes("MEMORY.md")) die("MEMORY.md must be included");
  for (const rel of targets) if (!allowedTarget(rel)) die(`forbidden target: ${rel}`);
  for (const rel of targets) regularOrMissing(livePath(root, rel));
  try { ensureSafeDirectory(root, p.base); } catch (error) { die(error.message); }
  if (fs.existsSync(p.snapshot)) die("run id already exists");
  try { fs.mkdirSync(p.lock); } catch { die("another curation transaction is active"); }
  try {
    writeJson(path.join(p.lock, "owner.json"), { runId, acquiredAt: new Date().toISOString() });
    try {
      ensureSafeDirectory(root, path.join(p.snapshot, "backup"));
      ensureSafeDirectory(root, path.join(p.snapshot, "staging"));
    } catch (error) { die(error.message); }
    const entries = targets.map(rel => {
      const live = livePath(root, rel);
      const state = regularOrMissing(live);
      if (state === "file") {
        const beforeSha256 = sha(live);
        atomicCopy(live, path.join(p.snapshot, "backup", rel + ".bak"), runId);
        atomicCopy(live, path.join(p.snapshot, "staging", rel), runId);
        return { path: rel, state: "existing", beforeSha256 };
      }
      mkdirParent(path.join(p.snapshot, "staging", rel));
      return { path: rel, state: "new", beforeSha256: null };
    });
    const manifest = {
      version: 2, runId, workspace: root, status: "planned",
      createdAt: new Date().toISOString(), entries,
    };
    writeJson(p.manifest, manifest);
    console.log(JSON.stringify({ ok: true, snapshot: p.snapshot, targets }, null, 2));
  } catch (error) {
    releaseLock(p, runId);
    throw error;
  }
} else if (command === "verify") {
  requireOwnedLock(p, runId);
  const m = loadManifest(p, root, runId);
  if (m.status !== "planned") die(`cannot verify status ${m.status}`);
  const warnings = verify(root, p, m);
  writeJson(p.manifest, m);
  console.log(JSON.stringify({ ok: true, warnings, entries: m.entries.map(e => ({ path: e.path, stagedSha256: e.stagedSha256 })) }, null, 2));
} else if (command === "commit") {
  requireOwnedLock(p, runId);
  const m = loadManifest(p, root, runId);
  if (m.status !== "planned") die(`cannot commit status ${m.status}`);
  const warnings = verify(root, p, m);
  m.status = "committing";
  m.commitStartedAt = new Date().toISOString();
  writeJson(p.manifest, m);
  const prepared = [];
  const replaced = [];
  try {
    for (const e of m.entries) {
      const live = livePath(root, e.path);
      mkdirParent(live);
      const tmp = `${live}.tmp-${runId}-${process.pid}`;
      fs.copyFileSync(path.join(p.snapshot, "staging", e.path), tmp, fs.constants.COPYFILE_EXCL);
      prepared.push({ e, live, tmp });
    }
    for (const item of prepared) {
      const state = regularOrMissing(item.live);
      if (item.e.state === "existing") {
        if (state !== "file" || sha(item.live) !== item.e.beforeSha256) die(`concurrent live edit: ${item.e.path}`);
      } else if (state !== "missing") die(`new target appeared concurrently: ${item.e.path}`);
      fs.renameSync(item.tmp, item.live);
      replaced.push(item);
    }
  } catch (error) {
    const quarantine = path.join(p.snapshot, "quarantine", "failed-commit");
    for (const item of replaced.reverse()) {
      if (item.e.state === "existing") {
        atomicCopy(path.join(p.snapshot, "backup", item.e.path + ".bak"), item.live, runId + "-restore");
      } else if (fs.existsSync(item.live)) {
        const q = path.join(quarantine, item.e.path);
        mkdirParent(q);
        fs.renameSync(item.live, q);
      }
    }
    for (const item of prepared) if (fs.existsSync(item.tmp)) fs.rmSync(item.tmp, { force: true });
    m.status = "commit_failed_rolled_back";
    m.error = String(error?.message || error);
    writeJson(p.manifest, m);
    releaseLock(p, runId);
    die("commit failed; in-process rollback completed");
  }
  for (const e of m.entries) e.afterSha256 = sha(livePath(root, e.path));
  m.status = "committed";
  m.committedAt = new Date().toISOString();
  writeJson(p.manifest, m);
  releaseLock(p, runId);
  console.log(JSON.stringify({ ok: true, runId, warnings, rollback: `rollback ${runId} --confirm ${runId}` }, null, 2));
} else if (command === "abort") {
  if (rest[0] !== "--confirm" || rest[1] !== runId) die("exact --confirm RUN_ID required");
  requireOwnedLock(p, runId);
  const m = loadManifest(p, root, runId);
  if (m.status !== "planned") die(`cannot abort status ${m.status}`);
  verify(root, p, m);
  m.status = "aborted";
  m.abortedAt = new Date().toISOString();
  writeJson(p.manifest, m);
  releaseLock(p, runId);
  console.log(JSON.stringify({ ok: true, runId, status: "aborted" }));
} else if (command === "rollback") {
  if (rest[0] !== "--confirm" || rest[1] !== runId) die("exact --confirm RUN_ID required");
  const acquired = acquireRecoveryLock(p, runId);
  try {
    const m = loadManifest(p, root, runId);
    if (!["committed", "committing"].includes(m.status)) die(`cannot rollback status ${m.status}`);
    for (const e of m.entries) {
      const live = livePath(root, e.path);
      const state = regularOrMissing(live);
      if (m.status === "committed") {
        if (state !== "file" || sha(live) !== e.afterSha256) die(`later live edit blocks rollback: ${e.path}`);
      } else if (state === "file") {
        const current = sha(live);
        if (current !== e.beforeSha256 && current !== e.stagedSha256) die(`unknown live state blocks recovery: ${e.path}`);
      } else if (e.state === "existing") {
        die(`missing existing file blocks recovery: ${e.path}`);
      }
    }
    const quarantine = path.join(p.snapshot, "quarantine", "pre-rollback");
    for (const e of m.entries) {
      const live = livePath(root, e.path);
      if (e.state === "existing") {
        if (fs.existsSync(live) && sha(live) !== e.beforeSha256) {
          const q = path.join(quarantine, e.path);
          mkdirParent(q);
          fs.copyFileSync(live, q);
        }
        atomicCopy(path.join(p.snapshot, "backup", e.path + ".bak"), live, runId + "-rollback");
      } else if (fs.existsSync(live)) {
        const q = path.join(quarantine, e.path);
        mkdirParent(q);
        fs.renameSync(live, q);
      }
    }
    m.status = "rolled_back";
    m.rolledBackAt = new Date().toISOString();
    writeJson(p.manifest, m);
    console.log(JSON.stringify({ ok: true, runId, status: "rolled_back", quarantine }, null, 2));
  } finally {
    if (acquired || lockOwner(p.lock)?.runId === runId) releaseLock(p, runId);
  }
} else if (command === "status") {
  const manifest = fs.existsSync(p.manifest) ? readJson(p.manifest) : null;
  console.log(JSON.stringify({ runId, lock: lockOwner(p.lock), manifest }, null, 2));
} else {
  die("command must be begin, verify, commit, abort, rollback, or status");
}
} catch (error) {
  console.error("ERROR:", error?.message || String(error));
  process.exit(error?.exitCode || 2);
}
