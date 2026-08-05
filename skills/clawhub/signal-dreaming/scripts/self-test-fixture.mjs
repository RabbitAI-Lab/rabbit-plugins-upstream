#!/usr/bin/env node
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import crypto from "node:crypto";

function die(message) {
  console.error(message);
  process.exit(2);
}
function realTemp() {
  return fs.realpathSync.native(os.tmpdir());
}
function requireBase(raw) {
  if (!raw) die("base required");
  const abs = path.resolve(raw);
  const rel = path.relative(realTemp(), abs);
  if (rel.startsWith("..") || path.isAbsolute(rel) || !path.basename(abs).startsWith("signal-dreaming-self-test-")) die("unsafe self-test base");
  const stat = fs.lstatSync(abs);
  if (stat.isSymbolicLink() || !stat.isDirectory() || fs.realpathSync.native(abs) !== abs) die("self-test base must be canonical");
  return abs;
}
function requireRoot(raw) {
  const abs = path.resolve(raw);
  let cursor = abs;
  while (cursor !== path.dirname(cursor) && !path.basename(cursor).startsWith("signal-dreaming-self-test-")) cursor = path.dirname(cursor);
  const base = requireBase(cursor);
  const rel = path.relative(base, abs);
  if (rel.startsWith("..") || path.isAbsolute(rel)) die("root escapes self-test base");
  return abs;
}
function safeRel(raw) {
  if (typeof raw !== "string" || !raw || raw.includes("\0")) die("unsafe relative path");
  const normalized = raw.replaceAll("\\", "/");
  if (path.posix.isAbsolute(normalized) || normalized.split("/").includes("..")) die("unsafe relative path");
  return path.posix.normalize(normalized);
}
function file(root, rel) {
  return path.join(requireRoot(root), ...safeRel(rel).split("/"));
}
function write(target, text) {
  fs.mkdirSync(path.dirname(target), { recursive: true, mode: 0o700 });
  fs.writeFileSync(target, text, "utf8");
}
function hash(target) {
  return crypto.createHash("sha256").update(fs.readFileSync(target)).digest("hex");
}
function markdown(mode) {
  if (mode === "memory-edited") return "# Memory\n\n- curated: true\n";
  if (mode === "topic-edited") return "# Topic\n\n- durable detail\n";
  if (mode === "secret") return "# Memory\n\n- token: " + "sk" + "-" + "A".repeat(24) + "\n";
  if (mode === "raw") return "# Memory\n\n" + "assistant" + ": copied transcript\n";
  if (mode === "large") return "# Memory\n\n" + "x".repeat(10241) + "\n";
  if (mode === "concurrent") return "# Memory\n\n- concurrent live edit\n";
  die(`unknown content mode: ${mode}`);
}
function readStdinJson() {
  try { return JSON.parse(fs.readFileSync(0, "utf8")); } catch { die("JSON required on stdin"); }
}
function nested(value, dotted) {
  return dotted.split(".").reduce((current, key) => current?.[key], value);
}
function expected(raw) {
  try { return JSON.parse(raw); } catch { return raw; }
}

const [command, ...args] = process.argv.slice(2);

if (command === "init") {
  const base = fs.mkdtempSync(path.join(realTemp(), "signal-dreaming-self-test-"));
  console.log(fs.realpathSync.native(base));
} else if (command === "workspace") {
  const base = requireBase(args[0]);
  if (!/^[A-Za-z0-9._-]+$/.test(args[1] ?? "")) die("unsafe workspace label");
  const root = path.join(base, args[1]);
  fs.mkdirSync(path.join(root, "memory"), { recursive: true, mode: 0o700 });
  write(path.join(root, "MEMORY.md"), "# Memory\n\n- baseline\n");
  write(path.join(root, "memory", "topic.md"), "# Topic\n\n- baseline\n");
  console.log(fs.realpathSync.native(root));
} else if (command === "write-live") {
  write(file(args[0], args[1]), markdown(args[2]));
} else if (command === "write-stage") {
  const target = file(args[0], `.backup/memory-dreams/${args[1]}/staging/${safeRel(args[2])}`);
  write(target, markdown(args[3]));
} else if (command === "sha") {
  console.log(hash(file(args[0], args[1])));
} else if (command === "assert-sha") {
  if (hash(file(args[0], args[1])) !== args[2]) die(`sha mismatch: ${args[1]}`);
} else if (command === "assert-exists") {
  if (!fs.existsSync(file(args[0], args[1]))) die(`expected path missing: ${args[1]}`);
} else if (command === "assert-missing") {
  if (fs.existsSync(file(args[0], args[1]))) die(`expected path absent: ${args[1]}`);
} else if (command === "assert-status") {
  const manifest = JSON.parse(fs.readFileSync(file(args[0], `.backup/memory-dreams/${args[1]}/manifest.json`), "utf8"));
  if (manifest.status !== args[2]) die(`expected status ${args[2]}, got ${manifest.status}`);
} else if (command === "assert-json") {
  const value = readStdinJson();
  const actual = nested(value, args[0]);
  const wanted = expected(args[1]);
  if (JSON.stringify(actual) !== JSON.stringify(wanted)) die(`JSON mismatch at ${args[0]}`);
} else if (command === "assert-json-includes") {
  const value = readStdinJson();
  const actual = nested(value, args[0]);
  if (!Array.isArray(actual) || !actual.includes(args[1])) die(`JSON array missing ${args[1]}`);
} else if (command === "simulate-crash") {
  const root = requireRoot(args[0]);
  const runId = args[1];
  const manifestPath = file(root, `.backup/memory-dreams/${runId}/manifest.json`);
  const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
  if (manifest.status !== "planned" || !manifest.entries.every(entry => typeof entry.stagedSha256 === "string")) die("verify transaction before crash simulation");
  manifest.status = "committing";
  manifest.commitStartedAt = new Date().toISOString();
  const first = manifest.entries[0];
  fs.copyFileSync(file(root, `.backup/memory-dreams/${runId}/staging/${first.path}`), file(root, first.path));
  write(manifestPath, JSON.stringify(manifest, null, 2) + "\n");
} else if (command === "symlink") {
  const root = requireRoot(args[0]);
  const link = file(root, args[1]);
  fs.mkdirSync(path.dirname(link), { recursive: true, mode: 0o700 });
  fs.symlinkSync(args[2], link);
} else if (command === "legacy-snapshot") {
  const root = requireRoot(args[0]);
  write(file(root, `.backup/memory-dreams/${args[1]}/MEMORY.md.bak`), "# Legacy backup\n");
} else if (command === "preflight") {
  const root = requireRoot(args[0]);
  const mode = args[1];
  const envelope = {
    openclawVersion: "2026.7.1",
    capabilities: { promoteExplain: true, remHarness: true },
    status: [{ status: { workspaceDir: root, backend: "builtin" }, dreamingAudit: { issues: [] } }],
    promote: { workspaceDir: root, audit: { issues: [] }, candidates: [] },
    cron: { jobs: [
      { id: "native", name: "Native Dreaming", enabled: true, schedule: { kind: "cron" }, payload: { message: "__openclaw_memory_core_short_term_promotion_dream__" } },
      { id: "v2", name: "signal-dreaming-v2", enabled: true, schedule: { kind: "cron" }, payload: { message: "Run gate-driven curation with curation-gate.mjs" } },
    ] },
  };
  if (mode === "bad-schema") delete envelope.promote.candidates;
  console.log(JSON.stringify(envelope));
} else if (command === "cleanup") {
  const base = requireBase(args[0]);
  fs.rmSync(base, { recursive: true, force: true });
} else {
  die("unknown fixture command");
}
