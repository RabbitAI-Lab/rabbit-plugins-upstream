## Description:

Helps agents and developers make calls to unstable external APIs more resilient with retry backoff, jitter, rate-limit handling, circuit breaking, and fallback guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill when an agent depends on external services such as models, search, or databases and needs resilient call patterns. It guides retry, backoff, rate-limit, circuit-breaker, and fallback behavior so transient failures do not cascade.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install instructions fetch mutable remote content and can install the skill globally without version or integrity checks.

Mitigation: Review or pin an exact package version or Git commit before installing, prefer a project-scoped install, and use the global install path only when the skill should be available to future agent sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/api-resilience)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON output from the demo script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a zero-dependency Python demo for simulated API retry and circuit-breaker behavior.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
