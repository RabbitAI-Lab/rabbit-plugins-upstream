## Description:

Cargo Diagnostics helps agents explain Cargo workflow runs after the fact by tracing individual runs, grouping batch errors by root cause, drawing executed graphs, and attributing credit spend by node and provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to diagnose failing, incorrect, empty, expensive, or misrouted Cargo workflow runs. It guides agents through run traces, batch failure sweeps, graph inspection, and credit attribution before recommending a fix or escalation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads Cargo workspace workflow and billing data while diagnosing failures and costs.

Mitigation: Install only after trusting the Cargo CLI package, use the lowest token scope that works, and summarize findings instead of exposing raw run or billing data.

Risk: Credit attribution and subscription checks may require admin access.

Mitigation: Use admin-scoped tokens only for the billing commands that require them and confirm the active workspace with `cargo-ai whoami` before running diagnostics.

Risk: Suggested reruns, workflow edits, connector reauthentication, batch creation, or admin billing queries can change state or spend credits.

Mitigation: Require explicit user approval before those actions, pilot paid reruns on a small sample, and report the observed cost and record count before scaling.

## Reference(s):

- [Cargo Diagnostics skill page](https://clawhub.ai/cargo-ai/skills/cargo-diagnostics)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Run trace](references/run-trace.md)
- [Batch error sweep](references/batch-error-sweep.md)
- [Play cost profile](references/play-optimize-credits.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with inline Cargo CLI and SQL command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact evidence tables, graph commands, cost estimates, and escalation guidance; avoids raw run JSON dumps.]

## Skill Version(s):

1.3.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
