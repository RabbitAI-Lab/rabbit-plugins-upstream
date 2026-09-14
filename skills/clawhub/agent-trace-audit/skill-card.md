## Description:

Builds a traceable action ledger from agent logs, flags ungated write operations, and emits a timeline plus violation list for audit review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and compliance reviewers use this skill to inspect agent action logs, reconstruct what happened, and identify ungated write operations that need human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable install instructions can change what users install over time.

Mitigation: Review install commands and prefer an immutable commit or vetted package version before use.

Risk: The audit script may mislead users if treated as a strict compliance or incident-response gate.

Mitigation: Use the output as review support only and confirm malformed-log handling, action classification, output sanitization, and exit-code behavior before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-trace-audit)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [LGD hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with CLI commands and plain-text audit output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local JSONL log audit; emits a sorted action timeline and violation count.]

## Skill Version(s):

1.0.0 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
