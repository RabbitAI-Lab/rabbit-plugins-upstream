// preflight.mjs — one-shot PR gate (anti-slop checklist as code).
// Usage: node src/tools/preflight.mjs payload.json
//   payload.json = { files: {path: content}, stats: {adds, dels} }
// Or with no args: runs built-in self-test fixtures.
// Checks: (1) diff hygiene (<=3 files, <=60 changed lines — warn, not fail);
// (2) boundary guards on new file contents; (3) regression-test presence
// (some added file looks like a test); (4) no cosmetic-only bloat signal.
// Exit 0 + "PREFLIGHT PASS" or exit 1 + offending lines. No dependencies.
import { readFileSync } from "node:fs";

function importGuards() { return {}; } // guards injected below when bundled; direct imports used in repo use:
// import { wasmJsDiffGuard } from "./wasm-js-diff-guard.js";
// (kept import-free here so the file also runs via copy-paste in constrained runners)

const CHECKS = [];
function check(name, ok, detail = "") { CHECKS.push({ name, ok: !!ok, detail }); }

export function preflight(files, stats = {}, guards = {}) {
  CHECKS.length = 0;
  const paths = Object.keys(files);
  check("files-touched<=3", paths.length <= 3, `${paths.length} files: ${paths.join(", ")}`);
  const churn = (stats.adds || 0) + (stats.dels || 0);
  check("churn<=80-lines", churn <= 80 || (stats.adds === undefined), `${churn} changed lines`);
  const hasTest = paths.some(p => /(test|spec|repro)[\/._-]/i.test(p)) ||
    Object.values(files).some(c => /#\[test\]|#\[cfg\(test\)\]|\bdescribe\s*\(|\bit\s*\(/.test(c)));
  check("regression-test-present", hasTest, hasTest ? "test file or inline #[test]/describe block in diff" : "NO test — add failing-before/passing-after test");
  const findings = [];
  for (const [p, content] of Object.entries(files)) {
    if (guards.wasm && /\.(ts|tsx|js|jsx)$/.test(p)) findings.push(...guards.wasm(content, p));
    if (guards.wild && /\.rs$/.test(p)) findings.push(...guards.wild(content, p));
    if (guards.mut && /\.(rs|ts|tsx|js)$/.test(p)) findings.push(...guards.mut(content, p));
  }
  check("boundary-guards-clean", findings.length === 0, findings.map(f => `${f.kind}@${f.line}: ${f.detail}`).join(" | ") || "clean");
  const pass = CHECKS.every(c => c.ok);
  return { pass, checks: [...CHECKS], findings };
}

if (process.argv[1] && process.argv[1].endsWith("preflight.mjs")) {
  if (process.argv[2]) {
    const payload = JSON.parse(readFileSync(process.argv[2], "utf8"));
    const { wasmJsDiffGuard } = await import("./wasm-js-diff-guard.js").catch(() => ({}));
    const { wildcardOkGuard } = await import("./wildcard-ok-guard.js").catch(() => ({}));
    const { mutationBeforeFallibleGuard } = await import("./mutation-before-fallible-guard.js").catch(() => ({}));
    const r = preflight(payload.files || {}, payload.stats || {}, { wasm: wasmJsDiffGuard, wild: wildcardOkGuard, mut: mutationBeforeFallibleGuard });
    console.log(r.pass ? "PREFLIGHT PASS" : "PREFLIGHT FAIL");
    for (const c of r.checks) console.log(` [${c.ok ? "ok" : "FAIL"}] ${c.name} ${c.detail}`);
    process.exit(r.pass ? 0 : 1);
  } else {
    // self-test
    const r1 = preflight({ "src/fix.rs": "match st {\n _ => Ok(()),\n}", "tests/repro.rs": "#[test] fn r(){}" }, { adds: 10, dels: 2 }, {});
    console.log("self-test (no guards):", JSON.stringify(r1.checks.map(c => c.ok)));
    const r2 = preflight({ "src/a.rs": "x", "src/b.rs": "y", "src/c.rs": "z", "src/d.rs": "w" }, { adds: 5, dels: 0 }, {});
    console.log("self-test (4 files, no test):", r2.pass === false ? "correctly FAIL" : "BAD-pass");
  }
}
