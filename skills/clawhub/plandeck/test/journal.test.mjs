// journal.test.mjs — mission journal state, privacy, ordering, and actor tests.

import { test } from "node:test";
import assert from "node:assert/strict";
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import {
  describeEntry,
  logArchived,
  logTransitions,
  readJournal,
  readLastState,
  recentForNext,
  resolveActor,
} from "../scripts/lib/journal.mjs";

function fixture(name) {
  return mkdtempSync(join(tmpdir(), `plandeck-journal-${name}-`));
}

function liveCard(id, options = {}) {
  return {
    id,
    column: options.column || "backlog",
    status: options.status || "queued",
    receipt: options.receipt ?? null,
  };
}

function journalPath(root) {
  return join(root, ".plandeck", "journal.ndjson");
}

function writeJournal(root, entries) {
  mkdirSync(join(root, ".plandeck"), { recursive: true });
  writeFileSync(journalPath(root), `${entries.map((entry) => JSON.stringify(entry)).join("\n")}\n`);
}

test("logTransitions writes a synthetic baseline on first observation", () => {
  const root = fixture("baseline");
  try {
    logTransitions(root, [liveCard("A"), liveCard("B")]);
    const entries = readJournal(root);
    assert.equal(entries.length, 1);
    assert.deepEqual(entries[0], {
      ts: entries[0].ts,
      cardId: null,
      field: "plan",
      from: null,
      to: "loaded (2 cards)",
      actor: "unknown-agent",
    });
    assert.deepEqual(Object.keys(readLastState(root).cards), ["A", "B"]);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("logTransitions records effective column changes", () => {
  const root = fixture("column");
  try {
    logTransitions(root, [liveCard("A", { column: "backlog" })]);
    logTransitions(root, [liveCard("A", { column: "ready" })], { actor: "agent-a" });
    const entry = readJournal(root)[0];
    assert.deepEqual({ field: entry.field, from: entry.from, to: entry.to, actor: entry.actor }, {
      field: "column", from: "backlog", to: "ready", actor: "agent-a",
    });
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("logTransitions records status changes independently of column", () => {
  const root = fixture("status");
  try {
    logTransitions(root, [liveCard("A", { column: "doing", status: "queued" })]);
    logTransitions(root, [liveCard("A", { column: "doing", status: "active" })]);
    const entries = readJournal(root);
    assert.equal(entries[0].field, "status");
    assert.equal(entries[0].from, "queued");
    assert.equal(entries[0].to, "active");
    assert.equal(entries.some((entry) => entry.field === "column"), false);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("logTransitions detects a card added after the baseline", () => {
  const root = fixture("added");
  try {
    logTransitions(root, [liveCard("A")]);
    logTransitions(root, [liveCard("A"), liveCard("B")]);
    assert.deepEqual(readJournal(root)[0], {
      ts: readJournal(root)[0].ts,
      cardId: "B",
      field: "card",
      from: null,
      to: "added",
      actor: "unknown-agent",
    });
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("logTransitions detects a card removed without archive", () => {
  const root = fixture("removed");
  try {
    logTransitions(root, [liveCard("A"), liveCard("B", { column: "doing" })]);
    logTransitions(root, [liveCard("A")]);
    const entry = readJournal(root)[0];
    assert.deepEqual({ cardId: entry.cardId, field: entry.field, from: entry.from, to: entry.to }, {
      cardId: "B", field: "card", from: "doing", to: "removed",
    });
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("receipt transitions store only a fingerprint and character length", () => {
  const root = fixture("receipt");
  const secret = "private receipt body";
  try {
    logTransitions(root, [liveCard("A")]);
    logTransitions(root, [liveCard("A", { receipt: secret })]);
    const raw = readFileSync(journalPath(root), "utf8");
    const entry = readJournal(root)[0];
    assert.equal(entry.field, "receipt");
    assert.match(entry.to, /^[a-f0-9]{10}:20$/);
    assert.doesNotMatch(raw, /private receipt body/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("a corrupt last-state cache re-baselines instead of throwing", () => {
  const root = fixture("corrupt-state");
  try {
    mkdirSync(join(root, ".plandeck"), { recursive: true });
    writeFileSync(join(root, ".plandeck", "last-state.json"), "{broken");
    assert.doesNotThrow(() => logTransitions(root, [liveCard("A")]));
    assert.equal(readJournal(root)[0].to, "loaded (1 cards)");
    assert.deepEqual(Object.keys(readLastState(root).cards), ["A"]);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("logArchived records lifecycle entries and preserves unrelated state", () => {
  const root = fixture("archive");
  try {
    logTransitions(root, [liveCard("A", { column: "done", status: "done" }), liveCard("B")]);
    logArchived(root, [{ id: "A", column: "done" }], { actor: "archiver" });
    const entry = readJournal(root)[0];
    assert.deepEqual({ cardId: entry.cardId, field: entry.field, from: entry.from, to: entry.to, actor: entry.actor }, {
      cardId: "A", field: "lifecycle", from: "done", to: "archived", actor: "archiver",
    });
    assert.deepEqual(Object.keys(readLastState(root).cards), ["B"]);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("readJournal filters by timestamp and returns newest-first", () => {
  const root = fixture("read");
  try {
    writeJournal(root, [
      { ts: "2026-07-10T08:00:00.000Z", cardId: "A", field: "column", from: "backlog", to: "ready", actor: "a" },
      { ts: "2026-07-11T08:00:00.000Z", cardId: "B", field: "column", from: "ready", to: "doing", actor: "b" },
      { ts: "2026-07-12T08:00:00.000Z", cardId: "C", field: "status", from: "queued", to: "active", actor: "c" },
    ]);
    assert.deepEqual(readJournal(root, { since: "2026-07-11T00:00:00Z" }).map((entry) => entry.cardId), ["C", "B"]);
    assert.deepEqual(readJournal(root, { limit: 2 }).map((entry) => entry.cardId), ["C", "B"]);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("recentForNext caps entries and returns them oldest-first", () => {
  const root = fixture("recent");
  try {
    writeJournal(root, Array.from({ length: 6 }, (_, index) => ({
      ts: `2026-07-${String(index + 1).padStart(2, "0")}T08:00:00.000Z`,
      cardId: String(index + 1),
      field: "card",
      from: null,
      to: "added",
      actor: "agent",
    })));
    assert.deepEqual(recentForNext(root, 3).map((entry) => entry.cardId), ["4", "5", "6"]);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("resolveActor follows explicit, environment, and fallback precedence", () => {
  const previous = process.env.PLANDECK_ACTOR;
  try {
    process.env.PLANDECK_ACTOR = "environment-agent";
    assert.equal(resolveActor("  explicit\nagent\u0000  "), "explicit agent");
    assert.equal(resolveActor(), "environment-agent");
    delete process.env.PLANDECK_ACTOR;
    assert.equal(resolveActor(), "unknown-agent");
    assert.equal(resolveActor("x".repeat(80)).length, 64);
  } finally {
    if (previous === undefined) delete process.env.PLANDECK_ACTOR;
    else process.env.PLANDECK_ACTOR = previous;
  }
});

test("describeEntry renders receipt fingerprints without receipt text", () => {
  const output = describeEntry({
    ts: "2026-07-14T09:12:00.000Z",
    cardId: "C007",
    field: "receipt",
    from: null,
    to: "a1b2c3d4e5:212",
    actor: "unknown-agent",
    receipt: "must not appear",
  });
  assert.match(output, /C007 receipt updated \(a1b2c3d4e5:212\)/);
  assert.match(output, /2026-07-14 09:12 UTC/);
  assert.doesNotMatch(output, /must not appear/);
});

test("one observation appends transitions in deterministic id and field order", () => {
  const root = fixture("order");
  try {
    logTransitions(root, [
      liveCard("A", { column: "backlog", status: "queued", receipt: "old" }),
      liveCard("B", { column: "ready", status: "queued" }),
    ]);
    logTransitions(root, [
      liveCard("B", { column: "doing", status: "active" }),
      liveCard("A", { column: "review", status: "active", receipt: "new" }),
    ]);
    const lines = readFileSync(journalPath(root), "utf8").trim().split(/\r?\n/).map((line) => JSON.parse(line));
    assert.deepEqual(lines.slice(1).map((entry) => [entry.cardId, entry.field]), [
      ["A", "column"], ["A", "status"], ["A", "receipt"], ["B", "column"], ["B", "status"],
    ]);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});
