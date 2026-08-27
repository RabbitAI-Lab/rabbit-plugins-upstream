## Description:

Audits Rust code for unsafe blocks, ownership issues, and Cargo dependency risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review Rust changes before merge, with emphasis on unsafe code, ownership and lifetime issues, concurrency, error handling, dependency risk, idioms, tests, and SQL injection patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes optional commands such as cargo install cargo-mutants, cargo mutants --workspace, cargo audit, cargo outdated, and cargo deny check that can use network, CPU, disk, or project resources.

Mitigation: Confirm the project scope and explicitly approve tool, network, and resource use before running these commands.

Risk: The skill is an opinionated Rust review assistant, so findings and recommendations may need project-specific validation.

Mitigation: Treat output as review guidance and require maintainer review before merging code or applying blocking recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-rust-review)
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown audit report with optional shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured findings, risk assessments, recommendations, and approve/approve with actions/block decision.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
