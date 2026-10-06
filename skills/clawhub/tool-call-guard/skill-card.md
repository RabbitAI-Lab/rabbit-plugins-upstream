## Description:

Helps agents assess tool calls by their potential side effects and suggests allowing reads, confirming writes, or blocking higher-risk actions pending human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and agent operators use this skill to review file, network, messaging, database, and payment tool calls before execution and to set human approval boundaries for consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unknown dangerous commands can receive an ALLOW recommendation.

Mitigation: Do not rely on ALLOW as an enforcement decision for shell commands or irreversible actions; use a fail-closed gate scoped to known tools and require human review.

Risk: Requested tool access is broader than the classifier needs.

Mitigation: Review permissions before installation and grant only the tools needed for the intended workflow.

## Reference(s):

- [Tool Call Guard on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/tool-call-guard)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Markdown guidance or CLI text/JSON classification]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool-call risk level and ALLOW, CONFIRM, or BLOCK recommendation; advisory, not authoritative enforcement.]

## Skill Version(s):

1.0.3 (source: ClawHub release; bundled version labels differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
