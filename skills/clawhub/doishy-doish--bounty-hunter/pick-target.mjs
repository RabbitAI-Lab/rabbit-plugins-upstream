// pick-target.mjs — serial-lock selector (winner-take-all doctrine 2026-11-05).
// Reads a bounty-alerts.json payload (live file or fetched), re-ranks with the
// same 3-tier filter the harvester uses, and prints the single lock target.
// Usage (page_eval or execute_js):
//   const pick = await import("./src/tools/pick-target.mjs");
//   pick.pickOne(alertsJson) -> top alert object or null
// Protocol: lock alerts[0], ignore rest, 30-min budget, PR -> unlock,
// re-verify next (fresh competing_prs/claims) before touching code. Max 2 sprints.
export function reproTier(r) {
  if (r.failing_assertion) return 2;
  if (r.has_repro || r.repro_command) return 1;
  return 0;
}
export function estMinutes(r) {
  const n = Array.isArray(r.target_files) ? r.target_files.length : 0;
  let m = 10 + n * 10;
  m += r.failing_assertion ? -5 : 15;
  m += r.has_stack_trace ? 0 : 10;
  return Math.max(5, m);
}
export function rankAll(alerts) {
  return [...alerts]
    .map(r => ({ ...r, selection_rank_tier: reproTier(r), est_minutes: estMinutes(r), reward_density: Math.round(((r.reward_usdc || 0) / estMinutes(r)) * 100) / 100 }))
    .sort((a, b) =>
      (b.selection_rank_tier - a.selection_rank_tier) ||
      (a.est_minutes - b.est_minutes) ||
      (b.reward_density - a.reward_density) ||
      ((b.reward_usdc || 0) - (a.reward_usdc || 0)));
}
export function pickOne(alertsJson) {
  const list = Array.isArray(alertsJson) ? alertsJson : (alertsJson.alerts || []);
  const ranked = rankAll(list);
  return ranked[0] || null;
}
