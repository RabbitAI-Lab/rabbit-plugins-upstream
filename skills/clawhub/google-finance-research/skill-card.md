## Description:

Retrieves source-attributed Google Finance quotes, company information, charts, financials, news, and market snapshots through Crawlora for market research and comparisons without trading or portfolio actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, developers, and other users can gather sourced market snapshots and compare instruments or reporting periods for research briefs. The skill does not provide personalized trading decisions or place orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup terms and instrument identifiers are shared with Crawlora using the user's API key.

Mitigation: Use only if comfortable sharing those queries with Crawlora; do not include secrets, private portfolio details, or confidential business context.

Risk: Ambiguous instruments or data with unknown freshness can mislead financial comparisons.

Mitigation: Verify exchange-qualified identifiers, show source and collection times separately, and mark unknown freshness or missing metrics rather than assuming live or complete data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/google-finance-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Google Finance endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown market brief with quote or period comparison tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source attribution, available timestamps, instrument identifiers, units, and explicit missing or uncertain values.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
