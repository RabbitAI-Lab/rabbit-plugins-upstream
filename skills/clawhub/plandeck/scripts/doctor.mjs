// doctor.mjs — diagnose plan corruption and perform explicit snapshot restores.

import { existsSync, readFileSync } from "node:fs";
import { basename, join, resolve } from "node:path";
import { PlanError, atomicWriteFile, normalizePlan, parseYaml } from "./lib/deck.mjs";
import { appendJournalEntry, resolveActor } from "./lib/journal.mjs";
import { diffCardsSummary, listSnapshots } from "./lib/snapshot.mjs";

/** Diagnose a plan or explicitly restore one of its last-known-good snapshots. */
export function runDoctor(planDir, { restore, json = false, actor } = {}) {
  const root = resolve(planDir);
  const snapshots = listSnapshots(root);

  if (restore) {
    const result = restorePlan(root, snapshots, restore, actor);
    printResult(result, json);
    return result;
  }

  try {
    const current = readPlan(join(root, "plan.yaml"), root);
    const newest = snapshots[0] || null;
    const diff = newest ? diffCardsSummary(readPlan(newest.path, root).cards, current.cards) : null;
    const result = {
      ok: true,
      healthy: true,
      restored: false,
      planDir: root,
      snapshotCount: snapshots.length,
      newestSnapshot: newest ? publicSnapshot(newest) : null,
      diff,
    };
    printResult(result, json);
    return result;
  } catch (error) {
    const result = {
      ok: false,
      healthy: false,
      restored: false,
      planDir: root,
      error: error.message || String(error),
      snapshotCount: snapshots.length,
      snapshots: annotateSnapshots(snapshots, root),
    };
    printResult(result, json);
    return result;
  }
}

function restorePlan(root, snapshots, restore, actor) {
  const selection = String(restore);
  const target = selection === "latest" ? snapshots[0] : snapshots.find((snapshot) => snapshot.ts === selection);
  if (!target) {
    return {
      ok: false,
      healthy: false,
      restored: false,
      planDir: root,
      error: `Snapshot not found: ${selection}`,
      snapshotCount: snapshots.length,
      snapshots: snapshots.map(publicSnapshot),
    };
  }

  const planPath = join(root, "plan.yaml");
  const corruptPath = join(root, "plan.yaml.corrupt");
  const currentSource = existsSync(planPath) ? readFileSync(planPath, "utf8") : "";
  const snapshotSource = readFileSync(target.path, "utf8");
  atomicWriteFile(corruptPath, currentSource);
  atomicWriteFile(planPath, snapshotSource);
  appendJournalEntry(root, {
    cardId: null,
    field: "plan",
    from: "corrupt",
    to: `restored (${target.file})`,
    actor: resolveActor(actor),
  });

  return {
    ok: true,
    healthy: true,
    restored: true,
    planDir: root,
    planPath,
    corruptPath,
    snapshotCount: snapshots.length,
    snapshot: publicSnapshot(target),
  };
}

function annotateSnapshots(snapshots, root) {
  const cards = new Map();
  for (const snapshot of snapshots) {
    try {
      cards.set(snapshot.file, readPlan(snapshot.path, root).cards);
    } catch {
      cards.set(snapshot.file, null);
    }
  }
  return snapshots.map((snapshot, index) => {
    const predecessor = snapshots[index + 1] || null;
    const currentCards = cards.get(snapshot.file);
    const previousCards = predecessor ? cards.get(predecessor.file) : null;
    const diff = currentCards && previousCards ? diffCardsSummary(previousCards, currentCards) : null;
    return {
      ...publicSnapshot(snapshot),
      diff,
      summary: predecessor ? (diff ? describeDiff(diff) : "snapshot could not be compared") : "baseline snapshot",
    };
  });
}

function readPlan(path, root) {
  if (!existsSync(path)) throw new PlanError(`Missing plan.yaml: ${path}`);
  const source = readFileSync(path, "utf8");
  return { source, cards: normalizePlan(parseYaml(source), root).cards };
}

function publicSnapshot(snapshot) {
  return { file: snapshot.file, ts: snapshot.ts };
}

function describeDiff(diff) {
  const parts = [];
  if (diff.added.length) parts.push(`added ${diff.added.join(", ")}`);
  if (diff.removed.length) parts.push(`removed ${diff.removed.join(", ")}`);
  if (diff.changed.length) {
    parts.push(`changed ${diff.changed.map((card) => `${card.id} (${card.fields.map((field) => field.name).join(", ")})`).join(", ")}`);
  }
  return parts.length ? parts.join("; ") : "no card changes";
}

function printResult(result, json) {
  if (json) {
    console.log(JSON.stringify(result, null, 2));
    return;
  }
  console.log(`Plandeck doctor · ${basename(result.planDir)}`);
  if (result.restored) {
    console.log(`✓ Restored ${result.snapshot.file}.`);
    console.log(`Saved the previous plan as ${result.corruptPath}.`);
    return;
  }
  if (!result.ok) {
    console.error(result.error);
    if (result.snapshots?.length) {
      console.log(`Snapshots (${result.snapshots.length}, newest first):`);
      for (const snapshot of result.snapshots) console.log(`  ${snapshot.file}: ${snapshot.summary || "available"}`);
    } else {
      console.log("Snapshots: none");
    }
    return;
  }
  console.log("✓ plan.yaml is healthy.");
  console.log(`Snapshots: ${result.snapshotCount}`);
  if (result.newestSnapshot) console.log(`Newest: ${result.newestSnapshot.file} (${describeDiff(result.diff)})`);
}
