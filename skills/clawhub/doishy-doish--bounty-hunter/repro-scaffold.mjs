// repro-scaffold.mjs — red-test generator. Takes a harvested failing_assertion
// and emits a drop-in regression test file for the target repo, so the alert
// response starts with the red test already written — only the green diff left.
// Usage: node src/tools/repro-scaffold.mjs '{"id":"core#9999","lang":"rs","assertion":"..."}'
// Langs: rs (cargo #[test]), ts (vitest). No dependencies.
export function scaffold({ id, lang, assertion, targetHint = "" }) {
  const safe = String(id).replace(/[^A-Za-z0-9]/g, "_");
  if (lang === "ts") {
    return {
      path: `test/repro-${safe}.test.ts`,
      content: `// Repro for bounty ${id}${targetHint ? ` (${targetHint})` : ""}\n// Harvested assertion — must FAIL before the fix, PASS after.\nimport { describe, expect, it } from "vitest";\n\ndescribe("repro ${id}", () => {\n  it("harvested assertion", () => {\n    // TODO: arrange inputs per issue body, then:\n    // ${String(assertion).split("\n")[0]}\n    expect(true).toBe(true); // replace with real assertion\n  });\n});\n`,
    };
  }
  return {
    path: `tests/repro_bounty_${safe}.rs`,
    content: `// Repro for bounty ${id}${targetHint ? " (" + targetHint + ")" : ""}\n// Harvested assertion — must FAIL before the fix, PASS after.\n#[test]\nfn repro_bounty_${safe}() {\n    // TODO: arrange inputs per issue body, then assert:\n    // ${String(assertion).split("\n")[0]}\n    todo!("fill repro from issue body");\n}\n`,
  };
}

if (process.argv[1] && process.argv[1].endsWith("repro-scaffold.mjs") && process.argv[2]) {
  const arg = JSON.parse(process.argv[2]);
  const r = scaffold(arg);
  console.log("path: " + r.path + "\n" + r.content);
}
