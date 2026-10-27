## Description:

openInvest helps agents review multi-asset portfolios and market data, track investment decisions, and produce committee-based investment verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

External users can inspect portfolio holdings, prices, strategy, and decision history; track position changes; and request multi-role analysis of stocks and other assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented shell-heredoc save workflow can execute commands embedded in AI analysis.

Mitigation: Use the documented MCP submit_committee tool instead until the shell workflow is corrected.

Risk: Portfolio information may be sent to an external provider or remote hub, including during import previews.

Mitigation: Confirm which provider or remote hub receives the information before using these features.

Risk: Enabling brokerage integration can allow live trades.

Mitigation: Keep live brokerage trading disabled unless you deliberately configure and authorize it; enter credentials locally rather than in chat.

## Reference(s):

- [Publisher profile](https://clawhub.ai/user/longsizhuo)
- [openInvest ClawHub release](https://clawhub.ai/longsizhuo/skills/openinvest)
- [Tool reference](artifact/references/tools.md)
- [Committee protocol](artifact/references/committee-protocol.md)
- [Project wiki documentation](https://github.com/longsizhuo/openInvest/tree/main/docs/wiki)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Files]

**Output Format:** [Conversational analysis and Markdown decision reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include portfolio summaries, P&L, asset analysis, and proposed trade amounts; decision reports can be saved for later review.]

## Skill Version(s):

0.32.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
