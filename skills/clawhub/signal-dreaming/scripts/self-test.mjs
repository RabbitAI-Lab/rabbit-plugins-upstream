#!/usr/bin/env node
import assert from "node:assert/strict";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import {
  LOCK_REL,
  STATE_REL,
  parseDreamLog,
  safePath,
  sha256File,
  writeJsonAtomic,
} from "./common.mjs";
import {
  MAX_INPUT_BYTES,
  MAX_LOGS_PER_RUN,
  buildDeltaPlan,
  inspectState,
  nextState,
  quarantineState,
  renderDiary,
} from "./delta-state.mjs";
import { auditWorkspace } from "./dream-audit.mjs";
import { preflight } from "./preflight.mjs";
import {
  acknowledgeIncomplete,
  beginRun,
  createRunId,
  finalizeRun,
  validateWritePath,
  verifyBeforeWrite,
} from "./run-guard.mjs";

const results = [];
const roots = [];

async function test(name, fn) {
  try {
    await fn();
    results.push({ name, ok: true });
  } catch (error) {
    results.push({ name, ok: false, code: error.code, message: error.message });
  }
}

async function expectCode(code, fn) {
  await assert.rejects(fn, (error) => error.code === code);
}

async function write(file, content) {
  await fs.mkdir(path.dirname(file), { recursive: true });
  await fs.writeFile(file, content);
}

function dreamLog(start = 1, count = 1) {
  return Array.from({ length: count }, (_, index) => (
    `## 🌙 Dream #${start + index} · 2026-07-${String(index + 1).padStart(2, "0")} 10:00\n\nDone.\n`
  )).join("\n");
}

async function workspace(label = "fixture") {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), `signal-dreaming-v3-${label}-`));
  roots.push(root);
  await write(path.join(root, "MEMORY.md"), "# Memory\n");
  await write(path.join(root, "memory/dream-log.md"), dreamLog(103, 1));
  return root;
}

function evidence(overrides = {}) {
  return {
    openclawVersion: "2026.7.1-2",
    nodeVersion: "22.23.1",
    nativeDreamingEnabled: false,
    cronJobs: [{
      id: "writer-1",
      name: "daily-dream",
      enabled: true,
      payload: { kind: "agentTurn", message: "Run a dream consolidation with signal-dreaming." },
    }],
    ...overrides,
  };
}

async function addLog(root, name = "2026-07-23.md", content = "new memory\n") {
  await write(path.join(root, "memory", name), content);
}

async function planFor(root) {
  return buildDeltaPlan(root, { now: "2026-07-23T10:00:00Z" });
}

await test("preflight accepts one writer and native Dreaming off", async () => {
  const root = await workspace("preflight-ok");
  const result = await preflight(root, evidence());
  assert.equal(result.ok, true);
  assert.equal(result.writeAllowed, true);
});

await test("native Dreaming enabled fails write mode", async () => {
  const root = await workspace("native-on");
  const result = await preflight(root, evidence({ nativeDreamingEnabled: true }));
  assert(result.errors.some((item) => item.code === "NATIVE_DREAMING_ENABLED"));
});

await test("native Dreaming enabled permits read-only diagnosis only", async () => {
  const root = await workspace("native-read");
  const result = await preflight(root, evidence({ nativeDreamingEnabled: true }), { readOnly: true });
  assert.equal(result.ok, true);
  assert.equal(result.writeAllowed, false);
});

await test("two enabled signal writers fail closed", async () => {
  const root = await workspace("two-writers");
  const second = { id: "writer-2", name: "signal-dreaming-v2", enabled: true, payload: { message: "signal-dreaming" } };
  const result = await preflight(root, evidence({ cronJobs: [...evidence().cronJobs, second] }));
  const error = result.errors.find((item) => item.code === "MULTIPLE_WRITERS");
  assert(error);
  assert.match(error.message, /disable all but one/);
});

await test("disabled v2 writer is ignored", async () => {
  const root = await workspace("disabled-writer");
  const disabled = { id: "writer-2", name: "signal-dreaming-v2", enabled: false, payload: { message: "signal-dreaming" } };
  const result = await preflight(root, evidence({ cronJobs: [...evidence().cronJobs, disabled] }));
  assert.equal(result.ok, true);
  assert.equal(result.writers.length, 1);
});

await test("manual run with zero writers warns but remains write eligible", async () => {
  const root = await workspace("manual-zero-writers");
  const result = await preflight(root, evidence({ cronJobs: [] }));
  assert.equal(result.ok, true);
  assert.equal(result.writeAllowed, true);
  assert(result.warnings.some((item) => item.code === "NO_SCHEDULED_WRITER"));
});

await test("scheduled run with zero writers fails closed", async () => {
  const root = await workspace("scheduled-zero-writers");
  const result = await preflight(root, evidence({ cronJobs: [] }), { scheduled: true });
  assert.equal(result.ok, false);
  assert.equal(result.writeAllowed, false);
  assert(result.errors.some((item) => item.code === "NO_SCHEDULED_WRITER"));
});

await test("cron schema drift fails closed", async () => {
  const root = await workspace("schema-drift");
  const result = await preflight(root, evidence({ cronJobs: [{ id: "x", enabled: true }] }));
  assert(result.errors.some((item) => item.code === "CLI_SCHEMA"));
});

await test("older OpenClaw is rejected", async () => {
  const root = await workspace("old-openclaw");
  const result = await preflight(root, evidence({ openclawVersion: "2026.7.1-1" }));
  assert(result.errors.some((item) => item.code === "OPENCLAW_TOO_OLD"));
});

await test("workspace symlink escape fails path preflight", async () => {
  const root = await workspace("symlink");
  const external = await fs.mkdtemp(path.join(os.tmpdir(), "signal-dreaming-external-"));
  roots.push(external);
  await write(path.join(external, "outside.md"), "# outside\n");
  await fs.unlink(path.join(root, "MEMORY.md"));
  await fs.symlink(path.join(external, "outside.md"), path.join(root, "MEMORY.md"));
  const result = await preflight(root, evidence());
  assert(result.errors.some((item) => ["SYMLINK_OUTPUT", "SYMLINK_ESCAPE"].includes(item.code)));
});

await test("missing state bootstraps only the last seven days", async () => {
  const root = await workspace("bootstrap");
  await addLog(root, "2026-06-01.md");
  await addLog(root, "2026-07-17.md");
  await addLog(root, "2026-07-18.md");
  const plan = await planFor(root);
  assert.deepEqual(plan.selectedLogs.map((item) => item.path), ["memory/2026-07-17.md", "memory/2026-07-18.md"]);
});

await test("older backlog stays manual after bounded bootstrap", async () => {
  const root = await workspace("manual-backlog");
  await addLog(root, "2026-06-01.md");
  await addLog(root, "2026-07-23.md");
  const first = await planFor(root);
  await writeJsonAtomic(path.join(root, STATE_REL), nextState(first, "2026-07-23T10:00:00Z", 104));
  const normal = await planFor(root);
  assert.equal(normal.noop, true);
  const manual = await buildDeltaPlan(root, { now: "2026-07-23T10:00:00Z", fullHistory: true });
  assert.deepEqual(manual.selectedLogs.map((item) => item.path), ["memory/2026-06-01.md"]);
});

await test("394-log full-history bootstrap remains bounded", async () => {
  const root = await workspace("backlog");
  const start = new Date("2025-01-01T00:00:00Z");
  for (let index = 0; index < 394; index += 1) {
    const day = new Date(start);
    day.setUTCDate(day.getUTCDate() + index);
    await addLog(root, `${day.toISOString().slice(0, 10)}.md`, `${index}\n`);
  }
  const plan = await buildDeltaPlan(root, { now: "2026-07-23T10:00:00Z", fullHistory: true });
  assert.equal(plan.selectedLogs.length, MAX_LOGS_PER_RUN);
  assert.equal(plan.batchCapped, true);
  assert(plan.selectedBytes <= MAX_INPUT_BYTES);
});

await test("same-day append is detected by content hash", async () => {
  const root = await workspace("same-day");
  await addLog(root);
  const first = await planFor(root);
  const state = {
    schemaVersion: 3,
    lastSuccessfulRun: "2026-07-23T10:00:00Z",
    lastDreamNumber: 103,
    bootstrapCutoff: "2026-07-17",
    dailyLogs: Object.fromEntries(first.selectedLogs.map((item) => [item.path, item])),
  };
  await writeJsonAtomic(path.join(root, STATE_REL), state);
  await fs.appendFile(path.join(root, "memory/2026-07-23.md"), "later append\n");
  const second = await planFor(root);
  assert.deepEqual(second.selectedLogs.map((item) => item.path), ["memory/2026-07-23.md"]);
});

await test("same-day suffix log is discovered", async () => {
  const root = await workspace("suffix");
  await addLog(root, "2026-07-23-topic.md");
  const plan = await planFor(root);
  assert(plan.selectedLogs.some((item) => item.path === "memory/2026-07-23-topic.md"));
});

await test("unchanged state produces a true read-only no-op", async () => {
  const root = await workspace("noop");
  await addLog(root);
  const first = await planFor(root);
  await writeJsonAtomic(path.join(root, STATE_REL), {
    schemaVersion: 3,
    lastSuccessfulRun: "2026-07-23T10:00:00Z",
    lastDreamNumber: 103,
    bootstrapCutoff: "2026-07-17",
    dailyLogs: Object.fromEntries(first.selectedLogs.map((item) => [item.path, item])),
  });
  const before = await fs.stat(path.join(root, "memory/dream-log.md"));
  const second = await planFor(root);
  const after = await fs.stat(path.join(root, "memory/dream-log.md"));
  assert.equal(second.noop, true);
  assert.equal(after.mtimeMs, before.mtimeMs);
});

await test("corrupt state fails closed", async () => {
  const root = await workspace("state-corrupt");
  const statePath = path.join(root, STATE_REL);
  await write(statePath, "{no");
  await expectCode("STATE_INVALID", () => planFor(root));
  const inspection = await inspectState(root);
  const hash = await sha256File(statePath);
  assert.equal(inspection.sha256, hash);
  assert.equal(inspection.bytes, 3);
  await expectCode("CONFIRMATION", () => quarantineState(root, "wrong"));
  const result = await quarantineState(root, hash, { now: "2026-07-23T10:00:00Z" });
  assert.equal(result.ok, true);
  assert.equal(await fs.stat(statePath).then(() => true, () => false), false);
  assert.equal(await sha256File(path.join(root, result.backup)), hash);
  const plan = await planFor(root);
  assert.equal(plan.mode, "bootstrap");
});

await test("unknown state schema fails closed", async () => {
  const root = await workspace("state-old");
  await writeJsonAtomic(path.join(root, STATE_REL), { schemaVersion: 2, dailyLogs: {} });
  await expectCode("STATE_SCHEMA_UNSUPPORTED", () => planFor(root));
});

await test("recall JSON absence is irrelevant", async () => {
  const root = await workspace("no-recall");
  await addLog(root);
  const plan = await planFor(root);
  assert.equal(plan.selectedLogs.length, 1);
});

await test("Dream 103 advances to 104 and trims to 30", async () => {
  const root = await workspace("diary-trim");
  await write(path.join(root, "memory/dream-log.md"), `# Dream Log\n\nKeep this preamble.\n\n${dreamLog(74, 30)}`);
  const rendered = await renderDiary(root, {
    number: 104,
    timestamp: "2026-07-23 10:00",
    trigger: "manual",
    durationMinutes: 3,
    newLogCount: 1,
    changes: ["Updated memory/topic.md"],
    note: "A bounded test.",
  });
  const parsed = parseDreamLog(rendered);
  assert.equal(parsed.entries.length, 30);
  assert.equal(parsed.entries[0].number, 75);
  assert.equal(parsed.max, 104);
  assert.match(rendered, /^# Dream Log\n\nKeep this preamble\./);
});

for (const [name, content, code] of [
  ["duplicate diary number", `${dreamLog(1, 1)}\n${dreamLog(1, 1)}`, "DIARY_DUPLICATE"],
  ["descending diary number", `${dreamLog(2, 1)}\n${dreamLog(1, 1)}`, "DIARY_DESCENDING"],
  ["malformed diary heading", "## 🌙 Dream #broken\n", "DIARY_MALFORMED"],
  ["noncanonical diary heading", "## Dream #103 — 2026-07-23 10:00\n", "DIARY_MALFORMED"],
  ["wrong-level diary heading", "### 🌙 Dream #103 · 2026-07-23 10:00\n", "DIARY_MALFORMED"],
]) {
  await test(`${name} is detected`, async () => {
    const root = await workspace("diary-invalid");
    await write(path.join(root, "memory/dream-log.md"), content);
    const audit = await auditWorkspace(root);
    assert(audit.errors.some((item) => item.code === code));
  });
}

for (const [bytes, expectedOk, expectedWarning] of [
  [8191, true, false],
  [8192, true, false],
  [8193, true, true],
  [10240, true, true],
  [10241, false, false],
]) {
  await test(`MEMORY.md size boundary ${bytes}`, async () => {
    const root = await workspace(`size-${bytes}`);
    await write(path.join(root, "MEMORY.md"), "x".repeat(bytes));
    const audit = await auditWorkspace(root);
    assert.equal(audit.ok, expectedOk);
    assert.equal(audit.warnings.some((item) => item.code === "MEMORY_SOFT_LIMIT"), expectedWarning);
  });
}

await test("secret audit reports only file and category", async () => {
  const root = await workspace("secret");
  const fake = `ghp_${"A".repeat(25)}`;
  await write(path.join(root, "MEMORY.md"), fake);
  const audit = await auditWorkspace(root);
  const serialized = JSON.stringify(audit);
  assert(audit.secretFindings.some((item) => item.categories.includes("github-token")));
  assert.equal(serialized.includes(fake), false);
});

await test("path traversal and absolute write targets are rejected", async () => {
  assert.throws(() => validateWritePath("memory/../MEMORY.md"), { code: "INVALID_WRITE_TARGET" });
  assert.throws(() => validateWritePath("/tmp/topic.md"), { code: "INVALID_WRITE_TARGET" });
  const root = await workspace("traversal");
  await expectCode("UNSAFE_PATH", () => safePath(root, "../outside"));
});

await test("daily logs cannot enter a write plan", async () => {
  assert.throws(() => validateWritePath("memory/2026-07-23.md"), { code: "INVALID_WRITE_TARGET" });
});

await test("backup failure leaves an incomplete manifest", async () => {
  const root = await workspace("backup-fail");
  await addLog(root);
  const plan = await planFor(root);
  const runId = createRunId();
  await expectCode("SIMULATED_BACKUP_FAILURE", () => beginRun(root, runId, plan, ["memory/dream-log.md"], {
    copyFile: async () => { throw Object.assign(new Error("simulated"), { code: "SIMULATED_BACKUP_FAILURE" }); },
  }));
  const manifest = JSON.parse(await fs.readFile(path.join(root, ".backup/memory-dreams", runId, "manifest.json"), "utf8"));
  assert.equal(manifest.status, "incomplete");
});

await test("live hash change after backup blocks the first write", async () => {
  const root = await workspace("live-change");
  await addLog(root);
  const plan = await planFor(root);
  const runId = createRunId();
  await beginRun(root, runId, plan, ["MEMORY.md", "memory/dream-log.md"]);
  await fs.appendFile(path.join(root, "MEMORY.md"), "racing edit\n");
  await expectCode("LIVE_HASH_CHANGED", () => verifyBeforeWrite(root, runId));
});

await test("daily input append after backup blocks the first write", async () => {
  const root = await workspace("daily-race");
  await addLog(root);
  const plan = await planFor(root);
  const runId = createRunId();
  await beginRun(root, runId, plan, ["memory/dream-log.md"]);
  await fs.appendFile(path.join(root, "memory/2026-07-23.md"), "racing daily append\n");
  await expectCode("DAILY_INPUT_CHANGED", () => verifyBeforeWrite(root, runId));
});

await test("symlink write target is rejected before live writes", async () => {
  const root = await workspace("write-symlink");
  await addLog(root);
  const external = await fs.mkdtemp(path.join(os.tmpdir(), "signal-dreaming-write-external-"));
  roots.push(external);
  await write(path.join(external, "topic.md"), "# outside\n");
  await fs.symlink(path.join(external, "topic.md"), path.join(root, "memory/topic.md"));
  const plan = await planFor(root);
  await assert.rejects(
    () => beginRun(root, createRunId(), plan, ["memory/topic.md", "memory/dream-log.md"]),
    (error) => ["SYMLINK_OUTPUT", "SYMLINK_ESCAPE"].includes(error.code),
  );
});

await test("a second concurrent run is rejected", async () => {
  const root = await workspace("concurrent");
  await addLog(root);
  const plan = await planFor(root);
  await beginRun(root, createRunId(), plan, ["memory/dream-log.md"]);
  await expectCode("RUN_ACTIVE", () => beginRun(root, createRunId(), plan, ["memory/dream-log.md"]));
});

await test("stale lock requires exact manual acknowledgement", async () => {
  const root = await workspace("stale");
  await addLog(root);
  const plan = await planFor(root);
  const runId = createRunId();
  await beginRun(root, runId, plan, ["memory/dream-log.md"]);
  const lockFile = path.join(root, LOCK_REL);
  const lock = JSON.parse(await fs.readFile(lockFile, "utf8"));
  lock.pid = 999_999_999;
  await writeJsonAtomic(lockFile, lock);
  await assert.rejects(
    () => beginRun(root, createRunId(), plan, ["memory/dream-log.md"]),
    (error) => error.code === "STALE_LOCK" && /inspect its manifest\/backups/.test(error.message),
  );
  await expectCode("CONFIRMATION", () => acknowledgeIncomplete(root, runId, "wrong"));
  const acknowledged = await acknowledgeIncomplete(root, runId, runId);
  assert(acknowledged.reviewedAt);
});

await test("crash after backup remains visible and blocks silent overwrite", async () => {
  const root = await workspace("crash");
  await addLog(root);
  const plan = await planFor(root);
  const runId = createRunId();
  await beginRun(root, runId, plan, ["memory/dream-log.md"]);
  const lockFile = path.join(root, LOCK_REL);
  const lock = JSON.parse(await fs.readFile(lockFile, "utf8"));
  lock.pid = 999_999_998;
  await writeJsonAtomic(lockFile, lock);
  await expectCode("STALE_LOCK", () => beginRun(root, createRunId(), plan, ["memory/dream-log.md"]));
  const manifest = JSON.parse(await fs.readFile(path.join(root, ".backup/memory-dreams", runId, "manifest.json"), "utf8"));
  assert.equal(manifest.status, "backed_up");
});

await test("unplanned Markdown change is caught", async () => {
  const root = await workspace("unplanned");
  await addLog(root);
  await write(path.join(root, "memory/topic.md"), "# Topic\n");
  const plan = await planFor(root);
  const runId = createRunId();
  const manifest = await beginRun(root, runId, plan, ["memory/dream-log.md"]);
  await verifyBeforeWrite(root, runId);
  await fs.appendFile(path.join(root, "memory/dream-log.md"), "\n## 🌙 Dream #104 · 2026-07-23 10:00\n");
  await fs.appendFile(path.join(root, "memory/topic.md"), "unplanned\n");
  const audit = await auditWorkspace(root, { manifest, files: ["memory/dream-log.md"] });
  assert(audit.errors.some((item) => item.code === "UNPLANNED_CHANGE"));
});

await test("daily log modification is caught by the audit", async () => {
  const root = await workspace("daily-audit");
  await addLog(root);
  const plan = await planFor(root);
  const runId = createRunId();
  const manifest = await beginRun(root, runId, plan, ["memory/dream-log.md"]);
  await verifyBeforeWrite(root, runId);
  await fs.appendFile(path.join(root, "memory/dream-log.md"), "\n## 🌙 Dream #104 · 2026-07-23 10:00\n");
  await fs.appendFile(path.join(root, "memory/2026-07-23.md"), "changed after write check\n");
  const audit = await auditWorkspace(root, { manifest, files: ["memory/dream-log.md"] });
  assert(audit.errors.some((item) => item.code === "DAILY_LOG_CHANGED"));
});

await test("partial planned writes become incomplete and do not advance state", async () => {
  const root = await workspace("partial");
  await addLog(root);
  const plan = await planFor(root);
  const runId = createRunId();
  await beginRun(root, runId, plan, ["MEMORY.md", "memory/dream-log.md"]);
  await verifyBeforeWrite(root, runId);
  const originalDiary = await fs.readFile(path.join(root, "memory/dream-log.md"), "utf8");
  const result = await finalizeRun(root, runId, {
    number: 104,
    timestamp: "2026-07-23 10:00",
    trigger: "auto",
    durationMinutes: 1,
    newLogCount: 1,
    changes: ["Diary only"],
    note: "Simulated partial write.",
  });
  assert.equal(result.ok, false);
  assert.equal(await fs.readFile(path.join(root, "memory/dream-log.md"), "utf8"), originalDiary);
  assert.equal(await fs.stat(path.join(root, STATE_REL)).then(() => true, () => false), false);
});

await test("invalid diary entry is rejected without writing the diary", async () => {
  const root = await workspace("diary-entry-invalid");
  await addLog(root);
  const plan = await planFor(root);
  const runId = createRunId();
  await beginRun(root, runId, plan, ["memory/dream-log.md"]);
  await verifyBeforeWrite(root, runId);
  const before = await fs.readFile(path.join(root, "memory/dream-log.md"), "utf8");
  const result = await finalizeRun(root, runId, {
    number: 104,
    timestamp: "2026-07-23 10:00",
    trigger: "auto",
    durationMinutes: 1,
    newLogCount: 1,
    changes: [],
    note: "Invalid because changes is empty.",
  });
  assert.equal(result.ok, false);
  assert.equal(result.error.code, "DIARY_ENTRY_INVALID");
  assert.equal(await fs.readFile(path.join(root, "memory/dream-log.md"), "utf8"), before);
});

await test("successful guarded run commits manifest and state", async () => {
  const root = await workspace("success");
  await addLog(root);
  const plan = await planFor(root);
  const runId = createRunId();
  await beginRun(root, runId, plan, ["MEMORY.md", "memory/dream-log.md"]);
  await verifyBeforeWrite(root, runId);
  await write(path.join(root, "MEMORY.md"), "# Memory\n\nCurrent state.\n");
  const result = await finalizeRun(root, runId, {
    number: 104,
    timestamp: "2026-07-23 10:00",
    trigger: "manual",
    durationMinutes: 2,
    newLogCount: 1,
    changes: ["Updated MEMORY.md"],
    note: "Commit fixture.",
  });
  assert.equal(result.ok, true);
  assert.equal(result.manifest.status, "committed");
  assert.equal(result.state.lastDreamNumber, 104);
  assert.equal(await fs.stat(path.join(root, LOCK_REL)).then(() => true, () => false), false);
});

await test("broken MEMORY.md pointer is detected", async () => {
  const root = await workspace("pointer");
  await write(path.join(root, "MEMORY.md"), "Details: `memory/missing.md`\n");
  const audit = await auditWorkspace(root);
  assert(audit.errors.some((item) => item.code === "BROKEN_POINTER"));
});

await test("run id includes second precision and collision suffix", async () => {
  const first = createRunId(new Date("2026-07-23T10:09:17Z"));
  const second = createRunId(new Date("2026-07-23T10:09:17Z"));
  assert.match(first, /^20260723-100917-[a-f0-9]{6}$/);
  assert.notEqual(first, second);
});

for (const root of roots) {
  await fs.rm(root, { recursive: true, force: true });
}

const failures = results.filter((item) => !item.ok);
const report = {
  schema: "signal-dreaming.self-test.v3",
  version: "3.0.0-rc.1",
  platform: process.platform,
  arch: process.arch,
  node: process.versions.node,
  limits: {
    bootstrapDays: 7,
    maxLogsPerRun: MAX_LOGS_PER_RUN,
    maxInputBytes: MAX_INPUT_BYTES,
  },
  passed: results.length - failures.length,
  failed: failures.length,
  results,
};
process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
if (failures.length) process.exitCode = 1;
