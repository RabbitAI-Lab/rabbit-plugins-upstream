## Description:

Compare relocation budgets across cities using itemized cost-of-living prices and optional US housing-market context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

People comparing a move between cities can estimate comparable household budgets, rent differences, and, for US locations, housing-market context while tracking assumptions and missing expenses.

### Deployment Geography for Use:

Global; housing-market context is limited to the United States.

## Known Risks and Mitigations:

Risk: City and housing-market queries and the API key are sent to Crawlora.

Mitigation: Keep the key in an environment variable, avoid sensitive personal details in queries, and use the service only if comfortable sharing these details.

Risk: Broad comparisons can consume API credits.

Mitigation: Limit requested cities, pages, and calls; monitor credit use.

Risk: Crowdsourced prices, ambiguous currencies, and missing expenses can distort relocation estimates.

Mitigation: Verify currency and dated conversion rates, compare the same basket and rent basis, and label excluded costs and source freshness.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/relocation-cost-comparison)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown comparison with itemized budget tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source dates, currency and household assumptions, coverage limits, and excluded costs.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
