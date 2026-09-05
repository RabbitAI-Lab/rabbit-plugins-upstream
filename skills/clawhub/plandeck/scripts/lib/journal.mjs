// journal.mjs — durable, append-only history for observed plan transitions.

import { appendFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { join, resolve } from "node:path";
import { atomicWriteFile } from "./deck.mjs";

const FIELD_ORDER = new Map(["plan", "card", "lifecycle", "column", "status", "receipt"].map((field, index) => [field, index]));
const warnedRoots = new Set();

/** Append one timestamped journal entry. Continuity failures never block the caller. */
export function appendJournalEntry(planDir, partialEntry) {
  try {
    return appendEntries(planDir, [partialEntry])[0] || null;
  } catch (error) {
    warnOnce(planDir, error);
    return null;
  }
}

/** Compare live cards with the durable last-state cache and record every transition. */
export function logTransitions(planDir, liveCards, { actor } = {}) {
  try {
    const current = cardsState(liveCards);
    const priorState = readLastState(planDir);
    if (!priorState) {
      appendEntries(planDir, [{
        cardId: null,
        field: "plan",
        from: null,
        to: `loaded (${Object.keys(current).length} cards)`,
        actor,
      }]);
      writeLastStateUnsafe(planDir, { cards: current });
      return;
    }

    const prior = priorState.cards;
    const entries = [];
    for (const id of Object.keys(prior)) {
      if (!(id in current)) entries.push({ cardId: id, field: "card", from: prior[id]?.column ?? null, to: "removed", actor });
    }
    for (const id of Object.keys(current)) {
      if (!(id in prior)) {
        entries.push({ cardId: id, field: "card", from: null, to: "added", actor });
        continue;
      }
      for (const field of ["column", "status", "receipt"]) {
        const from = prior[id]?.[field] ?? null;
        const to = current[id]?.[field] ?? null;
        if (from !== to) entries.push({ cardId: id, field, from, to, actor });
      }
    }

    entries.sort(compareEntries);
    if (entries.length) appendEntries(planDir, entries);
    writeLastStateUnsafe(planDir, { cards: current });
  } catch (error) {
    warnOnce(planDir, error);
  }
}

/** Record cards deliberately moved out of the live plan by the archive command. */
export function logArchived(planDir, archivedCards, { actor } = {}) {
  try {
    const state = readLastState(planDir) || { cards: {} };
    const entries = (Array.isArray(archivedCards) ? archivedCards : [])
      .map((card) => ({
        cardId: String(card?.id ?? "").trim(),
        field: "lifecycle",
        from: card?.column ?? null,
        to: "archived",
        actor,
      }))
      .filter((entry) => entry.cardId)
      .sort(compareEntries);
    if (entries.length) appendEntries(planDir, entries);
    for (const entry of entries) delete state.cards[entry.cardId];
    writeLastStateUnsafe(planDir, state);
  } catch (error) {
    warnOnce(planDir, error);
  }
}

/** Read journal entries newest-first, optionally filtering and limiting them. */
export function readJournal(planDir, { since, limit } = {}) {
  const path = journalPath(planDir);
  if (!existsSync(path)) return [];
  let entries;
  try {
    entries = readFileSync(path, "utf8")
      .split(/\r?\n/)
      .filter(Boolean)
      .flatMap((line) => {
        try {
          const entry = JSON.parse(line);
          return entry && typeof entry === "object" && !Array.isArray(entry) ? [entry] : [];
        } catch {
          return [];
        }
      });
  } catch {
    return [];
  }

  if (since !== undefined && since !== null && since !== "") {
    const threshold = Date.parse(String(since));
    if (Number.isFinite(threshold)) entries = entries.filter((entry) => Date.parse(entry.ts) >= threshold);
  }
  entries.reverse();
  if (limit !== undefined && limit !== null && Number.isFinite(Number(limit))) {
    entries = entries.slice(0, Math.max(0, Math.trunc(Number(limit))));
  }
  return entries;
}

/** Return the newest entries in chronological order for NEXT.md narration. */
export function recentForNext(planDir, n = 5) {
  const count = Math.max(0, Math.trunc(Number(n) || 0));
  return readJournal(planDir, { limit: count }).reverse();
}

/** Render one journal event without exposing raw receipt content. */
export function describeEntry(entry) {
  const cardId = entry?.cardId || "Card";
  let description;
  switch (entry?.field) {
    case "plan":
      description = `Plan ${entry.to || "updated"}`;
      break;
    case "card":
      description = entry.to === "added" ? `${cardId} added` : `${cardId} removed${entry.from ? ` from ${entry.from}` : ""}`;
      break;
    case "lifecycle":
      description = `${cardId} archived`;
      break;
    case "column":
      description = `${cardId} moved ${displayValue(entry.from)} → ${displayValue(entry.to)}`;
      break;
    case "status":
      description = `${cardId} status ${displayValue(entry.from)} → ${displayValue(entry.to)}`;
      break;
    case "receipt":
      description = `${cardId} receipt ${entry.to === null ? "removed" : `updated (${entry.to})`}`;
      break;
    default:
      description = `${cardId} ${entry?.field || "updated"} ${displayValue(entry?.from)} → ${displayValue(entry?.to)}`;
  }
  return `${description} — ${resolveActor(entry?.actor)}, ${formatTimestamp(entry?.ts)}`;
}

/** Resolve and sanitize an actor name using flag, environment, then fallback precedence. */
export function resolveActor(explicit) {
  for (const candidate of [explicit, process.env.PLANDECK_ACTOR, "unknown-agent"]) {
    const actor = sanitizeActor(candidate);
    if (actor) return actor;
  }
  return "unknown-agent";
}

/** Read the durable transition cache, returning null when it is absent or corrupt. */
export function readLastState(planDir) {
  const path = lastStatePath(planDir);
  try {
    const state = JSON.parse(readFileSync(path, "utf8"));
    if (!state || typeof state !== "object" || Array.isArray(state)) return null;
    if (!state.cards || typeof state.cards !== "object" || Array.isArray(state.cards)) return null;
    return { cards: state.cards };
  } catch {
    return null;
  }
}

/** Atomically replace the durable transition cache. */
export function writeLastState(planDir, state) {
  try {
    writeLastStateUnsafe(planDir, state);
    return true;
  } catch (error) {
    warnOnce(planDir, error);
    return false;
  }
}

function appendEntries(planDir, partialEntries) {
  if (!partialEntries.length) return [];
  const dir = continuityDir(planDir);
  mkdirSync(dir, { recursive: true });
  const ts = new Date().toISOString();
  const entries = partialEntries.map((entry) => orderedEntry(ts, entry));
  appendFileSync(join(dir, "journal.ndjson"), `${entries.map((entry) => JSON.stringify(entry)).join("\n")}\n`, "utf8");
  return entries;
}

function orderedEntry(ts, entry) {
  return {
    ts,
    cardId: entry.cardId ?? null,
    field: entry.field,
    from: entry.from ?? null,
    to: entry.to ?? null,
    actor: resolveActor(entry.actor),
  };
}

function cardsState(liveCards) {
  const cards = {};
  for (const card of Array.isArray(liveCards) ? liveCards : []) {
    const id = String(card?.id ?? "").trim();
    if (!id) continue;
    cards[id] = {
      column: card?.column ?? null,
      status: card?.status ?? null,
      receipt: receiptDescriptor(card?.receipt),
    };
  }
  return cards;
}

function receiptDescriptor(receipt) {
  if (receipt === null || receipt === undefined || receipt === "") return null;
  let source;
  try {
    source = typeof receipt === "string" ? receipt : JSON.stringify(receipt);
  } catch {
    source = String(receipt);
  }
  return `${createHash("sha1").update(source).digest("hex").slice(0, 10)}:${source.length}`;
}

function writeLastStateUnsafe(planDir, state) {
  const dir = continuityDir(planDir);
  mkdirSync(dir, { recursive: true });
  atomicWriteFile(join(dir, "last-state.json"), `${JSON.stringify({ cards: state?.cards || {} }, null, 2)}\n`);
}

function compareEntries(a, b) {
  const aId = a.cardId ?? "";
  const bId = b.cardId ?? "";
  const byId = aId.localeCompare(bId);
  if (byId) return byId;
  return (FIELD_ORDER.get(a.field) ?? Number.MAX_SAFE_INTEGER) - (FIELD_ORDER.get(b.field) ?? Number.MAX_SAFE_INTEGER);
}

function sanitizeActor(value) {
  return String(value ?? "")
    .replace(/[\u0000-\u001f\u007f-\u009f]/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 64)
    .trim();
}

function formatTimestamp(value) {
  const stamp = String(value || "");
  return stamp ? `${stamp.slice(0, 16).replace("T", " ")} UTC` : "unknown time";
}

function displayValue(value) {
  return value === null || value === undefined || value === "" ? "none" : String(value);
}

function continuityDir(planDir) {
  return join(resolve(planDir), ".plandeck");
}

function journalPath(planDir) {
  return join(continuityDir(planDir), "journal.ndjson");
}

function lastStatePath(planDir) {
  return join(continuityDir(planDir), "last-state.json");
}

function warnOnce(planDir, error) {
  const root = resolve(planDir);
  if (warnedRoots.has(root)) return;
  warnedRoots.add(root);
  console.warn(`Could not update Plandeck continuity data in ${root}: ${error.message || error}`);
}
