## Description:

Audits selected agent action logs to produce a chronological activity ledger and flag writes recorded without a gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code); all rights reserved (documentation and theory)

## Use Case:

Developers and agent operators can review chosen local action logs to trace who did what and identify ungated write actions for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent action logs may contain sensitive context.

Mitigation: Audit only specific logs you choose and review or redact sensitive content before sharing results.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-trace-audit)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text action timeline and violation summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports recorded timestamps, actors, actions, targets, and gate status from the selected log.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
