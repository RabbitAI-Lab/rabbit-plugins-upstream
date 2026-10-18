## Description:

Provides guidance and an advisory classifier for reviewing agent tool calls by their potential side effects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers can use this skill to review proposed file, network, database, messaging, or payment tool calls and plan human approval for actions with side effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unknown or ambiguously named tools may receive an unsafe allow recommendation.

Mitigation: Register tools with explicit permissions and fail closed when a tool is unknown or cannot be classified confidently.

Risk: A suggested confirmation does not itself authorize or stop a destructive, messaging, payment, or database action.

Mitigation: Require approval bound to the exact tool call and its arguments before execution; do not use the classifier as the sole enforcement gate.

Risk: The skill describes an audit trail but does not provide real audit logging.

Mitigation: Add durable logging of attempted calls, approval decisions, and execution outcomes before relying on it for oversight.

## Reference(s):

- [ClawHub tool-call-guard release](https://clawhub.ai/zhaoxinghua09-cell/skills/tool-call-guard)
- [LGD theory (background reference)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Markdown guidance and plain-text or JSON tool-call classifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory classifications include a risk level, suggested action, and reason; they do not enforce tool permissions.]

## Skill Version(s):

1.0.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
