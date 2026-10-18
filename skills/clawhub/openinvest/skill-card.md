## Description:

openInvest helps agents review multi-asset portfolios, track markets and transactions, and produce investment committee verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and their agents use this skill to review holdings and performance, monitor assets, record portfolio changes, and request multi-role investment analyses. It supports both interactive and scheduled workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portfolio actions can alter holdings, cash, trades, alerts, or configuration.

Mitigation: Confirm each write action with the user before changing investment records or settings.

Risk: Remote access may expose investment data or bearer tokens over unencrypted HTTP.

Mitigation: Use HTTPS for remote hubs, never send bearer tokens over plain HTTP, and keep API keys in .env rather than chat.

## Reference(s):

- [openInvest on ClawHub](https://clawhub.ai/longsizhuo/skills/openinvest)
- [Choosing a committee path](artifact/references/two-paths.md)
- [Tool and API reference](artifact/references/tools.md)
- [Project documentation](https://github.com/longsizhuo/openInvest/tree/main/docs/wiki)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown explanations and committee memos; JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include portfolio metrics, investment verdicts, supporting analysis, and suggested next steps.]

## Skill Version(s):

0.28.0 (source: release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
