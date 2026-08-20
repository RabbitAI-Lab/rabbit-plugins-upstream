## Description:

Queries Jiimore and LinkFox Amazon niche-market data for a reference ASIN, returning market-segment metrics such as demand, search and sales volume, brand concentration, CPC, launch success, and return rates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, analysts, and agent users use this skill to evaluate the Amazon niche segments associated with a known ASIN. It supports competitive intensity, brand concentration, new-product opportunity, advertising cost, and demand-score analysis for US, JP, and DE marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ASIN queries, API keys, session metadata, and onboarding or billing data may be sent to LinkFox services when the skill is used.

Mitigation: Install only when this data sharing is acceptable, keep API keys secret, and avoid printing or sharing credential-bearing outputs.

Risk: Endpoint override environment variables can redirect requests away from the default LinkFox services.

Mitigation: Use endpoint overrides only with fully trusted destinations and review the active environment before running the scripts.

Risk: The skill can guide phone login, API-key creation, credit purchase, and payment QR-code flows.

Mitigation: Require explicit user approval before login, purchasing credits, querying orders, or sending feedback.

Risk: Full API responses are stored locally in LinkFox session data and cached for reuse.

Mitigation: Review local LinkFox storage paths, clean retained data when no longer needed, and use the non-inline summary path for large responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-info-by-asin)
- [API reference](references/api.md)
- [Authentication and credit onboarding](references/onboarding.md)
- [LinkFox skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses to local LinkFox session data and may print complete or summarized JSON depending on response size.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
