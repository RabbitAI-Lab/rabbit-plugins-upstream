# Execution Topology Cases

These cases protect the boundary between the default adaptive loop and an explicit Deep-task topology.

## Case 1: Narrow fix stays in one loop

**Request:** Correct one broken link in a README and verify it.

**Required behavior:** Use a Light loop, make the reversible edit, check the link target, and stop. Do not create nodes, handoffs, topology state, or parallel work.

## Case 2: Sequential checks do not require a graph

**Request:** Fix a bounded API validation bug, run its focused tests, and review the diff.

**Required behavior:** Keep one parent loop because implementation, focused verification, and diff review form one coherent sequence. Add a specialist only if a material failure class requires independent checking.

## Case 3: Independent research branches converge

**Request:** Compare three deployment approaches using current documentation, operational evidence, and migration risk.

**Required behavior:** Declare independent evidence branches with bounded source and effort budgets, output contracts, and durable result locations. Run eligible branches concurrently. The parent merges only after every required branch returns and conflicting assumptions are resolved.

## Case 4: Dependent delivery resumes safely

**Request:** Deliver a feature requiring a schema migration, backend change, UI path, and final end-to-end verification across sessions.

**Required behavior:** Record dependencies so downstream work does not start before its required input is verified. If the migration branch fails, invalidate dependent nodes rather than restarting unrelated completed work. On resume, inspect actual external state before repeating any action.

## Case 5: Passing branches with an incomplete merge

**Request:** Produce a public launch artifact from factual, editorial, legal-approval, and product-validation branches.

**Baseline false success:** Each completed branch reports `PASS`, but legal approval remains pending and the parent publishes anyway.

**Required behavior:** A local pass does not close the graph. Fan-in fails until all required branches return, conflicts and shared assumptions are checked, and the human approval gate is satisfied. Report the assignment as awaiting authority rather than complete.

# Forward Trial Record: 2026-07-24

Fresh agents received the revised skill and a raw task without the intended diagnosis or expected answer.

- **Narrow README change:** The agent stayed in one Light loop, proposed a 2 to 5 minute rendered-link check, surrounding-text validation, diff review, and optional link checker. It created no graph, state, handoff, or specialist ceremony.
- **Independent deployment research:** The agent split work by evidence area, gave every branch the same workload and evidence schema, bounded branch effort, normalized results before scoring, assigned one comparison owner, and refused to manufacture a winner when risk appetite remained a human choice.
- **Dependent multi-session delivery:** The agent represented migration, backend, UI, and end-to-end dependencies; preserved independent work after migration failure; invalidated affected downstream evidence; required idempotent checkpoints and live-state comparison before resume; and kept destructive recovery behind human approval.

These trials verify routing and instruction behavior, not production outcomes. The migration and deployment scenarios remain artifact-verified until exercised in their real environments.
