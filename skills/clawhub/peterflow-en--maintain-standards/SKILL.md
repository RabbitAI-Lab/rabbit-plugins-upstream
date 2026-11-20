---
name: maintain-standards
description: Initialize a workspace standards library, draft proposals, apply a selected decision or check current rules for conflicts and drift against code.
---

# Maintain shared standards

Use ordinary language or one of these actions. Follow multiple actions only when requested.

| Action | Example | Read |
| --- | --- | --- |
| `init [workspace] [--from source] [--scope area]` | “Connect our existing engineering rules.” | [Initialize](references/init.md) |
| `draft [material] [--from source] [--scope area]` | “Turn the review outcome into a proposed rule.” | [Draft a candidate](references/draft.md) |
| `apply [candidate, file#item or decision]` | “Adopt the second proposal.” | [Apply a decision](references/apply.md) |
| `check [area] [--from evidence]` | “Compare the pagination standard with the code.” | [Check current rules](references/check.md) |

A source can be a user decision, local artifact, review or commit. Resolve paths against the requested workspace. Infer an unambiguous target from the conversation. Ask about ambiguous actions or selected items. Offer the four usages for a bare invocation with no discernible goal. Preview and review requests stay read-only.

## Standards levels and ownership

Use the location the user specified, then the active entry in `AGENTS.md` or the project README. Reuse existing directories and filenames. A new PeterFlow workspace defaults to `.peterflow/standards/`.

| Level | Content and default location | Who maintains it |
| --- | --- | --- |
| L0 Team rules | `general.md` contains rules shared by design, implementation and review. | The team owner decides the wording, scope and exceptions. |
| L1 Engineering topics | Top-level pages such as `api.md`, `database.md`, `errors.md` and `testing.md`. | The topic owner decides the wording, scope and exceptions. |
| L2 Feature rules and proposals | `features/<feature>.md` holds current feature rules. `candidates/<topic>.md` holds proposals awaiting a decision. | The agent checks the evidence and drafts a change. The owner adopts, amends, defers or declines it. The agent writes adopted wording into the governing rule. |
| L3 Navigation, evidence and history | The main `README.md`, `features/README.md`, `evidence/`, `sources.md` and `backup/`. | Within its authorization, the agent maintains indexes, checks the version and scope of evidence, records decision sources and archives superseded text. |

For example, a reviewer's suggestion to change database policy starts as an L2 proposal. Once the owner adopts it, the agent can update the L1 rule in `database.md` and record the decision in L3. An explicit decision and authorization to write are enough to proceed directly to `apply`.

## Find the rules for a change

Start at the main index. Read the applicable L0 sections and the L1 topic for the change. If product behavior is affected, follow the feature index to the current L2 rule. Trace shared code to its actual callers. A database index change calls for the database topic. If it also changes what happens when a document opens, read that feature's rule too.

Base design and acceptance on current rules, requirements and contracts. Consult evidence and sources to verify a fact or decision, a selected proposal when handling it, and the archive when tracing an earlier decision. Everyday development, review and default checks follow the current index.

Give readers the condition, what to do and why. Preserve exceptions and the strength of the evidence. Use `plainly` if available for reader-facing prose. The templates also work in a standalone installation. Keep writes within the requested rules and references.
