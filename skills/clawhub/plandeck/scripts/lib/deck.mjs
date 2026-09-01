// deck.mjs — load a plan.yaml, normalize its cards, and assemble the board payload.
//
// Zero dependencies. The small YAML-subset reader that backs it lives at the
// bottom of this file.

import { existsSync, readFileSync, readdirSync, renameSync, statSync, unlinkSync, writeFileSync } from "node:fs";
import { basename, dirname, join, resolve } from "node:path";
import { COLUMN_META, COLUMNS, annotate, compareId, nextAction, points, rollup } from "./intelligence.mjs";
import { observeArchive } from "./continuity.mjs";

export class PlanError extends Error {
  constructor(message) {
    super(message);
    this.name = "PlanError";
  }
}

const VALID_STATUS = new Set(["queued", "active", "blocked", "done"]);
const AGING_DAYS = { doing: 2, review: 2, ready: 5, blocked: 1 };
const NOTE_CACHE = new Map();
const DAY_MS = 86400000;
let atomicWriteCounter = 0;

/** Load plan.yaml and normalize it for the deterministic engine. */
export function loadPlan(planDir) {
  const root = resolve(planDir);
  const planPath = join(root, "plan.yaml");
  if (!existsSync(planPath)) throw new PlanError(`Missing plan.yaml: ${planPath}`);
  const doc = parseYaml(readFileSync(planPath, "utf8"));
  return normalizePlan(doc, root);
}

/** Normalize a parsed plan document and validate its card identities. */
export function normalizePlan(doc, planDir = "<memory>") {
  if (!doc || typeof doc !== "object" || Array.isArray(doc)) throw new PlanError("plan.yaml must be a YAML mapping.");
  const cardsRaw = doc.cards || doc.tasks; // also accept a `tasks:` list as an alias for `cards:`
  if (!Array.isArray(cardsRaw)) throw new PlanError("plan.yaml needs a `cards:` list.");

  const meta = doc.plan || doc.goal || {};
  const cards = cardsRaw.map((card, index) => normalizeCard(card, index));
  const ids = new Set();
  for (const card of cards) {
    if (ids.has(card.id)) throw new PlanError(`Duplicate card id: ${card.id}`);
    ids.add(card.id);
  }

  return {
    planDir,
    version: Number(doc.version) || 1,
    title: text(meta.title || "Untitled plan"),
    slug: slugify(meta.slug || basename(planDir) || "plan"),
    kind: text(meta.kind || "open_ended"),
    status: text(meta.status || "active"),
    northStar: text(meta.north_star || meta.oracle || ""),
    tranche: text(meta.tranche || ""),
    velocity: meta.velocity !== null && meta.velocity !== undefined && meta.velocity !== "" && Number.isFinite(Number(meta.velocity))
      ? Number(meta.velocity)
      : null,
    cards,
  };
}

function normalizeCard(card, index) {
  if (!card || typeof card !== "object" || Array.isArray(card)) throw new PlanError(`Card ${index + 1} must be a mapping.`);
  const id = text(card.id);
  if (!id) throw new PlanError(`Card ${index + 1} is missing an id.`);

  const status = text(card.status || "").toLowerCase();
  if (status && !VALID_STATUS.has(status)) throw new PlanError(`Card ${id} has unsupported status "${status}".`);
  let column = text(card.column || "").toLowerCase();
  if (column && column !== "blocked" && !COLUMNS.includes(column)) throw new PlanError(`Card ${id} has unsupported column "${column}".`);
  if (!column) column = status === "done" ? "done" : status === "blocked" ? "blocked" : "backlog";

  return {
    id,
    title: text(card.title || card.objective || id),
    objective: text(card.objective || ""),
    column,
    status: status || (column === "done" ? "done" : column === "doing" ? "active" : "queued"),
    role: text(card.role || card.assignee || "").toLowerCase(),
    estimate: toNumber(card.estimate ?? card.points),
    confidence: toUnit(card.confidence),
    priority: normalizePriority(card.priority),
    risk: text(card.risk || "").toLowerCase() || null,
    depends_on: list(card.depends_on || card.deps),
    verify: list(card.verify),
    next_action: text(card.next_action || ""),
    tags: list(card.tags),
    updated_at: text(card.updated_at || ""),
    archived_at: text(card.archived_at || ""),
    receipt: normalizeReceipt(card.receipt),
    note: text(typeof card.receipt === "object" && card.receipt ? card.receipt.note : "") || text(card.note || ""),
  };
}

function normalizeReceipt(receipt) {
  if (!receipt) return null;
  if (typeof receipt === "string") return { summary: text(receipt) };
  if (typeof receipt !== "object" || Array.isArray(receipt)) return { summary: text(receipt) };
  return {
    result: text(receipt.result || ""),
    summary: text(receipt.summary || receipt.decision || receipt.result || ""),
    changed_files: list(receipt.changed_files),
    commands: normalizeCommands(receipt.commands),
    evidence: list(receipt.evidence),
    note: text(receipt.note || ""),
  };
}

function normalizeCommands(commands) {
  if (!commands) return [];
  const arr = Array.isArray(commands) ? commands : [commands];
  return arr
    .map((c) => (typeof c === "string" ? { cmd: text(c), status: "" } : { cmd: text(c?.cmd || ""), status: text(c?.status || "") }))
    .filter((c) => c.cmd || c.status);
}

/** Assemble the full payload the board renders and the API serves. */
export function buildPayload(planDir, now = Date.now()) {
  const root = resolve(planDir);
  const plan = loadPlan(root);
  const archive = loadArchive(root);
  for (const card of plan.cards) {
    if (archive.ids.has(card.id)) throw new PlanError(`Card id exists in both plan.yaml and archive.yaml: ${card.id}`);
  }
  const cp = annotate(plan.cards, undefined, archive.ids);
  ageCards(plan.cards, now);

  const notes = loadNotes(root);
  for (const card of plan.cards) {
    const key = normalizeNotePath(card.note);
    card.noteContent = key && notes[key] ? notes[key].content : null;
  }

  const roll = rollup(plan.cards, archive.summary);
  const next = nextAction(plan.cards, undefined, archive.summary.count);
  const columns = buildColumns(plan.cards);
  const eta = estimateEta(plan, roll, archive.cards, now);
  const warnings = collectWarnings(plan.cards, cp, archive.cards, notes);

  return {
    generatedAt: new Date(now).toISOString(),
    source: { planDir: root, planPath: join(root, "plan.yaml") },
    plan: {
      title: plan.title,
      slug: plan.slug,
      kind: plan.kind,
      status: plan.status,
      northStar: plan.northStar,
      tranche: plan.tranche,
    },
    rollup: roll,
    criticalPath: { chain: cp.chain, length: cp.length, cycle: cp.cycle || null },
    nextAction: next,
    eta,
    warnings,
    columns,
    cards: plan.cards.map(serializeCard),
  };
}

/** Move every done card into archive.yaml and leave the active plan compact. */
export function archiveDoneCards(planDir, now = Date.now(), { actor } = {}) {
  const root = resolve(planDir);
  const planPath = join(root, "plan.yaml");
  const archivePath = join(root, "archive.yaml");
  if (!existsSync(planPath)) throw new PlanError(`Missing plan.yaml: ${planPath}`);

  const planSource = readFileSync(planPath, "utf8");
  const planDoc = parseYaml(planSource);
  if (!planDoc || typeof planDoc !== "object" || Array.isArray(planDoc)) throw new PlanError("plan.yaml must be a YAML mapping.");
  const cardsKey = Array.isArray(planDoc.cards) ? "cards" : Array.isArray(planDoc.tasks) ? "tasks" : null;
  if (!cardsKey) throw new PlanError("plan.yaml needs a `cards:` list.");
  const normalizedPlan = normalizePlan(planDoc, root);

  const movedIndexes = [];
  const moved = planDoc[cardsKey].filter((card, index) => {
    if (!isDoneRaw(card)) return false;
    movedIndexes.push(index);
    return true;
  });
  const archivedNormalized = movedIndexes.map((index) => normalizedPlan.cards[index]);
  const remaining = planDoc[cardsKey].filter((card) => !isDoneRaw(card));
  if (!moved.length) {
    return { planDir: root, archivePath, archived: 0, archivedIds: [], remaining: remaining.length };
  }

  let archiveSource = null;
  let archiveDoc = { version: Number(planDoc.version) || 1, archived: [] };
  let existingArchive = { cards: [], ids: new Set() };
  if (existsSync(archivePath)) {
    archiveSource = readFileSync(archivePath, "utf8");
    archiveDoc = parseYaml(archiveSource);
    if (!archiveDoc || typeof archiveDoc !== "object" || Array.isArray(archiveDoc)) throw new PlanError("archive.yaml must be a YAML mapping.");
    if (!Array.isArray(archiveDoc.archived)) throw new PlanError("archive.yaml needs an `archived:` list.");
    existingArchive = normalizeArchiveDocument(archiveDoc);
  }

  const archivedAt = new Date(now).toISOString();
  const archivedCards = moved.map((card) => ({ ...card, archived_at: archivedAt }));
  for (const card of archivedCards) {
    const id = text(card.id);
    if (existingArchive.ids.has(id)) throw new PlanError(`Card id already exists in archive.yaml: ${id}`);
  }

  const nextPlanSource = removeYamlSequenceItems(planSource, cardsKey, movedIndexes, planDoc[cardsKey].length);
  const nextArchiveSource = archiveSource === null
    ? stringifyYaml({ ...archiveDoc, archived: archivedCards })
    : appendYamlSequenceItems(archiveSource, "archived", archivedCards);

  observeArchive(root, archivedNormalized, { actor });
  atomicWriteFile(archivePath, nextArchiveSource);
  atomicWriteFile(planPath, nextPlanSource);
  return {
    planDir: root,
    archivePath,
    archived: archivedCards.length,
    archivedIds: archivedCards.map((card) => text(card.id)),
    remaining: remaining.length,
  };
}

function removeYamlSequenceItems(source, key, indexes, expectedCount) {
  const layout = locateYamlSequence(source, key);
  if (layout.itemLines.length !== expectedCount) {
    throw new PlanError(`Could not safely locate every ${key} entry in plan.yaml.`);
  }

  const removed = new Set();
  for (const index of indexes) {
    const range = layout.ranges[index];
    if (!range) throw new PlanError(`Could not safely locate ${key} entry ${index + 1} in plan.yaml.`);
    for (let line = range.start; line < range.end; line += 1) removed.add(line);
  }

  const removeAll = indexes.length === expectedCount;
  return layout.lines.map((line, index) => {
    if (removed.has(index)) return "";
    if (removeAll && index === layout.keyIndex) return emptySequenceRecord(line);
    return line.raw;
  }).join("");
}

function appendYamlSequenceItems(source, key, items) {
  if (!items.length) return source;
  const layout = locateYamlSequence(source, key);
  if (layout.inline && layout.inline !== "[]") throw new PlanError(`archive.yaml needs an \`${key}:\` list.`);

  if (layout.inline === "[]") {
    layout.lines[layout.keyIndex].raw = removeInlineEmptySequence(layout.lines[layout.keyIndex]);
  }

  const eol = source.includes("\r\n") ? "\r\n" : "\n";
  const insertIndex = layout.itemLines.length ? layout.contentEnd : layout.keyIndex + 1;
  let before = layout.lines.slice(0, insertIndex).map((line) => line.raw).join("");
  const after = layout.lines.slice(insertIndex).map((line) => line.raw).join("");
  if (before && !before.endsWith("\n")) before += eol;
  const block = `${writeSequence(items, layout.sequenceIndent).replaceAll("\n", eol)}${eol}`;
  return `${before}${block}${after}`;
}

function locateYamlSequence(source, key) {
  const lines = splitSourceLines(source);
  const info = lines.map(inspectSourceLine);
  const significant = info.filter((line) => !line.trivia);
  const rootIndent = significant.length ? Math.min(...significant.map((line) => line.indent)) : 0;
  const keyIndex = info.findIndex((line) => {
    if (line.trivia || line.indent !== rootIndent) return false;
    const colon = line.trimmed.indexOf(":");
    return colon > 0 && line.trimmed.slice(0, colon).trim() === key;
  });
  if (keyIndex < 0) throw new PlanError(`Could not safely locate \`${key}:\` in YAML source.`);

  const keyLine = info[keyIndex];
  const colon = keyLine.trimmed.indexOf(":");
  const inline = keyLine.trimmed.slice(colon + 1).trim();
  const empty = {
    lines,
    keyIndex,
    inline,
    sequenceIndent: keyLine.indent + 2,
    itemLines: [],
    ranges: [],
    contentEnd: keyIndex + 1,
  };
  if (inline) return empty;

  let first = keyIndex + 1;
  while (first < info.length && info[first].trivia) first += 1;
  if (first >= info.length || info[first].indent <= keyLine.indent) return empty;

  const sequenceIndent = info[first].indent;
  const itemLines = [];
  let sequenceEnd = lines.length;
  for (let index = first; index < info.length; index += 1) {
    const line = info[index];
    if (line.trivia) continue;
    if (line.indent < sequenceIndent || (line.indent === sequenceIndent && !line.trimmed.startsWith("- "))) {
      sequenceEnd = index;
      break;
    }
    if (line.indent === sequenceIndent && line.trimmed.startsWith("- ")) itemLines.push(index);
  }

  if (!itemLines.length) return { ...empty, sequenceIndent };
  const starts = itemLines.map((lineIndex, itemIndex) => {
    let start = lineIndex;
    const floor = itemIndex === 0 ? keyIndex + 1 : itemLines[itemIndex - 1] + 1;
    while (start > floor && isSequenceTrivia(lines[start - 1], sequenceIndent)) start -= 1;
    return start;
  });
  let contentEnd = sequenceEnd;
  while (contentEnd > itemLines.at(-1) + 1 && isSequenceTrivia(lines[contentEnd - 1], sequenceIndent)) contentEnd -= 1;
  const ranges = starts.map((start, index) => ({ start, end: starts[index + 1] ?? contentEnd }));
  return { lines, keyIndex, inline, sequenceIndent, itemLines, ranges, contentEnd };
}

function splitSourceLines(source) {
  const lines = [];
  let start = 0;
  while (start < source.length) {
    const newline = source.indexOf("\n", start);
    const end = newline < 0 ? source.length : newline + 1;
    const raw = source.slice(start, end);
    const eol = raw.endsWith("\r\n") ? "\r\n" : raw.endsWith("\n") ? "\n" : "";
    lines.push({ raw, text: eol ? raw.slice(0, -eol.length) : raw, eol });
    start = end;
  }
  return lines;
}

function inspectSourceLine(line) {
  const code = stripHash(line.text).replace(/\s+$/, "");
  const trimmed = code.trimStart();
  return { trivia: !trimmed, indent: code.length - trimmed.length, trimmed };
}

function isSequenceTrivia(line, sequenceIndent) {
  if (!line.text.trim()) return true;
  if (!line.text.trimStart().startsWith("#")) return false;
  return line.text.length - line.text.trimStart().length <= sequenceIndent;
}

function emptySequenceRecord(line) {
  const code = stripHash(line.text);
  const colon = code.indexOf(":");
  if (colon < 0) throw new PlanError("Could not preserve the empty card list.");
  return `${code.slice(0, colon + 1)} []${code.slice(colon + 1)}${line.text.slice(code.length)}${line.eol}`;
}

function removeInlineEmptySequence(line) {
  const code = stripHash(line.text);
  const colon = code.indexOf(":");
  const token = code.indexOf("[]", colon + 1);
  if (token < 0) throw new PlanError("Could not append to the archived card list.");
  const text = `${line.text.slice(0, token)}${line.text.slice(token + 2)}`;
  return `${text}${line.eol}`;
}

export function atomicWriteFile(path, content) {
  atomicWriteCounter += 1;
  const tempPath = join(dirname(path), `.${basename(path)}.${process.pid}.${Date.now()}.${atomicWriteCounter}.tmp`);
  const options = { encoding: "utf8", flag: "wx" };
  if (existsSync(path)) options.mode = statSync(path).mode;
  try {
    writeFileSync(tempPath, content, options);
    renameSync(tempPath, path);
  } catch (error) {
    try {
      unlinkSync(tempPath);
    } catch {
      // The rename may have completed, or the temporary file was never created.
    }
    throw error;
  }
}

/** Serialize the supported YAML subset while preserving parsed mapping order. */
export function stringifyYaml(value) {
  if (!isMapping(value)) throw new PlanError("YAML document must be a mapping.");
  return `${writeMapping(value, 0)}\n`;
}

function loadArchive(planDir) {
  const archivePath = join(planDir, "archive.yaml");
  if (!existsSync(archivePath)) return { cards: [], ids: new Set(), summary: { count: 0, points: 0 } };

  const doc = parseYaml(readFileSync(archivePath, "utf8"));
  const { cards, ids } = normalizeArchiveDocument(doc);
  return {
    cards,
    ids,
    summary: {
      count: cards.length,
      points: cards.reduce((sum, card) => sum + points(card), 0),
    },
  };
}

function normalizeArchiveDocument(doc) {
  if (!doc || typeof doc !== "object" || Array.isArray(doc)) throw new PlanError("archive.yaml must be a YAML mapping.");
  const raw = doc.archived ?? [];
  if (!Array.isArray(raw)) throw new PlanError("archive.yaml needs an `archived:` list.");

  const cards = raw.map((card, index) => normalizeCard(card, index));
  const ids = new Set();
  for (const card of cards) {
    if (ids.has(card.id)) throw new PlanError(`Duplicate archived card id: ${card.id}`);
    ids.add(card.id);
  }
  return { cards, ids };
}

function isDoneRaw(card) {
  if (!card || typeof card !== "object" || Array.isArray(card)) return false;
  return text(card.status).toLowerCase() === "done" || text(card.column).toLowerCase() === "done";
}

function buildColumns(cards) {
  const laneIds = [...COLUMNS.slice(0, 3), "blocked", ...COLUMNS.slice(3)]; // backlog, ready, doing, blocked, review, done
  const seen = [];
  for (const id of laneIds) if (!seen.includes(id)) seen.push(id);

  const grouped = new Map(seen.map((id) => [id, []]));
  for (const card of cards) {
    const col = grouped.has(card._effectiveColumn) ? card._effectiveColumn : "backlog";
    grouped.get(col).push(card);
  }
  for (const arr of grouped.values()) arr.sort(cardSort);

  return seen.map((id) => {
    const meta = id === "blocked" ? { title: "Blocked", blurb: "Waiting on a dependency or a decision" } : COLUMN_META[id];
    const list = grouped.get(id);
    return {
      id,
      title: meta.title,
      blurb: meta.blurb,
      count: list.length,
      points: list.reduce((sum, c) => sum + points(c), 0),
      cards: list.map(serializeCard),
    };
  });
}

function cardSort(a, b) {
  // active first, then critical-path, then higher priority, then id
  const rank = (c) => (c.status === "active" || c.column === "doing" ? 0 : 1);
  if (rank(a) !== rank(b)) return rank(a) - rank(b);
  if (a._onCriticalPath !== b._onCriticalPath) return a._onCriticalPath ? -1 : 1;
  const pr = (c) => ({ P0: 0, P1: 1, P2: 2, P3: 3, P4: 4 })[c.priority] ?? 9;
  if (pr(a) !== pr(b)) return pr(a) - pr(b);
  return compareId(a.id, b.id);
}

function serializeCard(card) {
  return {
    id: card.id,
    title: card.title,
    objective: card.objective,
    column: card._effectiveColumn,
    declaredColumn: card.column,
    status: card.status,
    role: card.role,
    estimate: card.estimate,
    confidence: card.confidence,
    priority: card.priority,
    risk: card.risk,
    dependsOn: card.depends_on,
    unmetDeps: card._unmetDeps,
    missingDeps: card._missingDeps,
    unblocks: card._unblocks,
    onCriticalPath: card._onCriticalPath,
    ready: card._ready,
    ageDays: card._ageDays ?? null,
    aging: card._aging || false,
    verify: card.verify,
    nextAction: card.next_action,
    tags: card.tags,
    receipt: card.receipt,
    note: card.note || null,
    noteContent: card.noteContent || null,
  };
}

function ageCards(cards, now) {
  for (const card of cards) {
    const ts = Date.parse(card.updated_at || "");
    if (Number.isNaN(ts)) {
      card._ageDays = null;
      card._aging = false;
      continue;
    }
    const days = Math.max(0, Math.round(((now - ts) / 86400000) * 10) / 10);
    card._ageDays = days;
    const limit = AGING_DAYS[card._effectiveColumn];
    card._aging = Boolean(limit && days > limit && card._effectiveColumn !== "done");
  }
}

function estimateEta(plan, roll, archivedCards, now) {
  const configured = plan.velocity && plan.velocity > 0 ? plan.velocity : null;
  const observed = configured ? null : observedVelocity(plan.cards, archivedCards);
  const velocity = configured || observed;
  const basis = configured ? "configured" : observed ? "observed" : null;
  if (!velocity || velocity <= 0 || roll.remainingPoints <= 0) {
    return { velocity: velocity || null, basis, remainingPoints: roll.remainingPoints, days: null, date: null };
  }
  const days = Math.ceil(roll.remainingPoints / velocity);
  const date = new Date(now + days * DAY_MS).toISOString().slice(0, 10);
  return { velocity, basis, remainingPoints: roll.remainingPoints, days, date };
}

function observedVelocity(cards, archivedCards) {
  const samples = [];
  for (const card of cards) {
    if (!isDoneRaw(card)) continue;
    addVelocitySample(samples, card, card.updated_at);
  }
  for (const card of archivedCards) addVelocitySample(samples, card, card.archived_at || card.updated_at);
  if (samples.length < 3) return null;

  const timestamps = samples.map((sample) => sample.timestamp);
  const spanDays = (Math.max(...timestamps) - Math.min(...timestamps)) / DAY_MS;
  if (spanDays < 1) return null;
  const completedPoints = samples.reduce((sum, sample) => sum + sample.points, 0);
  return Number((completedPoints / spanDays).toFixed(2));
}

function addVelocitySample(samples, card, value) {
  const timestamp = Date.parse(value || "");
  if (!Number.isNaN(timestamp)) samples.push({ timestamp, points: points(card) });
}

function collectWarnings(cards, cp, archivedCards = [], notes = {}) {
  const warnings = [];
  if (cp.cycle && cp.cycle.length) warnings.push({ kind: "cycle", detail: `Dependency cycle: ${cp.cycle.join(" -> ")}` });
  const active = cards.filter((c) => c.status === "active" || c.column === "doing");
  if (active.length > 1) warnings.push({ kind: "multi-active", detail: `More than one active card: ${active.map((c) => c.id).join(", ")}` });
  for (const card of cards) {
    if (card._missingDeps && card._missingDeps.length) {
      warnings.push({ kind: "dangling-dep", detail: `${card.id} depends on unknown card(s): ${card._missingDeps.join(", ")}` });
    }
  }
  const aging = cards.filter((c) => c._aging);
  if (aging.length) warnings.push({ kind: "aging", detail: `Aging cards: ${aging.map((c) => `${c.id} (${c._ageDays}d)`).join(", ")}` });
  collectNoteWarnings(warnings, cards, archivedCards, notes);
  return warnings;
}

// --- notes (long receipts) ---
function loadNotes(planDir) {
  const dir = join(planDir, "cards");
  if (!existsSync(dir)) {
    pruneNoteCache(dir, new Set());
    return {};
  }

  let entries;
  try {
    entries = readdirSync(dir, { withFileTypes: true });
  } catch (error) {
    if (error?.code !== "ENOENT") throw error;
    pruneNoteCache(dir, new Set());
    return {};
  }

  const notes = {};
  const seen = new Set();
  for (const entry of entries.sort((a, b) => a.name.localeCompare(b.name))) {
    if (!entry.isFile() || !entry.name.endsWith(".md")) continue;
    const abs = join(dir, entry.name);
    let stat;
    try {
      stat = statSync(abs);
      if (!stat.isFile()) continue;
    } catch (error) {
      NOTE_CACHE.delete(abs);
      if (error?.code === "ENOENT") continue;
      throw error;
    }

    let cached = NOTE_CACHE.get(abs);
    if (!cached || cached.mtimeMs !== stat.mtimeMs) {
      try {
        cached = { dir, content: readFileSync(abs, "utf8"), mtimeMs: stat.mtimeMs };
        NOTE_CACHE.set(abs, cached);
      } catch (error) {
        NOTE_CACHE.delete(abs);
        if (error?.code === "ENOENT") continue;
        throw error;
      }
    }
    seen.add(abs);
    notes[`cards/${entry.name}`] = { content: cached.content, mtimeMs: cached.mtimeMs };
  }
  pruneNoteCache(dir, seen);
  return notes;
}

function pruneNoteCache(dir, seen) {
  for (const [path, cached] of NOTE_CACHE) {
    if (cached.dir === dir && !seen.has(path)) NOTE_CACHE.delete(path);
  }
}

function collectNoteWarnings(warnings, cards, archivedCards, notes) {
  const referenced = new Set();
  for (const card of [...cards, ...archivedCards]) {
    const note = normalizeNotePath(card.note);
    if (!note) continue;
    referenced.add(note);
    if (!Object.hasOwn(notes, note)) {
      warnings.push({ kind: "missing-note", detail: `${card.id} references missing note file: ${note}` });
    }
  }
  for (const note of Object.keys(notes).sort()) {
    if (!referenced.has(note)) warnings.push({ kind: "orphan-note", detail: `Unreferenced note file: ${note}` });
  }
}

function normalizeNotePath(value) {
  return text(value).replaceAll("\\", "/").replace(/^(?:\.\/)+/, "").replace(/^\/+/, "");
}

// --- small helpers ---
function text(v) { return String(v ?? "").trim(); }
function list(v) {
  if (!v) return [];
  if (Array.isArray(v)) return v.map(text).filter(Boolean);
  return [text(v)].filter(Boolean);
}
function toNumber(v) { const n = Number(v); return Number.isFinite(n) ? n : null; }
function toUnit(v) { const n = Number(v); return Number.isFinite(n) ? Math.max(0, Math.min(1, n)) : null; }
function normalizePriority(v) {
  const p = text(v).toUpperCase();
  return /^P[0-4]$/.test(p) ? p : null;
}
function slugify(v) {
  return String(v || "").trim().toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "plan";
}

// A small reader for the YAML subset plan.yaml uses: nested maps, block and
// inline sequences, inline [a, b] arrays, quoted and bare scalars, and #
// comments. Deliberately not a general YAML engine. It reads lines once into a
// flat list, then walks them with a shared cursor, recursing whenever the next
// line is indented deeper than the block being read.
/** Parse the YAML subset used by plan.yaml and archive.yaml. */
export function parseYaml(source) {
  const lines = [];
  source.replace(/\r\n/g, "\n").split("\n").forEach((raw, n) => {
    const body = stripHash(raw).replace(/\s+$/, "");
    if (!body.trim()) return;
    const indent = body.length - body.trimStart().length;
    if (indent % 2) throw new PlanError(`Unsupported odd indentation at line ${n + 1}.`);
    lines.push({ indent, text: body.trimStart(), n: n + 1 });
  });
  if (!lines.length) throw new PlanError("plan.yaml is empty.");
  const cursor = { at: 0 };
  const value = readNode(lines, cursor, lines[0].indent);
  if (cursor.at < lines.length) throw new PlanError(`Could not parse plan.yaml at line ${lines[cursor.at].n}.`);
  return value;
}

// A block at `indent` is a sequence when its first line starts with "- ", else a mapping.
function readNode(lines, cursor, indent) {
  if (cursor.at >= lines.length || lines[cursor.at].indent < indent) return null;
  return lines[cursor.at].text.startsWith("- ")
    ? readSequence(lines, cursor, indent)
    : readMapping(lines, cursor, indent);
}

function readMapping(lines, cursor, indent) {
  const map = {};
  while (cursor.at < lines.length) {
    const line = lines[cursor.at];
    if (line.indent !== indent || line.text.startsWith("- ")) break;
    const [key, inline] = splitPair(line.text, line.n);
    cursor.at += 1;
    if (inline !== "") map[key] = readScalar(inline);
    else map[key] = deeperThan(lines, cursor, indent) ? readNode(lines, cursor, lines[cursor.at].indent) : {};
  }
  return map;
}

function readSequence(lines, cursor, indent) {
  const list = [];
  while (cursor.at < lines.length) {
    const line = lines[cursor.at];
    if (line.indent !== indent || !line.text.startsWith("- ")) break;
    const head = line.text.slice(2).trim();
    cursor.at += 1;
    if (head === "") {
      list.push(deeperThan(lines, cursor, indent) ? readNode(lines, cursor, lines[cursor.at].indent) : null);
      continue;
    }
    if (/^[\w.-]+:(\s|$)/.test(head)) {
      // "- key: value" opens a mapping whose remaining keys may sit on deeper lines.
      const item = {};
      const [key, inline] = splitPair(head, line.n);
      item[key] = inline === "" ? {} : readScalar(inline);
      if (deeperThan(lines, cursor, indent)) {
        const rest = readNode(lines, cursor, lines[cursor.at].indent);
        if (rest && typeof rest === "object" && !Array.isArray(rest)) Object.assign(item, rest);
      }
      list.push(item);
    } else {
      list.push(readScalar(head));
    }
  }
  return list;
}

function deeperThan(lines, cursor, indent) {
  return cursor.at < lines.length && lines[cursor.at].indent > indent;
}

function splitPair(text, n) {
  const at = text.indexOf(":");
  if (at <= 0) throw new PlanError(`Expected key: value at line ${n}.`);
  return [text.slice(0, at).trim(), text.slice(at + 1).trim()];
}

function readScalar(token) {
  if (token === "[]") return [];
  if (token === "{}") return {};
  if (token === "null" || token === "~") return null;
  if (token === "true") return true;
  if (token === "false") return false;
  if (/^-?\d+(\.\d+)?$/.test(token)) return Number(token);
  if (token[0] === "[" && token[token.length - 1] === "]") {
    const inner = token.slice(1, -1).trim();
    return inner ? splitOutsideQuotes(inner, ",").map(readScalar) : [];
  }
  const quote = token[0];
  if ((quote === '"' || quote === "'") && token[token.length - 1] === quote) return unwrap(token, quote);
  return token;
}

function unwrap(token, quote) {
  const inner = token.slice(1, -1);
  if (quote === "'") return inner.replace(/''/g, "'");
  try {
    return JSON.parse(token);
  } catch {
    return inner.replace(/\\"/g, '"').replace(/\\n/g, "\n").replace(/\\\\/g, "\\");
  }
}

// Walk once, flip quote state on unescaped quotes, cut only on unquoted delimiters.
function splitOutsideQuotes(text, delim) {
  const parts = [];
  let quote = null;
  let start = 0;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if ((ch === '"' || ch === "'") && text[i - 1] !== "\\") quote = quote === ch ? null : quote || ch;
    else if (ch === delim && !quote) { parts.push(text.slice(start, i).trim()); start = i + 1; }
  }
  parts.push(text.slice(start).trim());
  return parts;
}

function writeMapping(map, indent) {
  return Object.entries(map).map(([key, value]) => writePair(key, value, indent)).join("\n");
}

function writePair(key, value, indent) {
  const head = `${" ".repeat(indent)}${key}:`;
  if (Array.isArray(value)) {
    if (!value.length) return `${head} []`;
    if (value.every(isScalar)) return `${head} [${value.map(writeScalar).join(", ")}]`;
    return `${head}\n${writeSequence(value, indent + 2)}`;
  }
  if (isMapping(value)) {
    if (!Object.keys(value).length) return `${head} {}`;
    return `${head}\n${writeMapping(value, indent + 2)}`;
  }
  return `${head} ${writeScalar(value)}`;
}

function writeSequence(values, indent) {
  return values.map((value) => {
    const pad = " ".repeat(indent);
    if (isScalar(value)) return `${pad}- ${writeScalar(value)}`;
    if (Array.isArray(value)) {
      if (value.every(isScalar)) return `${pad}- [${value.map(writeScalar).join(", ")}]`;
      throw new PlanError("Nested YAML sequences are not supported.");
    }
    const entries = Object.entries(value);
    if (!entries.length) return `${pad}- {}`;
    const [[firstKey, firstValue], ...rest] = entries;
    const lines = [writeSequenceHead(firstKey, firstValue, indent)];
    for (const [key, item] of rest) lines.push(writePair(key, item, indent + 2));
    return lines.join("\n");
  }).join("\n");
}

function writeSequenceHead(key, value, indent) {
  const head = `${" ".repeat(indent)}- ${key}:`;
  if (Array.isArray(value)) {
    if (!value.length) return `${head} []`;
    if (value.every(isScalar)) return `${head} [${value.map(writeScalar).join(", ")}]`;
    return `${head}\n${writeSequence(value, indent + 4)}`;
  }
  if (isMapping(value)) {
    if (!Object.keys(value).length) return `${head} {}`;
    return `${head}\n${writeMapping(value, indent + 4)}`;
  }
  return `${head} ${writeScalar(value)}`;
}

function writeScalar(value) {
  if (value === null || value === undefined) return "null";
  if (typeof value === "boolean") return value ? "true" : "false";
  if (typeof value === "number") return Number.isFinite(value) ? String(value) : "null";
  const valueText = String(value);
  const reserved = new Set(["null", "true", "false", "~", "[]", "{}"]);
  if (/^[A-Za-z_][A-Za-z0-9_./-]*$/.test(valueText) && !reserved.has(valueText.toLowerCase())) return valueText;
  return JSON.stringify(valueText);
}

function isMapping(value) {
  return Boolean(value && typeof value === "object" && !Array.isArray(value));
}

function isScalar(value) {
  return !value || typeof value !== "object";
}

// Strip a trailing # comment that is not inside quotes.
function stripHash(line) {
  let quote = null;
  for (let i = 0; i < line.length; i += 1) {
    const ch = line[i];
    if ((ch === '"' || ch === "'") && line[i - 1] !== "\\") quote = quote === ch ? null : quote || ch;
    else if (ch === "#" && !quote && (i === 0 || /\s/.test(line[i - 1]))) return line.slice(0, i);
  }
  return line;
}
