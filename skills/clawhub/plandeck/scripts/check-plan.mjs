// check-plan.mjs — Plandeck's completion gate + validator.
//
// planning-with-files taught: don't let an agent declare done from vibes.
// This computes the gate from the plan itself: structural errors fail hard
// (exit 1), an unfinished plan reports the next action, and "complete" is only
// granted when every card is done and no structural warning remains.

import { buildPayload } from "./lib/deck.mjs";

const HARD = new Set(["cycle", "dangling-dep"]);
const DOCTOR_HINT = "Run `plandeck doctor <dir>` to see recovery options.";

/** Validate a plan and report whether every live or archived card is complete. */
export function checkPlan(planDir, { json = false } = {}) {
  let payload;
  try {
    payload = buildPayload(planDir);
  } catch (error) {
    const result = { ok: false, complete: false, errors: [error.message, DOCTOR_HINT], warnings: [], next: null };
    if (json) console.log(JSON.stringify(result, null, 2));
    else console.error(`✗ ${error.message}\n${DOCTOR_HINT}`);
    return result;
  }

  const errors = payload.warnings.filter((w) => HARD.has(w.kind));
  const soft = payload.warnings.filter((w) => !HARD.has(w.kind));
  const { counts } = payload.rollup;
  const archived = payload.rollup.archived || { count: 0, points: 0 };
  const total = payload.cards.length + archived.count;
  const done = counts.done + archived.count;
  const complete = total > 0 && done === total && errors.length === 0;
  const ok = errors.length === 0;

  const result = {
    ok,
    complete,
    pct: payload.rollup.pct,
    points: { done: payload.rollup.donePoints, total: payload.rollup.totalPoints },
    counts,
    archived,
    criticalPath: payload.criticalPath.chain,
    next: payload.nextAction,
    errors: errors.map((e) => e.detail),
    warnings: soft.map((w) => w.detail),
  };

  if (json) {
    console.log(JSON.stringify(result, null, 2));
    return result;
  }

  const bar = renderBar(payload.rollup.pct);
  console.log(`Plandeck · ${payload.plan.title}`);
  console.log(`${bar} ${payload.rollup.pct}%  (${payload.rollup.donePoints}/${payload.rollup.totalPoints} pts · ${done}/${total} cards done)`);
  if (payload.criticalPath.chain.length) console.log(`Critical path: ${payload.criticalPath.chain.join(" → ")}  (${payload.criticalPath.length} pts)`);
  for (const e of errors) console.log(`  ✗ ${e.detail}`);
  for (const w of soft) console.log(`  ⚠ ${w.detail}`);
  if (complete) {
    console.log("✓ COMPLETE — every card is done and the plan is structurally clean.");
  } else if (!ok) {
    console.log("✗ BLOCKED — fix the structural errors above before continuing.");
  } else if (payload.nextAction && payload.nextAction.detail) {
    const id = payload.nextAction.cardId ? `${payload.nextAction.cardId} · ` : "";
    console.log(`→ NEXT: ${id}${payload.nextAction.detail}`);
  }

  return result;
}

function renderBar(pct, width = 24) {
  const filled = Math.round((pct / 100) * width);
  return `[${"█".repeat(filled)}${"·".repeat(width - filled)}]`;
}
