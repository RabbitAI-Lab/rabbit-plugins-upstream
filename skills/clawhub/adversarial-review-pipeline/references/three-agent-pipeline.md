# The Three-Agent Pipeline

Writer -> Breaker -> Reviewer. The classic adversarial shape.

## Tier 2 — Three-agent pipeline (Writer → Breaker → Reviewer)

The classic shape. Use it when your environment supports subagents and the
change is large enough to justify the coordination cost. It is **not** the
default, and a single-agent Tier 1 review is a legitimate choice for most
changes.

```
Writer  ->  Breaker  ->  Reviewer  ->  Human
 (code)     (findings)   (verdict)    (decide)
```

| Role | Job | Writes |
|---|---|---|
| **Writer** | Implements the change | the code |
| **Breaker** | Finds problems. Never writes fixes. | `breaker-<slug>.md` |
| **Reviewer** | Reconciles and produces a verdict | `review-<slug>.md` |

**Each role sees a different slice, and that is the point:**

- The **Writer** sees only the requirement.
- The **Breaker** sees only the Writer's output - never the Writer's
  reasoning. That isolation is what makes it adversarial.
- The **Reviewer** sees both the artifact and the findings, and reconciles
  them into a verdict.

### The Writer prompt

```text
Implement <the task>.

Scope the change first: list every place it must reach, and find every
caller of anything you change. That list is the scope - extra features are
not.

Then take the smallest complete change, in this order:
1. Does it need to exist at all? Skip anything nobody asked for and name it
   in one line.
2. Does the codebase already have a component for this? Use it the way the
   surrounding code does.
3. Standard library or platform feature? Use it, unless the project has
   its own.
4. Installed dependency? Use it. Do not add a dependency for a few lines.
5. One line a reader gets at a glance? One line.
6. Otherwise, the minimum code that works.

Deletion beats addition. Keep the codebase's own layers, interfaces, and
conventions. No wrapper, option, config, or "for later" code nobody asked
for.

Be lazy about the solution, never about the change: finish every part the
task needs, including the callers, tests, and fixtures the change breaks.

Validation at trust boundaries, error handling that prevents data loss,
security, accessibility, and anything explicitly requested are never cut.
```

### The Breaker prompt

Give the Breaker the artifact, not the author's reasoning, and tell it
explicitly not to fix anything:

```text
Review the change at <path-to-diff-or-branch>. Your ONLY job is to find
problems.

- Run the tests
- Check edge cases, empty states, and boundary values
- Look for security issues: authorization, injection, IDOR, secrets in logs
- Identify logic errors
- Question the assumptions
- YAGNI: flag speculative generality, unused abstractions, or features the
  task does not exercise
- DRY: flag duplicated logic, duplicated domain concepts, duplicated
  validation
- REINVENTION: flag a new helper/service/constant built when the codebase
  already has one - name the existing one to use
- UNNECESSARY INDIRECTION: flag a dependency, wrapper, or conversion layer
  replaceable by the standard library or a few lines

Do NOT suggest fixes. Just report what's broken.

Output: write findings to <path>/breaker-<slug>.md with severity labels
(block-merge / high / medium / low), a `## YAGNI & DRY Review` section, and
end with a `## Scope & Skipped` section.
```

### The Reviewer prompt

The Reviewer reconciles. Critically, it does **not** rubber-stamp the
Breaker - if the Breaker found nothing, the Reviewer verifies independently.

```text
Review the change at <path-to-diff-or-branch> and the findings at
<path>/breaker-<slug>.md.

- If the Breaker found issues: assess severity and propose fixes
- If the Breaker found nothing: verify independently. Do not trust the
  Breaker either.
- Review the `## YAGNI & DRY Review` section: is the speculative code or the
  duplication worth the complexity? Recommend removal, extraction, or accept
  with a rationale.
- Check every finding against the code before accepting it. A finding that
  does not hold up should be dropped, with the reason.

Produce a final verdict: ACCEPT / ACCEPT WITH FIXES / REJECT.

Output: write the verdict to <path>/review-<slug>.md
```

### The verdict is not the decision

The Reviewer produces a recommendation. A human decides. Report back with:

- **What was written** - the change itself
- **What the Breaker found** - count by severity
- **What the Reviewer recommends** - the verdict and any unresolved concerns
- **Your confidence** - and anything you could not verify

### Cost, and when it is not worth it

The three-agent pipeline costs roughly three times a single-agent review. If a
Tier 1 review finds nothing and the change is not on a risky path, you have
already spent the budget. Do not run the pipeline to feel thorough.

The combined tier table is at the end of Tier 3.

---
