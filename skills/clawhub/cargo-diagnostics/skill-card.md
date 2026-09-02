## Description:

Cargo Diagnostics helps agents explain Cargo workflow behavior after execution by tracing runs, grouping batch errors, drawing executed graphs, and attributing credit spend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and Cargo workspace users use this skill to diagnose failed, incorrect, empty, or unexpectedly expensive Cargo runs and batches after execution. It guides agents through run tracing, batch error grouping, graph inspection, and credit attribution before proposing fixes or paid reruns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect Cargo workflow, run, and billing data in the active workspace.

Mitigation: Install it only for a Cargo workspace the agent is intended to inspect, and confirm the active workspace before running commands.

Risk: Billing attribution steps may require an admin token.

Mitigation: Use admin tokens only when billing attribution is needed; standard diagnostics should use standard access where possible.

Risk: Suggested reruns or workflow changes can incur additional credits or alter workflow behavior.

Mitigation: Review proposed edits and provider swaps, and approve paid reruns only after a pilot cost estimate is shown.

## Reference(s):

- [Cargo Diagnostics ClawHub page](https://clawhub.ai/cargo-ai/skills/cargo-diagnostics)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Run trace](references/run-trace.md)
- [Batch error sweep](references/batch-error-sweep.md)
- [Play cost profile](references/play-optimize-credits.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and compact evidence tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Cargo CLI queries, workflow fixes, cost reductions, and paid rerun pilots for user approval.]

## Skill Version(s):

1.4.0 (source: frontmatter, skill-metadata.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
