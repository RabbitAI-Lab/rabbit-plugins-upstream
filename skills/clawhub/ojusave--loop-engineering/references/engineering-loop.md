# Engineering Loop

## Contents

- [Outcome](#outcome)
- [Observe](#observe)
- [Define acceptance](#define-acceptance)
- [Choose](#choose)
- [Act](#act)
- [Verify](#verify)
- [Diagnose](#diagnose)
- [Handoff to product specialists](#handoff-to-product-specialists)
- [Return criteria](#return-criteria)


## Outcome

Produce the smallest correct, maintainable change that advances the parent target without unrelated regressions. Verify the implementation and validate the target behavior in its intended runtime context when feasible.

## Observe

Inspect before editing:

- repository instructions
- architecture and module boundaries
- call sites and data flow
- existing tests
- runtime and build commands
- error handling
- relevant configuration
- current dependencies
- recent changes when available

Reproduce the issue or establish the current baseline whenever possible.

## Define acceptance

Record:

- inherited baseline, target measure, guardrails, and required evidence state
- target behavior
- current failing behavior or missing capability
- public contracts that must remain stable
- data and error cases
- security or permission boundaries
- targeted and broader checks
- rollback or reversibility needs

For a bug, the original reproduction must fail before the fix and pass afterward when practical.

## Choose

Prefer, in order:

1. Fixing the root cause inside an existing abstraction
2. Reusing an existing utility or pattern
3. Adding a small local abstraction
4. Introducing a current maintained dependency after the freshness gate
5. Refactoring architecture only when the request cannot be solved safely otherwise

Do not mix unrelated cleanup into the same change.

## Act

Implement one coherent slice:

- preserve types and contracts
- handle boundary conditions
- produce useful errors
- avoid silent fallbacks that hide failures
- keep configuration explicit
- add or update tests when behavior changes
- preserve observability where relevant

For high-risk work such as authentication, billing, permissions, migrations, infrastructure, concurrency, or destructive operations, define a rollback and require stronger verification.

## Verify

Run the repository's relevant checks, such as:

- targeted tests
- integration tests
- type checks
- lint
- build
- schema validation
- API or CLI reproduction
- runtime logs
- final diff inspection

Name checks and observed outcomes. Do not report `all tests pass` when only a narrow test ran.

Separate artifact verification from behavior validation. Tests, types, lint, builds, schemas, and diff review verify the implementation. The original or representative scenario observed through the relevant API, CLI, UI, runtime, or production-like environment validates intended behavior. If only artifact checks are available, report `ARTIFACT VERIFIED`; do not claim `OUTCOME VALIDATED`.

Inspect the final diff for:

- accidental files
- debug output
- dead code
- stale comments
- copied secrets
- unnecessary dependencies
- scope creep
- generated artifacts that should not be committed

## Diagnose

When a check fails:

- preserve the failure
- identify the contradicted assumption
- inspect adjacent behavior before patching
- avoid weakening the test
- change direction after two failures of the same approach

## Handoff to product specialists

When the change affects user-visible behavior, hand over:

- running artifact and path
- primary flow
- backend states and errors exposed to the UI
- data assumptions
- verified behavior
- unverified UX risks

Engineering cannot approve UX, visual design, or accessibility.

## Return criteria

Return `PASS` when:

- target behavior is observed
- material checks pass
- public contracts are preserved or intentionally changed
- final diff is scoped and clean
- remaining UI, UX, accessibility, or portability checks are handed to the parent
- the local evidence state and any remaining parent-outcome validation gap are explicit

Return `REWORK_REQUIRED` for a concrete correctable failure.
Return `BLOCKED` when the environment or dependency cannot be accessed.
Return `NEEDS_HUMAN_JUDGMENT` for architecture or risk choices not determined by evidence.
