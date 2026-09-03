// intelligence.mjs — Plandeck's brain.
//
// Pure, deterministic, zero-I/O functions over a normalized plan object.
// Everything here is testable without a filesystem, a clock, or a network.
// This is the layer that makes Plandeck smarter than a status board:
// dependency-aware Ready detection, critical path, estimate rollups, and the
// single "do this next" pointer an agent reads after /clear.

export const COLUMNS = ["backlog", "ready", "doing", "review", "done"];
export const COLUMN_META = {
  backlog: { title: "Backlog", blurb: "Captured, not yet unblocked" },
  ready: { title: "Ready", blurb: "Every dependency met, pull next" },
  doing: { title: "In Progress", blurb: "The one active card" },
  review: { title: "Review", blurb: "Done, awaiting proof" },
  done: { title: "Done", blurb: "Receipted and verified" },
};

const PRIORITY_RANK = { P0: 0, P1: 1, P2: 2, P3: 3, P4: 4 };

const isDone = (card) => card.status === "done" || card.column === "done";
const isBlocked = (card) => card.status === "blocked" || card.column === "blocked";

/** Points used by progress and critical-path math. Unestimated cards use one point. */
export function points(card) {
  return Number.isFinite(card.estimate) && card.estimate > 0 ? card.estimate : 1;
}

/** Weight used for path length, kept identical to progress units. */
function cpWeight(card) {
  return points(card);
}

/**
 * Kahn topological sort with cycle detection.
 * Returns { order: [id...], cycle: [id...] | null }. On a cycle, `order` holds
 * the resolvable prefix and `cycle` names the cards trapped in the loop.
 */
export function topoOrder(cards, byId = indexById(cards)) {
  const indegree = new Map();
  const dependents = new Map(); // id -> [ids that depend on it]
  for (const card of cards) {
    indegree.set(card.id, 0);
    dependents.set(card.id, []);
  }
  for (const card of cards) {
    for (const dep of card.depends_on || []) {
      if (!byId.has(dep)) continue; // dangling refs handled elsewhere
      indegree.set(card.id, indegree.get(card.id) + 1);
      dependents.get(dep).push(card.id);
    }
  }

  // Deterministic queue: lowest id first.
  const queue = cards
    .filter((c) => indegree.get(c.id) === 0)
    .map((c) => c.id)
    .sort(compareId);
  const order = [];
  while (queue.length) {
    const id = queue.shift();
    order.push(id);
    const next = [];
    for (const dependent of dependents.get(id)) {
      indegree.set(dependent, indegree.get(dependent) - 1);
      if (indegree.get(dependent) === 0) next.push(dependent);
    }
    for (const id2 of next.sort(compareId)) queue.push(id2);
  }

  const cycle = order.length === cards.length ? null : cards.map((c) => c.id).filter((id) => !order.includes(id));
  return { order, cycle };
}

/**
 * Longest estimate-weighted path through the dependency DAG.
 * Returns { chain: [id...], length, onPath: Set<id>, cycle }.
 * The chain is the sequence of cards whose serial completion drives the timeline.
 */
export function criticalPath(cards, byId = indexById(cards)) {
  const { order, cycle } = topoOrder(cards, byId);
  const dist = new Map(); // id -> longest weighted distance ending at id
  const prev = new Map(); // id -> predecessor on the longest path

  for (const id of order) {
    const card = byId.get(id);
    let best = 0;
    let bestPrev = null;
    for (const dep of card.depends_on || []) {
      const depCard = byId.get(dep);
      if (!depCard) continue;
      const viaDep = (dist.get(dep) || 0);
      if (viaDep > best) {
        best = viaDep;
        bestPrev = dep;
      }
    }
    dist.set(id, best + cpWeight(card));
    prev.set(id, bestPrev);
  }

  // Find the endpoint with the greatest distance (ties: lowest id for determinism).
  let endId = null;
  let endLen = -1;
  for (const id of order) {
    const d = dist.get(id);
    if (d > endLen || (d === endLen && compareId(id, endId) < 0)) {
      endLen = d;
      endId = id;
    }
  }

  const chain = [];
  let cursor = endId;
  while (cursor != null) {
    chain.unshift(cursor);
    cursor = prev.get(cursor);
  }

  return { chain, length: endLen < 0 ? 0 : endLen, onPath: new Set(chain), cycle };
}

/**
 * Per-card derived signals. Mutates a shallow copy set of flags onto each card
 * (prefixed `_`) so render + serialization can read them without recomputing.
 */
export function annotate(cards, byId = indexById(cards), satisfiedIds = new Set()) {
  const cp = criticalPath(cards, byId);
  const unblocks = new Map(cards.map((c) => [c.id, 0]));
  for (const card of cards) {
    for (const dep of card.depends_on || []) {
      if (unblocks.has(dep)) unblocks.set(dep, unblocks.get(dep) + 1);
    }
  }

  for (const card of cards) {
    const deps = (card.depends_on || []).map((id) => byId.get(id)).filter(Boolean);
    const missing = (card.depends_on || []).filter((id) => !byId.has(id) && !satisfiedIds.has(id));
    const unmet = deps.filter((d) => !isDone(d));
    card._deps = deps.map((d) => d.id);
    card._missingDeps = missing;
    card._unmetDeps = unmet.map((d) => d.id);
    card._ready = unmet.length === 0 && !isDone(card) && !isBlocked(card);
    card._unblocks = unblocks.get(card.id);
    card._onCriticalPath = cp.onPath.has(card.id);
    card._effectiveColumn = effectiveColumn(card);
  }
  return cp;
}

/**
 * Where a card actually lives on the board. A backlog card whose dependencies
 * are all met is promoted to Ready automatically — the board organizes itself.
 * An explicit `blocked` status wins its own lane regardless of column.
 */
export function effectiveColumn(card) {
  if (isBlocked(card)) return "blocked";
  if (isDone(card)) return "done";
  const col = COLUMNS.includes(card.column) ? card.column : "backlog";
  if (col === "backlog" && card._ready) return "ready";
  return col;
}

/** Progress + estimate rollups. Deterministic; no clock. */
export function rollup(cards, archived = { count: 0, points: 0 }) {
  const archivedCount = Math.max(0, Number(archived.count) || 0);
  const archivedPoints = Math.max(0, Number(archived.points) || 0);
  const totalPoints = cards.reduce((sum, c) => sum + points(c), archivedPoints);
  const donePoints = cards.filter(isDone).reduce((sum, c) => sum + points(c), archivedPoints);
  const counts = { total: cards.length, done: 0, blocked: 0, active: 0, ready: 0 };
  const byColumn = Object.fromEntries(["backlog", "ready", "doing", "review", "done", "blocked"].map((c) => [c, { cards: 0, points: 0 }]));

  for (const card of cards) {
    if (isDone(card)) counts.done += 1;
    if (isBlocked(card)) counts.blocked += 1;
    if (card.status === "active" || card.column === "doing") counts.active += 1;
    if (card._ready) counts.ready += 1;
    const col = card._effectiveColumn || effectiveColumn(card);
    byColumn[col].cards += 1;
    byColumn[col].points += points(card);
  }

  const totalCards = cards.length + archivedCount;
  const doneCards = counts.done + archivedCount;
  const pct = totalPoints > 0 ? Math.round((donePoints / totalPoints) * 100) : (totalCards ? Math.round((doneCards / totalCards) * 100) : 0);
  return {
    totalPoints,
    donePoints,
    remainingPoints: totalPoints - donePoints,
    pct,
    counts,
    byColumn,
    archived: { count: archivedCount, points: archivedPoints },
  };
}

/**
 * The single most important output: what to do NEXT.
 * An agent re-reading the plan after /clear should need only this.
 * Order of preference:
 *   1. an already-active card (finish what's started),
 *   2. a ready card on the critical path (protect the timeline),
 *   3. a ready card by priority, then by how many others it unblocks,
 *   4. nothing ready -> surface the top blocker to clear.
 */
export function nextAction(cards, byId = indexById(cards), archivedCount = 0) {
  const active = cards.find((c) => c.status === "active" || c.column === "doing");
  if (active) {
    return { cardId: active.id, title: active.title, reason: "active", detail: "Resume the card already in progress." };
  }

  const ready = cards.filter((c) => c._ready);
  if (ready.length) {
    const pick = ready.slice().sort(compareReady)[0];
    const why = pick._onCriticalPath
      ? "on the critical path"
      : pick._unblocks > 0
        ? `unblocks ${pick._unblocks} card${pick._unblocks === 1 ? "" : "s"}`
        : `highest priority (${pick.priority || "P?"})`;
    return { cardId: pick.id, title: pick.title, reason: "ready", detail: `Pull "${pick.title}" next — ${why}.` };
  }

  const blocked = cards.filter((c) => !isDone(c) && (isBlocked(c) || (c._unmetDeps && c._unmetDeps.length)));
  if (blocked.length) {
    const pick = blocked.slice().sort(compareReady)[0];
    const on = (pick._unmetDeps && pick._unmetDeps.length) ? ` (waiting on ${pick._unmetDeps.join(", ")})` : "";
    return { cardId: pick.id, title: pick.title, reason: "blocked", detail: `Everything is blocked. Clear "${pick.title}"${on} to open flow.` };
  }

  const remaining = cards.filter((c) => !isDone(c));
  if (!remaining.length) {
    if (!cards.length && archivedCount <= 0) {
      return { cardId: null, title: null, reason: "empty", detail: "No cards yet. Add the first card to plan.yaml." };
    }
    return { cardId: null, title: null, reason: "complete", detail: "Every card is done. Run the completion audit." };
  }
  return { cardId: remaining[0].id, title: remaining[0].title, reason: "unknown", detail: "No card is clearly ready; review the plan." };
}

// --- ordering helpers (all deterministic) ---

function compareReady(a, b) {
  if (a._onCriticalPath !== b._onCriticalPath) return a._onCriticalPath ? -1 : 1;
  const pa = PRIORITY_RANK[a.priority] ?? 9;
  const pb = PRIORITY_RANK[b.priority] ?? 9;
  if (pa !== pb) return pa - pb;
  if (a._unblocks !== b._unblocks) return b._unblocks - a._unblocks;
  return compareId(a.id, b.id);
}

/** Compare card ids deterministically with numeric segments in natural order. */
export function compareId(a, b) {
  return String(a).localeCompare(String(b), "en", { numeric: true });
}

/** Build the id lookup shared by graph calculations. */
export function indexById(cards) {
  return new Map(cards.map((c) => [c.id, c]));
}
