// deck.test.mjs — deterministic engine and live-server acceptance tests.
//
// Covers pure graph logic, YAML archiving, hub routing, watcher refreshes, and stale payload recovery.
import { test } from "node:test";
import assert from "node:assert/strict";
import { request as httpRequest } from "node:http";
import { fileURLToPath } from "node:url";
import {
  existsSync, mkdtempSync, mkdirSync, readFileSync, readdirSync, rmSync, statSync, unlinkSync, utimesSync, writeFileSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import {
  annotate, criticalPath, effectiveColumn, nextAction, rollup, topoOrder,
} from "../scripts/lib/intelligence.mjs";
import { archiveDoneCards, buildPayload, normalizePlan, parseYaml, stringifyYaml } from "../scripts/lib/deck.mjs";
import { checkPlan } from "../scripts/check-plan.mjs";
import { runBoard } from "../scripts/board.mjs";
import { appendJournalEntry, logTransitions, readJournal, readLastState } from "../scripts/lib/journal.mjs";
import { runCli as executeCli } from "../scripts/cli.mjs";

const here = dirname(fileURLToPath(import.meta.url));

// Isolate hub discovery per test process: node --test runs files in parallel,
// and a shared breadcrumb would let one file's tests register with another
// file's hub (the exact cross-talk that broke CI on Node 22).
process.env.PLANDECK_HUB_BREADCRUMB = join(mkdtempSync(join(tmpdir(), "plandeck-hub-test-")), "hub.json");

// Build normalized-ish cards for unit tests.
function card(id, opts = {}) {
  return {
    id,
    title: opts.title || id,
    column: opts.column || "backlog",
    status: opts.status || "queued",
    estimate: opts.estimate ?? null,
    priority: opts.priority || null,
    depends_on: opts.depends_on || [],
  };
}

function makePlan(dir, { title, slug = "plan", cards }) {
  mkdirSync(dir, { recursive: true });
  writeFileSync(join(dir, "plan.yaml"), stringifyYaml({
    version: 1,
    plan: { title, slug, kind: "specific", status: "active" },
    cards,
  }));
}

async function quietly(fn) {
  const original = console.log;
  console.log = () => {};
  try {
    return await fn();
  } finally {
    console.log = original;
  }
}

async function waitFor(fn, timeout = 3000) {
  const deadline = Date.now() + timeout;
  let lastError = null;
  while (Date.now() < deadline) {
    try {
      const value = await fn();
      if (value) return value;
    } catch (error) {
      lastError = error;
    }
    await new Promise((resolveWait) => setTimeout(resolveWait, 30));
  }
  if (lastError) throw lastError;
  throw new Error(`Condition was not met within ${timeout}ms.`);
}

function requestRaw(url, options = {}, body = "") {
  return new Promise((resolveRequest, rejectRequest) => {
    const req = httpRequest(url, options, (res) => {
      const chunks = [];
      res.on("data", (chunk) => chunks.push(chunk));
      res.on("end", () => resolveRequest({
        status: res.statusCode,
        headers: res.headers,
        body: Buffer.concat(chunks).toString("utf8"),
      }));
    });
    req.on("error", rejectRequest);
    req.end(body);
  });
}

async function captureConsole(fn) {
  const output = { log: [], error: [] };
  const originalLog = console.log;
  const originalError = console.error;
  console.log = (...values) => output.log.push(values.join(" "));
  console.error = (...values) => output.error.push(values.join(" "));
  try {
    output.result = await fn();
    return output;
  } finally {
    console.log = originalLog;
    console.error = originalError;
  }
}

async function invokeCli(args) {
  const captured = await captureConsole(() => executeCli(args));
  return {
    status: captured.result,
    stdout: captured.log.join("\n"),
    stderr: captured.error.join("\n"),
  };
}

test("topoOrder linearizes a chain and finds no cycle", () => {
  const cards = [card("C", { depends_on: ["B"] }), card("B", { depends_on: ["A"] }), card("A")];
  const { order, cycle } = topoOrder(cards);
  assert.equal(cycle, null);
  assert.deepEqual(order, ["A", "B", "C"]);
});

test("topoOrder detects a dependency cycle", () => {
  const cards = [card("A", { depends_on: ["B"] }), card("B", { depends_on: ["A"] })];
  const { cycle } = topoOrder(cards);
  assert.ok(cycle && cycle.length === 2, "both cyclic nodes reported");
});

test("criticalPath returns the longest points-weighted chain", () => {
  // A(2) -> B(3) -> D(5)   and   A(2) -> C(8)      longest by points = A,B,D (10) vs A,C (10). Tie -> lower id chain.
  const cards = [
    card("A", { estimate: 2 }),
    card("B", { estimate: 3, depends_on: ["A"] }),
    card("C", { estimate: 8, depends_on: ["A"] }),
    card("D", { estimate: 5, depends_on: ["B"] }),
  ];
  const cp = criticalPath(cards);
  assert.equal(cp.length, 10);
  assert.ok(cp.onPath.has("A"));
  // D-chain (A,B,D) and C-chain (A,C) both total 10; endpoint tie broken to lower id "C".
  assert.deepEqual(cp.chain, ["A", "C"]);
});

test("annotate auto-promotes a backlog card whose deps are all done to ready", () => {
  const cards = [
    card("A", { column: "done", status: "done", estimate: 1 }),
    card("B", { column: "backlog", depends_on: ["A"], estimate: 2 }),
    card("C", { column: "backlog", depends_on: ["B"], estimate: 2 }),
  ];
  annotate(cards);
  assert.equal(effectiveColumn(cards[1]), "ready", "B is ready (A done)");
  assert.equal(effectiveColumn(cards[2]), "backlog", "C stays backlog (B not done)");
  assert.equal(cards[1]._ready, true);
  assert.equal(cards[2]._ready, false);
});

test("blocked status wins its own lane regardless of column", () => {
  const cards = [card("A", { column: "doing", status: "blocked" })];
  annotate(cards);
  assert.equal(effectiveColumn(cards[0]), "blocked");
});

test("rollup computes honest percent from points", () => {
  const cards = [
    card("A", { column: "done", status: "done", estimate: 3 }),
    card("B", { column: "done", status: "done", estimate: 2 }),
    card("C", { estimate: 5 }),
  ];
  annotate(cards);
  const r = rollup(cards);
  assert.equal(r.totalPoints, 10);
  assert.equal(r.donePoints, 5);
  assert.equal(r.pct, 50);
});

test("unestimated cards use the same one-point unit in rollups and critical paths", () => {
  const cards = [
    card("A", { column: "done", status: "done" }),
    card("B", { depends_on: ["A"] }),
  ];
  annotate(cards);
  const r = rollup(cards);
  const cp = criticalPath(cards);
  assert.equal(r.totalPoints, 2);
  assert.equal(r.donePoints, 1);
  assert.equal(r.pct, 50);
  assert.equal(cp.length, 2);
  assert.deepEqual(cp.chain, ["A", "B"]);
});

test("nextAction prefers the active card, then critical-path ready", () => {
  const active = [card("A", { column: "doing", status: "active" }), card("B", { column: "ready" })];
  annotate(active);
  assert.equal(nextAction(active).cardId, "A");
  assert.equal(nextAction(active).reason, "active");

  const done = card("A", { column: "done", status: "done", estimate: 2 });
  const onPath = card("B", { column: "backlog", depends_on: ["A"], estimate: 5, priority: "P2" });
  const offPath = card("C", { column: "backlog", depends_on: ["A"], estimate: 1, priority: "P1" });
  const cards = [done, onPath, offPath];
  annotate(cards);
  const n = nextAction(cards);
  assert.equal(n.reason, "ready");
  assert.equal(n.cardId, "B", "critical-path card beats higher priority off-path");
});

test("nextAction surfaces a blocker when nothing is ready", () => {
  const cards = [card("A", { column: "blocked", status: "blocked" }), card("B", { column: "backlog", depends_on: ["A"] })];
  annotate(cards);
  const n = nextAction(cards);
  assert.equal(n.reason, "blocked");
});

test("nextAction distinguishes an empty plan from a completed plan", () => {
  assert.deepEqual(nextAction([]), {
    cardId: null,
    title: null,
    reason: "empty",
    detail: "No cards yet. Add the first card to plan.yaml.",
  });
  assert.equal(nextAction([], undefined, 2).reason, "complete");
});

test("parseYaml reads the plan subset (mappings, lists, inline arrays, comments)", () => {
  const doc = parseYaml(`version: 1
plan:
  title: "Demo"   # a comment
  slug: demo
cards:
  - id: C001
    depends_on: [C000, C002]
    estimate: 3
`);
  assert.equal(doc.version, 1);
  assert.equal(doc.plan.title, "Demo");
  assert.deepEqual(doc.cards[0].depends_on, ["C000", "C002"]);
  assert.equal(doc.cards[0].estimate, 3);
});

test("normalizePlan rejects duplicate card ids", () => {
  const doc = { version: 1, plan: { title: "x" }, cards: [{ id: "C1" }, { id: "C1" }] };
  assert.throws(() => normalizePlan(doc), /Duplicate card id/);
});

test("integration: the shipped sample plan computes the expected critical path and progress", () => {
  const payload = buildPayload(join(here, "..", "examples", "ship-onboarding-flow"), Date.parse("2026-07-12T12:00:00Z"));
  assert.deepEqual(payload.criticalPath.chain, ["C001", "C002", "C003", "C004", "C008", "C009"]);
  assert.equal(payload.criticalPath.length, 17);
  assert.equal(payload.rollup.totalPoints, 34);
  assert.equal(payload.rollup.donePoints, 5);
  assert.equal(payload.nextAction.cardId, "C003");
  const ready = payload.cards.filter((c) => c.column === "ready").map((c) => c.id).sort();
  assert.deepEqual(ready, ["C005", "C010"]);
});

test("ETA derives observed velocity from at least three dated completions", () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-velocity-"));
  try {
    makePlan(root, {
      title: "Velocity fixture",
      cards: [
        { id: "A", title: "Done one", column: "done", status: "done", estimate: 2, updated_at: "2026-07-01T00:00:00Z" },
        { id: "B", title: "Done two", column: "done", status: "done", estimate: 3, updated_at: "2026-07-03T00:00:00Z" },
        { id: "D", title: "Remaining", column: "backlog", estimate: 4 },
      ],
    });
    writeFileSync(join(root, "archive.yaml"), stringifyYaml({
      version: 1,
      archived: [
        { id: "C", title: "Archived", column: "done", status: "done", estimate: 5, archived_at: "2026-07-05T00:00:00Z" },
      ],
    }));

    const observed = buildPayload(root, Date.parse("2026-07-10T00:00:00Z"));
    assert.deepEqual(observed.eta, {
      velocity: 2.5,
      basis: "observed",
      remainingPoints: 4,
      days: 2,
      date: "2026-07-12",
    });

    const configuredDoc = parseYaml(readFileSync(join(root, "plan.yaml"), "utf8"));
    configuredDoc.plan.velocity = 4;
    writeFileSync(join(root, "plan.yaml"), stringifyYaml(configuredDoc));
    const configured = buildPayload(root, Date.parse("2026-07-10T00:00:00Z"));
    assert.equal(configured.eta.velocity, 4);
    assert.equal(configured.eta.basis, "configured");
    assert.equal(configured.eta.days, 1);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("blocked cards age after one day", () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-aging-"));
  try {
    makePlan(root, {
      title: "Aging fixture",
      cards: [
        {
          id: "A",
          title: "Blocked card",
          column: "blocked",
          status: "blocked",
          estimate: 1,
          updated_at: "2026-07-10T00:00:00Z",
        },
      ],
    });
    const payload = buildPayload(root, Date.parse("2026-07-12T00:00:00Z"));
    assert.equal(payload.cards[0].aging, true);
    assert.equal(payload.cards[0].ageDays, 2);
    assert.match(payload.warnings.find((warning) => warning.kind === "aging").detail, /A \(2d\)/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("an empty plan reports no cards yet and is not complete", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-empty-"));
  try {
    makePlan(root, { title: "Empty fixture", cards: [] });
    const payload = buildPayload(root);
    assert.equal(payload.nextAction.reason, "empty");
    assert.match(payload.nextAction.detail, /No cards yet/);
    const checked = await quietly(() => checkPlan(root, { json: true }));
    assert.equal(checked.complete, false);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("hub registers boards on one port, resolves slug collisions, and cleans up", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-hub-"));
  const firstDir = join(root, "first");
  const secondDir = join(root, "second");
  let hub = null;

  try {
    makePlan(firstDir, {
      title: "First board",
      slug: "x",
      cards: [{ id: "A", title: "First card", column: "backlog", estimate: 1 }],
    });
    makePlan(secondDir, {
      title: "Second board",
      slug: "x",
      cards: [{ id: "B", title: "Second card", column: "backlog", estimate: 2 }],
    });

    hub = await quietly(() => runBoard({ planDir: firstDir, port: 0, host: "127.0.0.1" }));
    const registered = await quietly(() => runBoard({ planDir: secondDir, port: hub.port, host: "127.0.0.1" }));
    assert.equal(registered.registered, true);
    assert.equal(registered.boardPath, "/x-2/");
    assert.equal(typeof registered.close, "function", "registration returns the same close contract as the hub branch");

    const repeated = await quietly(() => runBoard({ planDir: secondDir, port: hub.port, host: "127.0.0.1" }));
    assert.equal(repeated.boardPath, "/x-2/", "registering the same root is idempotent");

    const base = "http://127.0.0.1:" + hub.port;
    const state = await fetch(base + "/api/boards").then((response) => response.json());
    assert.equal(state.hub, true);
    assert.deepEqual(state.boards.map((board) => board.boardPath), ["/x-2/", "/x/"]);
    assert.deepEqual(state.boards.map((board) => board.title).sort(), ["First board", "Second board"]);
    assert.ok(state.boards.every((board) => typeof board.rollup.pct === "number"));

    const secondPayload = await fetch(base + "/x-2/api/board").then((response) => response.json());
    assert.equal(secondPayload.plan.title, "Second board", "longest matching board prefix routes correctly");

    const index = await fetch(base + "/").then((response) => response.text());
    assert.match(index, /First board/);
    assert.match(index, /Second board/);
    assert.match(index, /events\.onopen=.*setLive\(true\)/);
    assert.match(index, /events\.onerror=.*setLive\(false\)/);

    const wrongType = await fetch(base + "/api/boards", {
      method: "POST",
      headers: { "Content-Type": "text/plain" },
      body: JSON.stringify({ planDir: secondDir }),
    });
    assert.equal(wrongType.status, 415);

    const untrustedPost = await requestRaw(base + "/api/boards", {
      method: "POST",
      headers: { "Content-Type": "application/json", Host: "evil.example" },
    }, JSON.stringify({ planDir: secondDir }));
    assert.equal(untrustedPost.status, 403);

    const untrustedDelete = await requestRaw(base + "/api/boards?path=" + encodeURIComponent("/x-2/"), {
      method: "DELETE",
      headers: { "Content-Type": "application/json", Host: "evil.example" },
    });
    assert.equal(untrustedDelete.status, 403);

    const removed = await fetch(base + "/api/boards?path=" + encodeURIComponent("/x-2/"), {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
    });
    assert.equal(removed.status, 200);
    const afterDelete = await fetch(base + "/api/boards").then((response) => response.json());
    assert.deepEqual(afterDelete.boards.map((board) => board.boardPath), ["/x/"]);

    unlinkSync(join(firstDir, "plan.yaml"));
    await waitFor(async () => {
      const current = await fetch(base + "/api/boards").then((response) => response.json());
      return current.boards.length === 0;
    });

    const unknown = await fetch(base + "/not-a-board");
    assert.equal(unknown.status, 404);
    assert.match(await unknown.text(), /Do not kill the hub/);
  } finally {
    if (hub) await hub.close();
    rmSync(root, { recursive: true, force: true });
  }
});

test("hub breadcrumb discovers an ephemeral hub and preserves archived index counts", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-breadcrumb-"));
  const firstDir = join(root, "first");
  const secondDir = join(root, "second");
  const breadcrumbPath = process.env.PLANDECK_HUB_BREADCRUMB;
  let hub = null;
  try {
    makePlan(firstDir, {
      title: "Archived board",
      slug: "archived-board",
      cards: [
        { id: "A", title: "Done", column: "done", status: "done", estimate: 3 },
        { id: "B", title: "Open", column: "backlog", estimate: 2 },
      ],
    });
    archiveDoneCards(firstDir, Date.parse("2026-07-14T10:00:00Z"));
    makePlan(secondDir, {
      title: "Discovered board",
      slug: "discovered-board",
      cards: [{ id: "C", title: "Open", column: "backlog", estimate: 1 }],
    });

    hub = await quietly(() => runBoard({ planDir: firstDir, port: 0, host: "127.0.0.1" }));
    const breadcrumb = JSON.parse(readFileSync(breadcrumbPath, "utf8"));
    assert.equal(breadcrumb.port, hub.port);
    assert.equal(breadcrumb.host, "127.0.0.1");
    assert.equal(breadcrumb.pid, process.pid);

    const registered = await quietly(() => runBoard({ planDir: secondDir, host: "127.0.0.1" }));
    assert.equal(registered.registered, true);
    assert.equal(registered.port, hub.port);
    assert.equal(typeof registered.close, "function");

    const state = await fetch(`http://127.0.0.1:${hub.port}/api/boards`).then((response) => response.json());
    const archivedBoard = state.boards.find((board) => board.boardPath === "/archived-board/");
    assert.equal(archivedBoard.rollup.pct, 60);
    assert.equal(archivedBoard.rollup.counts.done, 1);
    assert.equal(archivedBoard.rollup.counts.total, 2);

    await hub.close();
    assert.equal(existsSync(breadcrumbPath), false);
  } finally {
    if (hub) await hub.close();
    rmSync(root, { recursive: true, force: true });
  }
});

test("oversized registration bodies return 413 and close the connection cleanly", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-body-limit-"));
  let hub = null;
  try {
    makePlan(root, {
      title: "Body limit fixture",
      cards: [{ id: "A", title: "Open", column: "backlog", estimate: 1 }],
    });
    hub = await quietly(() => runBoard({ planDir: root, port: 0, host: "127.0.0.1" }));
    const base = `http://127.0.0.1:${hub.port}`;
    const response = await fetch(base + "/api/boards", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ planDir: "x".repeat(70 * 1024) }),
    });
    assert.equal(response.status, 413);
    assert.equal(response.headers.get("connection"), "close");
    assert.match(await response.text(), /too large/);

    const healthy = await fetch(base + "/api/boards");
    assert.equal(healthy.status, 200);
    assert.equal((await healthy.json()).hub, true);
  } finally {
    if (hub) await hub.close();
    rmSync(root, { recursive: true, force: true });
  }
});

test("archive moves done cards, preserves progress, and satisfies dependencies", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-archive-"));
  try {
    makePlan(root, {
      title: "Archive fixture",
      slug: "archive-fixture",
      cards: [
        { id: "A", title: "Finished", column: "done", status: "done", estimate: 3, priority: "P1" },
        { id: "B", title: "Pending", column: "backlog", estimate: 2, depends_on: ["A"] },
      ],
    });

    const before = buildPayload(root);
    const first = archiveDoneCards(root, Date.parse("2026-07-14T10:00:00Z"));
    assert.equal(first.archived, 1);
    assert.deepEqual(first.archivedIds, ["A"]);

    const planDoc = parseYaml(readFileSync(join(root, "plan.yaml"), "utf8"));
    const archiveDoc = parseYaml(readFileSync(join(root, "archive.yaml"), "utf8"));
    assert.deepEqual(Object.keys(planDoc), ["version", "plan", "cards"]);
    assert.deepEqual(planDoc.cards.map((entry) => entry.id), ["B"]);
    assert.deepEqual(archiveDoc.archived.map((entry) => entry.id), ["A"]);
    assert.equal(archiveDoc.archived[0].archived_at, "2026-07-14T10:00:00.000Z");

    const after = buildPayload(root);
    assert.equal(after.rollup.pct, before.rollup.pct);
    assert.equal(after.rollup.donePoints, before.rollup.donePoints);
    assert.equal(after.rollup.totalPoints, before.rollup.totalPoints);
    assert.deepEqual(after.rollup.archived, { count: 1, points: 3 });
    assert.deepEqual(after.cards[0].missingDeps, []);
    assert.deepEqual(after.cards[0].unmetDeps, []);
    assert.equal(after.cards[0].column, "ready");
    assert.equal(after.warnings.some((warning) => warning.kind === "dangling-dep"), false);

    const checked = await quietly(() => checkPlan(root, { json: true }));
    assert.equal(checked.ok, true);

    planDoc.cards[0].column = "done";
    writeFileSync(join(root, "plan.yaml"), stringifyYaml(planDoc));
    const second = archiveDoneCards(root, Date.parse("2026-07-14T11:00:00Z"));
    assert.equal(second.archived, 1);
    const appended = parseYaml(readFileSync(join(root, "archive.yaml"), "utf8"));
    assert.deepEqual(appended.archived.map((entry) => entry.id), ["A", "B"]);
    assert.equal(appended.archived[1].archived_at, "2026-07-14T11:00:00.000Z");

    const completePayload = buildPayload(root);
    assert.equal(completePayload.cards.length, 0);
    assert.deepEqual(completePayload.rollup.archived, { count: 2, points: 5 });
    assert.equal(completePayload.rollup.pct, 100);
    const completeCheck = await quietly(() => checkPlan(root, { json: true }));
    assert.equal(completeCheck.complete, true);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("archive removes only done card line ranges and preserves surrounding YAML bytes", () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-archive-format-"));
  try {
    const planSource = [
      "# plan header\r\n",
      "version: 1\r\n",
      "plan:\r\n",
      "  title: Hand formatted plan\r\n",
      "  slug: hand-format\r\n",
      "cards:\r\n",
      "  # archived card comment\r\n",
      "  - id: A # inline done\r\n",
      "    title: Finished card\r\n",
      "    status: done\r\n",
      "    column: done\r\n",
      "    # proof stays with removed card\r\n",
      "    estimate: 2\r\n",
      "\r\n",
      "  # surviving card comment\r\n",
      "  - id: B\r\n",
      "    title: Still queued\r\n",
      "    status: queued\r\n",
      "    column: backlog\r\n",
      "    # keep this formatting exactly\r\n",
      "    estimate: 3\r\n",
      "# plan footer\r\n",
    ].join("");
    const expectedPlan = [
      "# plan header\r\n",
      "version: 1\r\n",
      "plan:\r\n",
      "  title: Hand formatted plan\r\n",
      "  slug: hand-format\r\n",
      "cards:\r\n",
      "\r\n",
      "  # surviving card comment\r\n",
      "  - id: B\r\n",
      "    title: Still queued\r\n",
      "    status: queued\r\n",
      "    column: backlog\r\n",
      "    # keep this formatting exactly\r\n",
      "    estimate: 3\r\n",
      "# plan footer\r\n",
    ].join("");
    const archiveSource = [
      "# archive header\r\n",
      "version: 1\r\n",
      "archived:\r\n",
      "  # existing archive comment\r\n",
      "  - id: X\r\n",
      "    title: Existing card\r\n",
      "    status: done\r\n",
      "    estimate: 1\r\n",
      "# archive footer\r\n",
    ].join("");
    writeFileSync(join(root, "plan.yaml"), planSource);
    writeFileSync(join(root, "archive.yaml"), archiveSource);

    archiveDoneCards(root, Date.parse("2026-07-14T10:00:00Z"));
    assert.equal(readFileSync(join(root, "plan.yaml"), "utf8"), expectedPlan);

    const archiveAfter = readFileSync(join(root, "archive.yaml"), "utf8");
    assert.ok(archiveAfter.startsWith(archiveSource.slice(0, archiveSource.indexOf("# archive footer"))));
    assert.ok(archiveAfter.endsWith("# archive footer\r\n"));
    assert.match(archiveAfter, /# existing archive comment/);
    assert.deepEqual(parseYaml(archiveAfter).archived.map((entry) => entry.id), ["X", "A"]);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("archive refuses an id already present in archive.yaml without changing either file", () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-archive-duplicate-"));
  try {
    makePlan(root, {
      title: "Duplicate archive fixture",
      cards: [{ id: "A", title: "Original", column: "done", status: "done", estimate: 1 }],
    });
    writeFileSync(join(root, "archive.yaml"), "# empty archive\nversion: 1\narchived: [] # keep this comment\n");
    archiveDoneCards(root, Date.parse("2026-07-14T10:00:00Z"));
    assert.match(readFileSync(join(root, "archive.yaml"), "utf8"), /archived:  # keep this comment/);
    makePlan(root, {
      title: "Duplicate archive fixture",
      cards: [{ id: "A", title: "Reused", column: "done", status: "done", estimate: 2 }],
    });

    const planBefore = readFileSync(join(root, "plan.yaml"), "utf8");
    const archiveBefore = readFileSync(join(root, "archive.yaml"), "utf8");
    assert.throws(() => archiveDoneCards(root), /already exists in archive\.yaml: A/);
    assert.equal(readFileSync(join(root, "plan.yaml"), "utf8"), planBefore);
    assert.equal(readFileSync(join(root, "archive.yaml"), "utf8"), archiveBefore);
    assert.deepEqual(readdirSync(root).filter((name) => name.endsWith(".tmp")), []);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("note cache invalidates on change and disappearance while check reports note orphans", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-notes-"));
  try {
    makePlan(root, {
      title: "Notes fixture",
      cards: [
        { id: "A", title: "Live note", column: "backlog", note: "cards/live.md" },
        { id: "B", title: "Missing note", column: "backlog", note: "cards/missing.md" },
      ],
    });
    writeFileSync(join(root, "archive.yaml"), stringifyYaml({
      version: 1,
      archived: [
        { id: "C", title: "Archived note", status: "done", note: "cards/archived.md", archived_at: "2026-07-10T00:00:00Z" },
      ],
    }));
    mkdirSync(join(root, "cards"));
    const livePath = join(root, "cards", "live.md");
    writeFileSync(livePath, "alpha");
    writeFileSync(join(root, "cards", "archived.md"), "archive");
    writeFileSync(join(root, "cards", "orphan.md"), "orphan");

    const first = buildPayload(root);
    assert.equal(first.cards.find((entry) => entry.id === "A").noteContent, "alpha");
    assert.match(first.warnings.find((warning) => warning.kind === "missing-note").detail, /B.*cards\/missing\.md/);
    assert.match(first.warnings.find((warning) => warning.kind === "orphan-note").detail, /cards\/orphan\.md/);
    assert.equal(first.warnings.some((warning) => warning.detail.includes("cards/archived.md")), false);

    writeFileSync(livePath, "beta");
    const future = new Date(Date.now() + 5000);
    utimesSync(livePath, future, future);
    const changed = buildPayload(root);
    assert.equal(changed.cards.find((entry) => entry.id === "A").noteContent, "beta");

    unlinkSync(livePath);
    const disappeared = buildPayload(root);
    assert.equal(disappeared.cards.find((entry) => entry.id === "A").noteContent, null);
    assert.ok(disappeared.warnings.some((warning) => warning.kind === "missing-note" && warning.detail.includes("A")));

    const checked = await quietly(() => checkPlan(root, { json: true }));
    assert.equal(checked.ok, true);
    assert.ok(checked.warnings.some((warning) => warning.includes("Unreferenced note file: cards/orphan.md")));
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("watcher keeps NEXT.md synchronized with fresh payloads", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-next-"));
  let boardServer = null;
  try {
    makePlan(root, {
      title: "Live next fixture",
      slug: "live-next",
      cards: [{ id: "A", title: "Initial next action", column: "doing", status: "active", estimate: 1 }],
    });
    boardServer = await quietly(() => runBoard({ planDir: root, port: 0, host: "127.0.0.1" }));
    const nextPath = join(root, "NEXT.md");
    const planPath = join(root, "plan.yaml");
    assert.match(readFileSync(nextPath, "utf8"), /Initial next action/);

    await new Promise((resolveWait) => setTimeout(resolveWait, 100));
    const unchangedMtime = statSync(nextPath).mtimeMs;
    writeFileSync(planPath, readFileSync(planPath, "utf8"));
    await new Promise((resolveWait) => setTimeout(resolveWait, 220));
    assert.equal(statSync(nextPath).mtimeMs, unchangedMtime, "an unchanged NEXT.md is not rewritten");

    makePlan(root, {
      title: "Live next fixture",
      slug: "live-next",
      cards: [{ id: "A", title: "Updated next action", column: "doing", status: "active", estimate: 1 }],
    });
    await waitFor(() => readFileSync(nextPath, "utf8").includes("Updated next action"));
    assert.doesNotMatch(readFileSync(nextPath, "utf8"), /Initial next action/);
  } finally {
    if (boardServer) await boardServer.close();
    rmSync(root, { recursive: true, force: true });
  }
});

test("deleting a note never evicts a board whose plan still exists", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-note-delete-"));
  let boardServer = null;
  try {
    makePlan(root, {
      title: "Note deletion fixture",
      slug: "note-delete",
      cards: [{ id: "A", title: "Referenced note", column: "backlog", note: "cards/A.md" }],
    });
    mkdirSync(join(root, "cards"));
    writeFileSync(join(root, "cards", "A.md"), "receipt");
    boardServer = await quietly(() => runBoard({ planDir: root, port: 0, host: "127.0.0.1" }));

    unlinkSync(join(root, "cards", "A.md"));
    const payload = await waitFor(async () => {
      const current = await fetch(boardServer.url + "api/board").then((response) => response.json());
      return current.warnings.some((warning) => warning.kind === "missing-note") ? current : null;
    });
    assert.equal(payload.stale, undefined);

    const state = await fetch(`http://127.0.0.1:${boardServer.port}/api/boards`).then((response) => response.json());
    assert.equal(state.boards.length, 1);
    assert.equal(state.boards[0].boardPath, "/note-delete/");
  } finally {
    if (boardServer) await boardServer.close();
    rmSync(root, { recursive: true, force: true });
  }
});

test("parse errors serve the last good payload with a stale warning", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-stale-"));
  let boardServer = null;
  try {
    makePlan(root, {
      title: "Stale fixture",
      slug: "stale-fixture",
      cards: [{ id: "A", title: "Stable card", column: "backlog", estimate: 1 }],
    });
    boardServer = await quietly(() => runBoard({ planDir: root, port: 0, host: "127.0.0.1" }));
    const endpoint = boardServer.url + "api/board";
    const good = await fetch(endpoint).then((response) => response.json());
    assert.ok(good.columns.length > 0);

    writeFileSync(join(root, "plan.yaml"), "version: 1\n plan:\n");
    const stale = await waitFor(async () => {
      const payload = await fetch(endpoint).then((response) => response.json());
      return payload.error ? payload : null;
    });
    assert.equal(stale.stale, true);
    assert.equal(stale.plan.title, good.plan.title);
    assert.deepEqual(stale.columns, good.columns);
    assert.deepEqual(stale.cards, good.cards);

    const appJs = readFileSync(join(root, ".plandeck-board", "app.js"), "utf8");
    assert.match(appJs, /plan\.yaml broken: .*showing last good state/);
  } finally {
    if (boardServer) await boardServer.close();
    rmSync(root, { recursive: true, force: true });
  }
});

test("archive journals lifecycle entries and removes archived ids from last-state", () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-archive-journal-"));
  try {
    makePlan(root, {
      title: "Archive journal fixture",
      cards: [
        { id: "A", title: "Done", column: "done", status: "done", estimate: 1 },
        { id: "B", title: "Open", column: "backlog", status: "queued", estimate: 1 },
      ],
    });
    logTransitions(root, buildPayload(root).cards);
    archiveDoneCards(root, Date.parse("2026-07-14T10:00:00Z"), { actor: "archive-agent" });
    const lifecycle = readJournal(root).find((entry) => entry.field === "lifecycle");
    assert.deepEqual({ cardId: lifecycle.cardId, from: lifecycle.from, to: lifecycle.to, actor: lifecycle.actor }, {
      cardId: "A", from: "done", to: "archived", actor: "archive-agent",
    });
    assert.deepEqual(Object.keys(readLastState(root).cards), ["B"]);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("a live board journals column transitions observed by its watcher", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-watcher-journal-"));
  let boardServer = null;
  try {
    makePlan(root, {
      title: "Watcher journal fixture",
      slug: "watcher-journal",
      cards: [{ id: "A", title: "Move me", column: "backlog", status: "queued", estimate: 1 }],
    });
    boardServer = await quietly(() => runBoard({ planDir: root, port: 0, host: "127.0.0.1", actor: "watch-agent" }));
    makePlan(root, {
      title: "Watcher journal fixture",
      slug: "watcher-journal",
      cards: [{ id: "A", title: "Move me", column: "doing", status: "active", estimate: 1 }],
    });
    const transition = await waitFor(() => readJournal(root).find((entry) => entry.cardId === "A" && entry.field === "column"));
    assert.equal(transition.from, "ready");
    assert.equal(transition.to, "doing");
    assert.equal(transition.actor, "watch-agent");
    assert.match(readFileSync(join(root, "NEXT.md"), "utf8"), /## Since you left/);
    assert.match(readFileSync(join(root, "NEXT.md"), "utf8"), /A moved ready → doing/);
  } finally {
    if (boardServer) await boardServer.close();
    rmSync(root, { recursive: true, force: true });
  }
});

test("board actor attribution survives CLI registration with an existing hub", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-actor-hub-"));
  const firstDir = join(root, "first");
  const secondDir = join(root, "second");
  let hub = null;
  try {
    makePlan(firstDir, {
      title: "Owner board",
      slug: "owner-board",
      cards: [{ id: "A", title: "Owner card", column: "backlog", status: "queued", estimate: 1 }],
    });
    makePlan(secondDir, {
      title: "Registered board",
      slug: "registered-board",
      cards: [{ id: "B", title: "Registered card", column: "backlog", status: "queued", estimate: 1 }],
    });
    hub = await quietly(() => runBoard({ planDir: firstDir, port: 0, host: "127.0.0.1", actor: "owner-agent" }));
    const registered = await invokeCli([
      "board", secondDir, "--port", String(hub.port), "--host", "127.0.0.1", "--actor", "cli-agent", "--json",
    ]);
    assert.equal(registered.status, 0, registered.stderr);
    assert.equal(JSON.parse(registered.stdout).registered, true);
    assert.equal(readJournal(firstDir).at(-1).actor, "owner-agent");
    assert.equal(readJournal(secondDir).at(-1).actor, "cli-agent");

    makePlan(secondDir, {
      title: "Registered board",
      slug: "registered-board",
      cards: [{ id: "B", title: "Registered card", column: "doing", status: "active", estimate: 1 }],
    });
    const transition = await waitFor(() => readJournal(secondDir).find((entry) => entry.cardId === "B" && entry.field === "column"));
    assert.equal(transition.actor, "cli-agent");
  } finally {
    if (hub) await hub.close();
    rmSync(root, { recursive: true, force: true });
  }
});

test("the per-board journal API filters by since and returns its documented shape", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-journal-api-"));
  let boardServer = null;
  try {
    makePlan(root, {
      title: "Journal API fixture",
      slug: "journal-api",
      cards: [{ id: "A", title: "API card", column: "backlog", status: "queued", estimate: 1 }],
    });
    boardServer = await quietly(() => runBoard({ planDir: root, port: 0, host: "127.0.0.1" }));
    appendJournalEntry(root, { cardId: "A", field: "status", from: "queued", to: "active", actor: "first" });
    await new Promise((resolveWait) => setTimeout(resolveWait, 5));
    const second = appendJournalEntry(root, { cardId: "A", field: "column", from: "ready", to: "doing", actor: "second" });
    const response = await fetch(`${boardServer.url}api/journal?since=${encodeURIComponent(second.ts)}&limit=5`);
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.deepEqual(Object.keys(body), ["entries"]);
    assert.equal(body.entries.length, 1);
    assert.deepEqual(body.entries[0], second);
    const post = await fetch(`${boardServer.url}api/journal`, { method: "POST" });
    assert.equal(post.status, 405);
  } finally {
    if (boardServer) await boardServer.close();
    rmSync(root, { recursive: true, force: true });
  }
});

test("checkPlan includes the doctor recovery hint after a parse failure", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-check-doctor-"));
  try {
    writeFileSync(join(root, "plan.yaml"), "version: 1\n plan:\n");
    const captured = await captureConsole(() => checkPlan(root));
    assert.equal(captured.result.ok, false);
    assert.ok(captured.result.errors.some((message) => message.includes("plandeck doctor")));
    assert.match(captured.error.join("\n"), /Run `plandeck doctor <dir>`/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("the CLI adds the doctor hint only for PlanError failures", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-cli-hint-"));
  try {
    writeFileSync(join(root, "plan.yaml"), "version: 1\n plan:\n");
    const planError = await invokeCli(["next", root]);
    assert.equal(planError.status, 1);
    assert.match(planError.stderr, /Run `plandeck doctor <dir>`/);

    const unrelated = await invokeCli(["board", join(root, "missing"), "--once"]);
    assert.equal(unrelated.status, 1);
    assert.match(unrelated.stderr, /No plan\.yaml/);
    assert.doesNotMatch(unrelated.stderr, /plandeck doctor/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("next --json returns a stable hash and --since suppresses unchanged payloads", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-next-since-"));
  try {
    makePlan(root, {
      title: "Polling fixture",
      cards: [{ id: "A", title: "Poll me", column: "backlog", status: "queued", estimate: 1 }],
    });
    const initial = await invokeCli(["next", root, "--json", "--actor", "poll-agent"]);
    assert.equal(initial.status, 0, initial.stderr);
    const first = JSON.parse(initial.stdout);
    assert.match(first.stateHash, /^[a-f0-9]{12}$/);
    assert.ok(first.next);

    const unchanged = await invokeCli(["next", root, "--json", "--since", first.stateHash]);
    assert.equal(unchanged.status, 0, unchanged.stderr);
    assert.deepEqual(JSON.parse(unchanged.stdout), { unchanged: true, stateHash: first.stateHash });

    makePlan(root, {
      title: "Polling fixture",
      cards: [{ id: "A", title: "Poll me", column: "doing", status: "active", estimate: 1 }],
    });
    const changed = await invokeCli(["next", root, "--json", "--since", first.stateHash]);
    const next = JSON.parse(changed.stdout);
    assert.equal(changed.status, 0, changed.stderr);
    assert.notEqual(next.stateHash, first.stateHash);
    assert.equal(next.unchanged, undefined);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("next --since prints unchanged in human mode", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-next-since-text-"));
  try {
    makePlan(root, {
      title: "Text polling fixture",
      cards: [{ id: "A", title: "Poll me", column: "backlog", status: "queued", estimate: 1 }],
    });
    const stateHash = JSON.parse((await invokeCli(["next", root, "--json"])).stdout).stateHash;
    const result = await invokeCli(["next", root, "--since", stateHash]);
    assert.equal(result.status, 0, result.stderr);
    assert.equal(result.stdout.trim(), "unchanged");
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("journal CLI supports JSON, limit, since, and actor-attributed entries", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-journal-cli-"));
  try {
    makePlan(root, {
      title: "Journal CLI fixture",
      cards: [{ id: "A", title: "Journal me", column: "backlog", status: "queued", estimate: 1 }],
    });
    assert.equal((await invokeCli(["next", root, "--json", "--actor", "first-agent"])).status, 0);
    makePlan(root, {
      title: "Journal CLI fixture",
      cards: [{ id: "A", title: "Journal me", column: "doing", status: "active", estimate: 1 }],
    });
    assert.equal((await invokeCli(["next", root, "--json", "--actor", "second-agent"])).status, 0);

    const limited = await invokeCli(["journal", root, "--json", "--limit", "1"]);
    assert.equal(limited.status, 0, limited.stderr);
    const body = JSON.parse(limited.stdout);
    assert.equal(body.planDir, root);
    assert.equal(body.count, 1);
    assert.equal(body.entries[0].actor, "second-agent");

    const since = await invokeCli(["journal", root, "--json", "--since", body.entries[0].ts]);
    assert.equal(since.status, 0, since.stderr);
    assert.ok(JSON.parse(since.stdout).entries.every((entry) => Date.parse(entry.ts) >= Date.parse(body.entries[0].ts)));

    const invalid = await invokeCli(["journal", root, "--since", "not-a-date"]);
    assert.equal(invalid.status, 1);
    assert.match(invalid.stderr, /ISO timestamp/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("doctor CLI diagnoses and explicitly restores the latest snapshot", async () => {
  const root = mkdtempSync(join(tmpdir(), "plandeck-doctor-cli-"));
  try {
    makePlan(root, {
      title: "Doctor CLI fixture",
      cards: [{ id: "A", title: "Safe card", column: "backlog", status: "queued", estimate: 1 }],
    });
    const observed = await invokeCli(["next", root, "--json"]);
    assert.equal(observed.status, 0, observed.stderr);
    const clean = readFileSync(join(root, "plan.yaml"), "utf8");
    const broken = "version: 1\n plan:\n";
    writeFileSync(join(root, "plan.yaml"), broken);

    const diagnosis = await invokeCli(["doctor", root, "--json"]);
    assert.equal(diagnosis.status, 1);
    const report = JSON.parse(diagnosis.stdout);
    assert.equal(report.ok, false);
    assert.equal(report.snapshotCount, 1);

    const restored = await invokeCli(["doctor", root, "--restore", "latest", "--actor", "doctor-agent", "--json"]);
    assert.equal(restored.status, 0, restored.stderr);
    assert.equal(JSON.parse(restored.stdout).restored, true);
    assert.equal(readFileSync(join(root, "plan.yaml"), "utf8"), clean);
    assert.equal(readFileSync(join(root, "plan.yaml.corrupt"), "utf8"), broken);
    assert.equal(readJournal(root)[0].actor, "doctor-agent");
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});
