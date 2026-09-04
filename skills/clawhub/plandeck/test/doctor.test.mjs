// doctor.test.mjs — snapshot retention, diagnosis, restore, and atomic-write tests.

import { test } from "node:test";
import assert from "node:assert/strict";
import {
  existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { runDoctor } from "../scripts/doctor.mjs";
import { atomicWriteFile, parseYaml, stringifyYaml } from "../scripts/lib/deck.mjs";
import { readJournal } from "../scripts/lib/journal.mjs";
import { diffCardsSummary, listSnapshots, maybeSnapshot } from "../scripts/lib/snapshot.mjs";

const START = Date.parse("2026-07-14T08:00:00.000Z");

function fixture(name) {
  return mkdtempSync(join(tmpdir(), `plandeck-doctor-${name}-`));
}

function makePlan(root, cards) {
  mkdirSync(root, { recursive: true });
  const source = stringifyYaml({
    version: 1,
    plan: { title: "Doctor fixture", slug: "doctor-fixture", kind: "specific", status: "active" },
    cards,
  });
  writeFileSync(join(root, "plan.yaml"), source);
  return source;
}

function card(id, options = {}) {
  return {
    id,
    title: options.title || id,
    column: options.column || "backlog",
    status: options.status || "queued",
    estimate: options.estimate ?? 1,
  };
}

function quietly(fn) {
  const originalLog = console.log;
  const originalError = console.error;
  console.log = () => {};
  console.error = () => {};
  try {
    return fn();
  } finally {
    console.log = originalLog;
    console.error = originalError;
  }
}

test("maybeSnapshot creates the first snapshot and skips unchanged content", () => {
  const root = fixture("first");
  try {
    makePlan(root, [card("A")]);
    assert.ok(maybeSnapshot(root, START));
    assert.equal(maybeSnapshot(root, START + 1), null);
    assert.equal(listSnapshots(root).length, 1);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("maybeSnapshot creates a new snapshot after plan content changes", () => {
  const root = fixture("changed");
  try {
    makePlan(root, [card("A")]);
    maybeSnapshot(root, START);
    makePlan(root, [card("A", { column: "doing", status: "active" })]);
    maybeSnapshot(root, START + 1);
    assert.equal(listSnapshots(root).length, 2);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("maybeSnapshot retains only the newest twenty snapshots", () => {
  const root = fixture("prune");
  try {
    for (let index = 0; index < 25; index += 1) {
      makePlan(root, [card("A", { title: `Revision ${index}` })]);
      maybeSnapshot(root, START + index);
    }
    const snapshots = listSnapshots(root);
    assert.equal(snapshots.length, 20);
    assert.equal(snapshots[0].ts, "20260714T080000024Z");
    assert.equal(snapshots.at(-1).ts, "20260714T080000005Z");
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("snapshot filenames are legal on Windows and contain no colons", () => {
  const root = fixture("filename");
  try {
    makePlan(root, [card("A")]);
    maybeSnapshot(root, START);
    const [snapshot] = listSnapshots(root);
    assert.match(snapshot.file, /^plan-\d{8}T\d{9}Z\.yaml$/);
    assert.doesNotMatch(snapshot.file, /:/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("listSnapshots returns snapshot metadata newest-first", () => {
  const root = fixture("list");
  try {
    makePlan(root, [card("A")]);
    maybeSnapshot(root, START);
    makePlan(root, [card("B")]);
    maybeSnapshot(root, START + 10);
    const snapshots = listSnapshots(root);
    assert.deepEqual(snapshots.map((snapshot) => snapshot.ts), ["20260714T080000010Z", "20260714T080000000Z"]);
    assert.ok(snapshots.every((snapshot) => snapshot.path.endsWith(snapshot.file)));
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("diffCardsSummary reports added, removed, and selected changed fields", () => {
  const diff = diffCardsSummary(
    [card("A"), card("B", { estimate: 2 }), card("D")],
    [card("B", { column: "doing", status: "active", estimate: 3 }), card("C")],
  );
  assert.deepEqual(diff.added, ["C"]);
  assert.deepEqual(diff.removed, ["A", "D"]);
  assert.deepEqual(diff.changed, [{
    id: "B",
    fields: [
      { name: "column", from: "backlog", to: "doing" },
      { name: "status", from: "queued", to: "active" },
      { name: "estimate", from: 2, to: 3 },
    ],
  }]);
});

test("runDoctor reports a healthy plan, snapshot count, and newest diff", () => {
  const root = fixture("healthy");
  try {
    makePlan(root, [card("A")]);
    maybeSnapshot(root, START);
    makePlan(root, [card("A", { column: "doing", status: "active" }), card("B")]);
    const result = quietly(() => runDoctor(root, { json: true }));
    assert.equal(result.ok, true);
    assert.equal(result.healthy, true);
    assert.equal(result.snapshotCount, 1);
    assert.equal(result.newestSnapshot.ts, "20260714T080000000Z");
    assert.deepEqual(result.diff.added, ["B"]);
    assert.deepEqual(result.diff.changed[0].fields.map((field) => field.name), ["column", "status"]);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("runDoctor surfaces a broken plan and annotates snapshots newest-first", () => {
  const root = fixture("broken");
  try {
    makePlan(root, [card("A")]);
    maybeSnapshot(root, START);
    makePlan(root, [card("A", { column: "doing", status: "active" }), card("B")]);
    maybeSnapshot(root, START + 1);
    writeFileSync(join(root, "plan.yaml"), "version: 1\n plan:\n");
    const result = quietly(() => runDoctor(root, { json: true }));
    assert.equal(result.ok, false);
    assert.match(result.error, /Unsupported odd indentation at line 2/);
    assert.deepEqual(result.snapshots.map((snapshot) => snapshot.ts), ["20260714T080000001Z", "20260714T080000000Z"]);
    assert.match(result.snapshots[0].summary, /added B; changed A/);
    assert.equal(result.snapshots[1].summary, "baseline snapshot");
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("runDoctor restore latest saves corruption and restores the newest snapshot", () => {
  const root = fixture("restore-latest");
  try {
    makePlan(root, [card("A")]);
    maybeSnapshot(root, START);
    const expected = makePlan(root, [card("B", { column: "doing", status: "active" })]);
    maybeSnapshot(root, START + 1);
    const broken = "version: 1\n plan:\n";
    writeFileSync(join(root, "plan.yaml"), broken);
    const result = quietly(() => runDoctor(root, { restore: "latest", actor: "repair-agent", json: true }));
    assert.equal(result.ok, true);
    assert.equal(result.restored, true);
    assert.equal(readFileSync(join(root, "plan.yaml"), "utf8"), expected);
    assert.equal(readFileSync(join(root, "plan.yaml.corrupt"), "utf8"), broken);
    assert.equal(parseYaml(readFileSync(join(root, "plan.yaml"), "utf8")).cards[0].id, "B");
    const journal = readJournal(root);
    assert.deepEqual({ field: journal[0].field, from: journal[0].from, to: journal[0].to, actor: journal[0].actor }, {
      field: "plan",
      from: "corrupt",
      to: "restored (plan-20260714T080000001Z.yaml)",
      actor: "repair-agent",
    });
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("runDoctor restores an exact non-newest snapshot token", () => {
  const root = fixture("restore-exact");
  try {
    const oldest = makePlan(root, [card("A")]);
    maybeSnapshot(root, START);
    makePlan(root, [card("B")]);
    maybeSnapshot(root, START + 1);
    const current = makePlan(root, [card("C")]);
    const result = quietly(() => runDoctor(root, { restore: "20260714T080000000Z", json: true }));
    assert.equal(result.snapshot.ts, "20260714T080000000Z");
    assert.equal(readFileSync(join(root, "plan.yaml"), "utf8"), oldest);
    assert.equal(readFileSync(join(root, "plan.yaml.corrupt"), "utf8"), current);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("runDoctor rejects an unknown snapshot without touching plan.yaml", () => {
  const root = fixture("restore-missing");
  try {
    const current = makePlan(root, [card("A")]);
    maybeSnapshot(root, START);
    const result = quietly(() => runDoctor(root, { restore: "20990101T000000000Z", json: true }));
    assert.equal(result.ok, false);
    assert.match(result.error, /Snapshot not found/);
    assert.equal(readFileSync(join(root, "plan.yaml"), "utf8"), current);
    assert.equal(existsSync(join(root, "plan.yaml.corrupt")), false);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("runDoctor never creates snapshots as a diagnosis side effect", () => {
  const root = fixture("single-purpose");
  try {
    makePlan(root, [card("A")]);
    assert.equal(listSnapshots(root).length, 0);
    const result = quietly(() => runDoctor(root, { json: true }));
    assert.equal(result.ok, true);
    assert.equal(listSnapshots(root).length, 0);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("atomicWriteFile removes its temporary file after rename failure", () => {
  const root = fixture("atomic-cleanup");
  try {
    const target = join(root, "target");
    mkdirSync(target);
    assert.throws(() => atomicWriteFile(target, "replacement"));
    assert.equal(statSync(target).isDirectory(), true);
    assert.deepEqual(readdirSync(root).filter((name) => name.startsWith(".target.") && name.endsWith(".tmp")), []);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});
