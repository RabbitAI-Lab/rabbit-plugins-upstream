## Description:

Uses the Nansen CLI to find tokens with smart-money activity by cross-referencing screener results with netflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Crypto researchers use Nansen CLI commands to screen tokens for smart-money activity and compare candidates with netflow and token flow data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated research calls may consume paid credits or trigger wallet payments, including in loops.

Mitigation: Confirm the selected API key or saved session, available credits, wallet payment policy and spending limits before making calls; avoid repeated calls without cost review.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-smart-money-alpha)
- [Nansen CLI npm package](https://www.npmjs.com/package/nansen-cli)
- [Nansen CLI browser login platform scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and research guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Screener candidates are compared with smart-money netflow and token flow data.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
