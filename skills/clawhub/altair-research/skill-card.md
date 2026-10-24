## Description:

Retrieves recent AI-generated research summaries and model decisions for covered U.S. stocks and ETFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[altair-world](https://clawhub.ai/user/altair-world)

### License/Terms of Use:

MIT-0

## Use Case:

Users seeking market research can review recent AI-generated outlooks, ratings, price targets, confidence levels, and areas of model disagreement for covered U.S. stocks and ETFs. Treat results as informational only; they are not investment advice or a basis for trading decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries are sent to Altair, and a custom MCP URL changes the service receiving them.

Mitigation: Leave ALTAIR_MCP_URL unset unless you trust the replacement server.

Risk: AI-generated research may be outdated or contain errors and could be mistaken for investment advice.

Mitigation: Check report dates and underlying sources; do not use reports as investment advice or to make trading decisions.

## Reference(s):

- [Altair TradingAgents research](https://altairworld.com/TradingAgents/)
- [Altair free public MCP endpoint](https://altairworld.com/mcp/free)
- [ClawHub skill page](https://clawhub.ai/altair-world/skills/altair-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown with ticker summaries, model comparison tables, and report sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes analysis dates and a financial-information disclaimer; report freshness varies by ticker.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
