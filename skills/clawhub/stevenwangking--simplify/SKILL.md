---
name: simplify
description: Simplify and refine recently modified code for clarity, consistency, reuse, and maintainability without changing behavior. Use when the user asks to simplify, clean up, refine, polish, or tidy code; when changed code is too nested, repetitive, overly clever, or off-style; or after tests pass and before committing.
---

# Simplify

Reduce complexity while preserving exact behavior. The goal is not fewer lines — it is code a new team member understands faster than the original.

## When to use

- A feature works and tests pass, but the implementation feels heavier than it needs to be
- Changed code shows deep nesting, duplication, unclear names, or dense one-liners
- As a final polish before committing or opening a PR

Skip it when: tests are failing (fix or confirm the baseline first — pre-existing failures elsewhere don't block, but distinguish them from failures you introduce); you don't yet understand the code; the code is already clean; a "simpler" version would be measurably slower; the module is about to be rewritten.

## Workflow

### 1. Scope to what changed

Default to the files and hunks modified in the current task — derive the scope from the diff, don't guess. If the user names a file or function, use exactly that. No drive-by cleanup of unrelated code. One sanctioned widening: if correctness requires touching a helper or its direct callers just outside the diff, follow the call chain only as far as the change requires, and say so in the summary.

### 2. Understand before touching

Chesterton's fence: don't remove what you can't explain. Before changing anything, answer — what is this code's responsibility, what calls it, which tests define its behavior, and why might it exist this way (performance, platform constraint, history — check git blame). Can't answer? Read more first.

### 3. Match project conventions

Simplification means moving code toward the codebase's style, not imposing external preferences. Read AGENTS.md / CLAUDE.md, study how neighboring code handles imports, naming, and error handling, and respect lint/formatter config. Simplification that breaks project consistency is churn.

### 4. Review through three lenses

- **Reuse** — prefer existing helpers before adding new ones. Extract a shared abstraction only when the behavior is genuinely identical, the concept has a clear name, and callers evolve together. Prefer a little duplication over a misleading abstraction.
- **Quality** — improve readability, naming, branching, and cohesion; preserve logging, validation, and error semantics.
- **Efficiency** — remove redundant work (extra passes, allocations, awaits, lookups) only when the improvement is obvious and behavior stays identical. A restraint check, not speculative optimization.

When lenses conflict, prefer behavioral safety and readability.

Investigate these signals — they are hints, not triggers; never refactor solely because a threshold was crossed:

| Category | Pattern | Direction |
|----------|---------|-----------|
| Structure | Deep nesting (3+ levels), long functions (50+ lines), nested ternaries, boolean flag params | Guard clauses, focused helpers, explicit branching, options object |
| Naming | Generic (`data`, `res`, `val`), abbreviated, or misleading names | Name what it holds or does |
| Redundancy | Same 5+ lines in several places, dead code, valueless wrappers, redundant assertions or `await` | Extract only genuinely shared concepts; delete confirmed-dead code; inline |
| Comments | "What" comments on obvious code | Delete them; keep "why" comments |

### 5. Simplify with restraint

Prefer flattened nesting with early returns, clear names, small cohesive helpers, and explicit control flow over dense one-liners.

```typescript
// Before
const label = item.isNew ? 'New' : item.isUpdated ? 'Updated' : item.isArchived ? 'Archived' : 'Active';
// After
function getStatusLabel(item: Item): string {
  if (item.isNew) return 'New';
  if (item.isUpdated) return 'Updated';
  if (item.isArchived) return 'Archived';
  return 'Active';
}
```

Do not swap between `||`, `??`, truthiness checks, and optional chaining — or replace `if` with logical expressions — without proving the edges behave identically (falsy values, empty collections, thrown errors, async ordering). Don't rewrite loops as `map`/`filter` chains when the loop is easier to follow. For Vue code, preserve reactivity, dependency tracking, lifecycle timing, `v-model`, and emitted events — they are contracts, not implementation details.

Classic traps: inlining a helper that gave a concept its name; merging unrelated logic into one complex function; removing abstractions that exist for extensibility or testability; optimizing for line count. If the change grows into a broad refactor, stop and reassess the scope.

### 6. Verify before finishing

- Re-read the diff for behavior drift: async ordering, type regressions, weakened error handling, changed edge cases
- Run the smallest relevant check — lint, types, build, or tests; distinguish pre-existing baseline failures from ones you introduced (only the latter are yours to fix or revert)
- Confirm the result is genuinely easier to understand and the diff stays clean

## Guardrails

- Inputs, outputs, side effects, error behavior, and edge cases stay identical — if unsure a change preserves behavior, don't make it
- No public API, storage format, or user-visible text changes unless explicitly requested
- No weakening of error handling, logging, or validation
- Naming follows project conventions, not personal preference
- Don't modify tests to hide a behavior change — if a test must change because a mock or test seam moved, first verify the behavioral contract is intact
- Keep refactoring commits separate from feature or bug-fix commits

## Output

Make changes directly when actionable; state uncertainties before editing. Summarize only meaningful simplifications and the validation that was run. Finding nothing worth changing is a valid outcome — a clean "nothing to change" beats forced edits.
