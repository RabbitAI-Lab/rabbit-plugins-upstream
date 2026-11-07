// wildcard-ok-guard.js — swallowed error variant (Rust `_ => Ok(())`).
// The most common bounty-grade Rust logic bug that passes CI: a match on a
// state/status/phase enum with a wildcard arm that returns Ok(())/None instead
// of handling (or explicitly rejecting) the variant. A newly introduced variant
// (PendingWithdrawal, Disputed) then falls through silently.
// Flags: match on a state-like scrutinee whose `_ =>` arm body contains
// Ok(, None, return Ok, or an empty/comment-only body.
// Returns rows: [{line, kind, detail}]. Review-hint severity: confirm the enum
// can't grow a meaningful variant before dismissing.
export function wildcardOkGuard(src, name = "<src>") {
  const rows = [];
  const lines = String(src).split("\n");
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(/match\s+([\w.:()]+)\s*\{/);
    if (!m) continue;
    const scr = m[1].split(/[.:(]/)[0].trim();
    if (!/state|status|phase|stage|step|kind|variant|result|outcome|res\b|st\b/i.test(m[1]) && !(scr.length <= 10 && /^[A-Za-z_]\w*$/.test(scr))) continue;
    // scan the match body for a wildcard arm (brace-depth aware, capped).
    // The arm's own line counts: `_ => Ok(())` carries the swallow inline.
    let depth = 0, j = i, armLine = -1, armBody = [];
    for (; j < Math.min(lines.length, i + 60); j++) {
      const l = lines[j];
      if (armLine < 0 && /^\s*_\s*=>/.test(l)) { armLine = j + 1; armBody.push(l.slice(l.indexOf("=>") + 2)); }
      else if (armLine >= 0) armBody.push(l);
      depth += (l.match(/\{/g) || []).length - (l.match(/\}/g) || []).length;
      if (armLine >= 0 && depth <= 0 && j > i) break;
    }
    const body = armBody.join("\n");
    if (armLine >= 0 && (/Ok\(\s*\(\s*\)\s*\)|return\s+Ok|=>\s*None\b|=>\s*Ok\(\(\)\)/.test(body) || /^\s*(\/\/[^\n]*\n|\s*)*,?\s*$/.test(body))) {
      rows.push({ line: armLine, kind: "wildcard-swallow", detail: `match on "${m[1]}" has a wildcard arm returning Ok/None in ${name} — new variants fall through silently; match every variant or deny` });
    }
    i = j;
  }
  return rows;
}
