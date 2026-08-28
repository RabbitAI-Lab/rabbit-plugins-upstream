## Description:

Provides error classification, recovery, and graceful-degradation patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to classify service and agent errors, choose recovery strategies, and produce user-actionable debugging guidance for resilient integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation and logging examples may capture more context than intended if copied directly into production workflows.

Mitigation: Narrow activation where possible and add redaction or allowlisted fields before logging context or sending alerts.

Risk: Reusable error-handling examples may be adapted without checking fit for a specific service, quota model, or escalation policy.

Mitigation: Review the selected classification and recovery strategy before deployment and tune retry, fallback, and human-escalation behavior for the target system.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-leyline-error-patterns)
- [Metadata Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)
- [Error Classification](modules/classification.md)
- [Recovery Strategies](modules/recovery-strategies.md)
- [Agent Damage Control](modules/agent-damage-control.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions]

**Output Format:** [Markdown with inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no executable tool or API call is defined by the artifact.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
