# Install in Cursor

Unzip the package into the project-level Cursor skills directory:

```bash
mkdir -p .cursor/skills
unzip skill.zip -d .cursor/skills
```

Expected structure:

```text
.cursor/
  skills/
    loop-engineering/
      SKILL.md
      references/
      scripts/
```

Restart or reload Cursor after installation.

Invoke explicitly:

```text
loop: fix this bug and verify the result
```

```text
loop: build this feature with a clear user flow and polished responsive UI
```

```text
loop: research and write this article. No AI slop and no em dashes.
```

```text
loop: generate a prompt for another coding agent. The resulting prompt must also use bounded loop engineering.
```

Light loops stay in memory. Deep or genuinely multi-cycle work can create local state under `.loop/`. By default the initializer uses Git's local exclude file and does not edit the tracked `.gitignore`; pass `--edit-gitignore` only when the project should share that ignore rule.

The `.cursor/skills/loop-engineering/` directory may be committed when the team should share the skill. Keep `.loop/` uncommitted.

Research example:

```text
loop: research whether this framework is a current fit, then write a comparison. Derive the evidence plan for this question and distinguish official documentation from vendor marketing, affiliate pages, SEO/AEO/GEO content, and independent evidence.
```

The protocols are adaptive. They provide fixed reliability boundaries, but the agent derives the task-specific outcome contract, evidence plan, specialist order, and checks from the current request and repository.

Every substantive invocation starts with a compact success card: starting point, target, measure, proof required, guardrails, and next use. Each meaningful cycle records its prediction, actual observation, measured delta, and learning. User responses lead with the result while keeping assignment status separate from evidence maturity.

When multiple checks are needed, the skill detects whether it can use a real specialist, a cold same-session pass, or an in-memory receipt. A handoff is complete only after a recipient returns evidence and the parent records its integration decision.

Loops correct their strategy when evidence contradicts it. They do not autonomously weaken the target, verifier, guardrails, or authority boundaries. Persistent changes to a loop or evaluator require representative before-and-after evidence and appropriate approval.
