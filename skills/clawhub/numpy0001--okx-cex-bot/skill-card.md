## Description:

Manage OKX grid and DCA Martingale trading bots, including creation, stopping, amendment, P&L monitoring, TP/SL, margin or investment adjustment, and AI-recommended parameters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[numpy0001](https://clawhub.ai/user/numpy0001)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading operators use this skill to manage native OKX server-side grid and DCA bots through the OKX CLI after confirming credentials, trading mode, parameters, and user approval for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, amend, or stop live OKX trading bots that may affect real funds.

Mitigation: Prefer demo mode for testing and allow live bot create, amend, or stop actions only after explicit user confirmation.

Risk: The CLI install and credential-check steps are under-scoped in the security evidence.

Mitigation: Pin the OKX CLI package to the reviewed version and avoid elevated or global installs where possible.

Risk: `okx config show --json` may expose credential material if it does not mask secrets.

Mitigation: Confirm the command masks secrets before using shared output, and never accept credentials in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/numpy0001/skills/okx-cex-bot)
- [Publisher profile](https://clawhub.ai/user/numpy0001)
- [OKX homepage](https://www.okx.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with OKX CLI command examples and JSON-output recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the OKX CLI and an authenticated live or demo profile; write operations require explicit user confirmation.]

## Skill Version(s):

1.3.8 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
