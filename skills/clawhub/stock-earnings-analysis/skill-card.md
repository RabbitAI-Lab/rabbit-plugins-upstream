## Description:

Organizes read-only U.S. stock earnings research by fiscal quarter, combining reported results, management guidance, earnings-call summaries, SEC risk-factor changes, and market context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and other users use the skill to review U.S. public-company earnings by quarter, including results, management guidance, call summaries, and related filing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company queries are sent to SentiSense, and API access uses an API key.

Mitigation: Use a dedicated SentiSense API key and omit a private agent name from optional client identification.

Risk: Returned summaries may be incomplete or AI-generated.

Mitigation: Treat summaries as research data and check cited company disclosures for material claims.

Risk: Earnings analysis can be mistaken for personalized investment advice.

Mitigation: Use the output for research and education only; it is not a recommendation to buy or sell securities.

## Reference(s):

- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense](https://sentisense.ai)
- [ClawHub release page, version 1.5.0](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Quarter-organized Markdown earnings analysis with summaries, tables, and cited sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research summaries; no trades, purchases, or write operations.]

## Skill Version(s):

1.5.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
