---
name: plan
description: Turn a feature request or change of direction into an implementation plan grounded in the current code, with observable acceptance criteria.
---

# Plan a change

Start with the result the user wants. Identify the workspace, scope, project instructions, current callers and existing tests. Inspect the working tree and index before proposing edits. Preserve ongoing work, including in a repository without a first commit.

Use the user's or project's standards entry point (default `.peterflow/standards/`). Follow its main index (L3) to applicable team rules (L0) and engineering topics (L1). For product behavior, trace the actual callers and follow the feature index to the adopted L2 rule. Turn relevant clauses into acceptance criteria with their source, conditions and exceptions. Use proposals and archives only for background. Where no library exists, plan from the requirements at hand.

When two plausible readings of the request give different results, find one input that distinguishes them. Use the requirement or a recorded decision to establish the expected result. If neither settles it, state what depends on that decision and what can proceed. Resolve implementation details from the code.

Choose the workflow by the scope of the change and the difficulty of verifying it. Honor a workflow the user has selected.

| Change | What the next person needs |
| --- | --- |
| Small, bounded edit with clear acceptance | A short plan in chat can cover the goal, edit and check. Continue with `implement`. |
| Several behaviors within a module need separate implementation and checks | Settle the design and dependencies. Use `tasks` to split the work into phases, then `implement`. |
| Several parts need independent delivery and acceptance plus a final check of the whole feature | Define boundaries, contracts and the combined check. Use `tasks-pro` to split the phases and `implement-pro` to execute them. |

Trace the proposed change through the real entry point. Identify the files, interfaces or data that change, consumers that must keep working, dependencies and the command or operation that will prove the result. Distinguish an expected observation from a test already run.

Reuse the user's files and location. New plans can use [the plan outline](assets/plan.md) at `.peterflow/specs/<topic>/plan.md`. A small change can keep the requirement, plan and verification together. For larger work, add `design/` for a separate design, `references/` for source material, `verification/` for evidence, `delivery/` for deployable artifacts or `contracts/` for shared contracts only when writing an actual file. Link existing authorities and preserve content at conflicting paths.

Return the plan or its path, the decisions, how to check them and any unresolved choice. Continue work already authorized. The next person can implement a small change directly or break a larger one into tasks.
