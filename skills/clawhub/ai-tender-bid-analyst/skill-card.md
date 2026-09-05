## Description:

Analyzes tender, procurement, bidder, supplier, brand, price, company, and market data through natural-language workflows backed by the ZhiLiao BiaoXun API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business-development, procurement, sales, and market-analysis teams use this skill to find tender opportunities, analyze bid-award outcomes, profile companies, compare competitors, and summarize procurement market trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration can send a hashed MAC-derived device identifier to a remote service for deduplication.

Mitigation: Configure ZLBX_API_KEY before first use to bypass auto-registration, or require explicit user consent before any device-feature collection.

Risk: The skill can store an API key locally after automatic registration.

Mitigation: Review local credential storage before deployment and prefer managed environment-variable secrets for shared or enterprise systems.

Risk: Ambiguous company names can lead to analysis of the wrong legal entity.

Mitigation: Ask the agent to confirm company matches when names are ambiguous, especially before relying on company, competitor, or market-share analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-tender-bid-analyst)
- [Bid Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Auto-Registration Reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown answers with tables, concise analysis, and occasional JSON or HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a locally stored API key; some contact fields may be masked for free or trial accounts.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
