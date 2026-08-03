#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { assertNoSymlinkComponents, ensureSafeDirectory, resolveInside, resolveWorkspaceRoot, safeRegularOrMissing } from "./path-guard.mjs";

function fail(message) {
  process.stdout.write(JSON.stringify({ fire: false, error: message }) + "\n");
  process.exit(2);
}
function shaFile(file) {
  return crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");
}
function workspace(arg) {
  try { return resolveWorkspaceRoot(arg); }
  catch (error) { fail(error.message); }
}
function topicSnapshot(root) {
  const memoryDir = resolveInside(root, "memory", { allowMissing: true, label: "memory directory" });
  const rows = [];
  if (!fs.existsSync(memoryDir)) return { count: 0, sha256: crypto.createHash("sha256").digest("hex") };
  const memoryStat = fs.lstatSync(memoryDir);
  if (memoryStat.isSymbolicLink() || !memoryStat.isDirectory()) fail("memory directory must be a real directory");
  for (const ent of fs.readdirSync(memoryDir, { withFileTypes: true })) {
    if (!ent.name.endsWith(".md")) continue;
    if (ent.isSymbolicLink()) fail(`symlinked topic rejected: memory/${ent.name}`);
    if (!ent.isFile()) continue;
    if (/^\d{4}-\d{2}-\d{2}.*\.md$/.test(ent.name)) continue;
    if (ent.name === "dream-log.md") continue;
    const rel = `memory/${ent.name}`;
    const topic = resolveInside(root, rel, { allowMissing: false, label: "topic" });
    if (safeRegularOrMissing(root, topic) !== "file") fail(`non-regular topic rejected: ${rel}`);
    rows.push(`${rel}\t${shaFile(topic)}`);
  }
  rows.sort();
  return {
    count: rows.length,
    sha256: crypto.createHash("sha256").update(rows.join("\n")).digest("hex"),
  };
}
function snapshot(root) {
  const memory = resolveInside(root, "MEMORY.md", { allowMissing: false, label: "MEMORY.md" });
  if (safeRegularOrMissing(root, memory) !== "file") fail("MEMORY.md missing or non-regular");
  const topics = topicSnapshot(root);
  return {
    memorySha256: shaFile(memory),
    memoryBytes: fs.statSync(memory).size,
    topicCount: topics.count,
    topicSha256: topics.sha256,
  };
}
function writeJson(root, file, value) {
  try {
    ensureSafeDirectory(root, path.dirname(file));
    assertNoSymlinkComponents(root, file, true);
  } catch (error) { fail(error.message); }
  const tmp = `${file}.tmp-${process.pid}`;
  fs.writeFileSync(tmp, JSON.stringify(value, null, 2) + "\n", { mode: 0o600, flag: "wx" });
  fs.renameSync(tmp, file);
}

try {
const [command, rootArg, runId] = process.argv.slice(2);
const root = workspace(rootArg);
const stateFile = resolveInside(root, "logs/signal-dreaming/state.json", { allowMissing: true, label: "gate state" });
const current = snapshot(root);

if (command === "check") {
  let previous = null;
  if (fs.existsSync(stateFile)) {
    try {
      if (safeRegularOrMissing(root, stateFile) !== "file") fail("gate state is non-regular");
      previous = JSON.parse(fs.readFileSync(stateFile, "utf8"));
    } catch (error) {
      if (error?.name === "PathSafetyError") fail(error.message);
    }
  }
  const reasons = [];
  if (!previous) reasons.push("no_successful_v2_review");
  if (current.memoryBytes > 10240) reasons.push("memory_over_10k");
  if (previous && previous.memorySha256 !== current.memorySha256) reasons.push("memory_changed");
  if (previous && previous.topicSha256 !== current.topicSha256) reasons.push("topics_changed");
  if (previous?.markedAt) {
    const age = Date.now() - Date.parse(previous.markedAt);
    if (Number.isFinite(age) && age > 30 * 86400000) reasons.push("review_older_than_30d");
  }
  process.stdout.write(JSON.stringify({ fire: reasons.length > 0, reasons, ...current }) + "\n");
} else if (command === "mark") {
  if (!runId || !/^[A-Za-z0-9._-]+$/.test(runId)) fail("safe run id required");
  const value = { version: 2, runId, markedAt: new Date().toISOString(), ...current };
  writeJson(root, stateFile, value);
  process.stdout.write(JSON.stringify({ ok: true, stateFile, ...value }) + "\n");
} else {
  fail("command must be check or mark");
}
} catch (error) {
  fail(error?.message || String(error));
}
