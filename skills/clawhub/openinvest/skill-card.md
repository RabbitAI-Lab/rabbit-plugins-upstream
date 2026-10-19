## Description:

openInvest helps agents review multi-asset portfolios, track positions and prices, and produce investment committee verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and their agents use this skill to review holdings and performance, log portfolio activity, and seek multi-role investment analysis across asset classes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can change portfolio records, ledger entries, alerts, and committee history.

Mitigation: Require explicit user confirmation before each write and review resulting records.

Risk: Untrusted news and event content can influence committee analysis.

Mitigation: Treat external content as untrusted and check investment conclusions against reliable data.

Risk: Investment advice could be mistaken for an instruction to place real trades.

Mitigation: Keep brokerage execution separate from the skill and obtain independent approval for trades.

Risk: API tokens may be exposed if entered into chat.

Mitigation: Store tokens in .env rather than chat messages.

## Reference(s):

- [openInvest ClawHub release](https://clawhub.ai/longsizhuo/skills/openinvest)
- [openInvest architecture wiki](https://github.com/longsizhuo/openInvest/tree/main/docs/wiki)
- [Committee protocol](artifact/references/committee-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Portfolio summaries and committee verdicts; portfolio changes require user confirmation.]

## Skill Version(s):

0.31.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
