## Description:

Classifies proposed agent tool calls by risk and suggests whether to allow, confirm, or block them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theoretical text all rights reserved

## Use Case:

Developers configuring agent access to files, networks, messages, or payments can use this advisory classifier to identify tool calls that merit confirmation or blocking before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unrecognized or generic tools can be classified as safe, allowing dangerous actions to pass unchecked.

Mitigation: Treat this as advisory rather than a sole enforcement boundary; require confirmation or block unknown tools by default, define per-tool policies, and test destructive, external-send, payment, and shell-like calls before deployment.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zhaoxinghua09-cell/skills/tool-call-guard)
- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports tool name, risk level, suggested action, reason, and matched terms; advisory only.]

## Skill Version(s):

1.0.2 (source: ClawHub release; artifact frontmatter says 1.1.0 and manifest says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
