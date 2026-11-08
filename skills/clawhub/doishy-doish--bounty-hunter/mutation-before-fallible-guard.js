// mutation-before-fallible-guard.js — dirty-state-before-early-return.
// In async flows a function mutates local cache/flags, then calls a fallible
// operation (`?` in Rust, `await` on a throwing call in TS). On failure the
// function returns early but the mutation stands: memory/store is now
// out-of-sync with disk/chain. Rust-side: `self.x =` / `*ptr =` before a `?`
// with no revert/rollback comment. TS-side: `this.x =` / `store.set(` / cache
// write before an `await` inside a try whose catch doesn't restore.
// Conservative by design (review-hint severity): flags the ordering, a human
// confirms whether the catch path restores it.
// Returns rows: [{line, kind, detail}].
export function mutationBeforeFallibleGuard(src, name = "<src>") {
  const rows = [];
  const lines = String(src).split("\n");
  const mutRe = /(self\.\w+\s*=|\*\w+\s*=|this\.\w+\s*=|\bstore\.set\s*\(|\bcache\.(set|put)\s*\(|set\w+\s*\(.*\)\s*;?\s*\/\/\s*flag)/;
  for (let i = 0; i < lines.length; i++) {
    if (!mutRe.test(lines[i])) continue;
    if (/revert|rollback|restore|compensat/i.test(lines.slice(i, i + 3).join("\n"))) continue;
    for (let j = i + 1; j < Math.min(lines.length, i + 12); j++) {
      const l = lines[j];
      if (/^\s*(fn |function |async function|const \w+ = (async )?\(|}\s*$)/.test(l)) break; // left the function
      if (/\?\s*;/.test(l) || /await\s+\w+\s*\(/.test(l)) {
        rows.push({ line: i + 1, kind: "mutation-before-fallible", detail: `mutation at line ${i + 1} precedes fallible op at line ${j + 1} in ${name} — verify the error path restores it` });
        break;
      }
      if (/catch\s*\(/.test(l)) break; // handled locally below; still listed once
    }
  }
  return rows;
}
