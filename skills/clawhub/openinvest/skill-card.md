## Description:

Helps agents review multi-asset portfolios, track investments, and produce investment-committee verdicts using market data and recorded decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and their agents use this skill to review holdings and trade history, check prices, record portfolio changes, and obtain multi-asset investment-committee analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill and its backend can read and retain sensitive portfolio and trade records.

Mitigation: Use only if comfortable sharing these records with the skill and its backend; protect access to the local or remote dataset.

Risk: Write actions can change portfolio, cash, or configuration records.

Mitigation: Confirm each proposed change matches the user's intent before executing it.

Risk: Untrusted financial news may influence investment recommendations or trigger new analysis.

Mitigation: Review news relevance and source quality before ingestion, and treat resulting verdicts as guidance rather than verified facts.

Risk: Remote hub connections and exposed API keys can disclose sensitive investment data.

Mitigation: Limit remote access and keep API keys in the documented local .env rather than in chat.

## Reference(s):

- [ClawHub openInvest release](https://clawhub.ai/longsizhuo/skills/openinvest)
- [openInvest technical wiki](https://github.com/longsizhuo/openInvest/tree/main/docs/wiki)
- [Committee protocol](artifact/references/committee-protocol.md)
- [Tools and API reference](artifact/references/tools.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and JSON-backed investment summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes portfolio summaries and committee verdicts; portfolio write actions change stored records.]

## Skill Version(s):

0.26.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
