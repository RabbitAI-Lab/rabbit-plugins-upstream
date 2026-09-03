// snapshot.mjs — last-known-good plan snapshots and card-level diff summaries.

import { existsSync, mkdirSync, readFileSync, readdirSync, unlinkSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { join, resolve } from "node:path";
import { normalizePlan, parseYaml } from "./deck.mjs";

const SNAPSHOT_PATTERN = /^plan-(\d{8}T\d{9}Z)\.yaml$/;
const MAX_SNAPSHOTS = 20;
const warnedRoots = new Set();

/** Snapshot a clean plan when its raw content differs from the newest snapshot. */
export function maybeSnapshot(planDir, now = Date.now()) {
  const root = resolve(planDir);
  try {
    const planPath = join(root, "plan.yaml");
    const source = readFileSync(planPath, "utf8");
    normalizePlan(parseYaml(source), root);

    const snapshots = listSnapshots(root);
    if (snapshots.length) {
      const newestSource = readFileSync(snapshots[0].path, "utf8");
      if (contentHash(newestSource) === contentHash(source)) return null;
    }

    const dir = snapshotDir(root);
    mkdirSync(dir, { recursive: true });
    const token = compactIso(now);
    const file = `plan-${token}.yaml`;
    const path = join(dir, file);
    try {
      writeFileSync(path, source, { encoding: "utf8", flag: "wx" });
    } catch (error) {
      if (error.code !== "EEXIST") throw error;
      return null;
    }

    const current = listSnapshots(root);
    for (const stale of current.slice(MAX_SNAPSHOTS)) unlinkSync(stale.path);
    return { file, path, ts: token };
  } catch (error) {
    warnOnce(root, error);
    return null;
  }
}

/** List Windows-safe plan snapshots newest-first. */
export function listSnapshots(planDir) {
  const root = resolve(planDir);
  const dir = snapshotDir(root);
  if (!existsSync(dir)) return [];
  try {
    return readdirSync(dir)
      .flatMap((file) => {
        const match = file.match(SNAPSHOT_PATTERN);
        return match ? [{ file, path: join(dir, file), ts: match[1] }] : [];
      })
      .sort((a, b) => b.file.localeCompare(a.file));
  } catch {
    return [];
  }
}

/** Compare card identity, column, status, and estimate in deterministic id order. */
export function diffCardsSummary(oldCards, newCards) {
  const before = indexCards(oldCards);
  const after = indexCards(newCards);
  const oldIds = [...before.keys()].sort(compareIds);
  const newIds = [...after.keys()].sort(compareIds);
  const added = newIds.filter((id) => !before.has(id));
  const removed = oldIds.filter((id) => !after.has(id));
  const changed = [];

  for (const id of newIds) {
    if (!before.has(id)) continue;
    const fields = [];
    for (const name of ["column", "status", "estimate"]) {
      const from = fieldValue(before.get(id), name);
      const to = fieldValue(after.get(id), name);
      if (from !== to) fields.push({ name, from, to });
    }
    if (fields.length) changed.push({ id, fields });
  }
  return { added, removed, changed };
}

function indexCards(cards) {
  const result = new Map();
  for (const card of Array.isArray(cards) ? cards : []) {
    const id = String(card?.id ?? "").trim();
    if (id) result.set(id, card);
  }
  return result;
}

function fieldValue(card, name) {
  const value = card?.[name];
  return value === undefined ? null : value;
}

function compareIds(a, b) {
  return a.localeCompare(b, undefined, { numeric: true });
}

function compactIso(now) {
  return new Date(now).toISOString().replace(/[-:.]/g, "");
}

function contentHash(source) {
  return createHash("sha1").update(source).digest("hex").slice(0, 10);
}

function snapshotDir(planDir) {
  return join(resolve(planDir), ".plandeck", "snapshots");
}

function warnOnce(planDir, error) {
  const root = resolve(planDir);
  if (warnedRoots.has(root)) return;
  warnedRoots.add(root);
  console.warn(`Could not update Plandeck snapshots in ${root}: ${error.message || error}`);
}
