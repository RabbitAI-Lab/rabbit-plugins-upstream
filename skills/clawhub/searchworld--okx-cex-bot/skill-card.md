## Description:

Manages OKX Grid and DCA Martingale bots, including creation, stopping, amendment, P&L monitoring, TP/SL, margin and investment adjustments, and AI-recommended parameters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through OKX Grid and DCA bot operations, including setup checks, command construction, live/demo mode selection, write confirmation, and post-action verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing this skill can let an agent use OKX credentials for real trading-bot actions.

Mitigation: Use demo mode first, confirm live versus demo mode before each write action, and require explicit user confirmation before creating, amending, stopping, or closing bot positions.

Risk: Raw API keys or sensitive profile details could be exposed during troubleshooting.

Mitigation: Use OKX configuration flows for credential setup and avoid placing raw API keys in chat, logs, or copied command output.

Risk: Incorrect bot IDs, bot types, or stop modes can affect the wrong bot or leave positions open.

Mitigation: List existing bots before acting, use server-returned algo IDs and algo order types, and verify state after every write action.

## Reference(s):

- [OKX](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-bot)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline OKX CLI shell commands and JSON-aware command output handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to run authenticated OKX CLI commands that read bot state or create, amend, stop, and verify trading bots.]

## Skill Version(s):

1.4.4 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
