## Description:

Compare city relocation budgets with Crawlora itemized Numbeo costs and optional US housing-market context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

People planning a move use this skill to compare itemized household expenses and rent across cities under stated assumptions, with optional US home-purchase market context.

### Deployment Geography for Use:

Global for cost-of-living comparisons; housing-market context covers the United States only.

## Known Risks and Mitigations:

Risk: City, housing, and budget queries are sent to Crawlora.

Mitigation: Share only the query details needed for the comparison and confirm the user is comfortable with external API use.

Risk: A Crawlora API key is required and large searches may use paid credits.

Mitigation: Keep the key private, bound page counts and calls, and review credit usage before broad searches.

Risk: Crowdsourced prices and mismatched currencies or housing assumptions can mislead relocation decisions.

Mitigation: Show source dates and provisional assumptions, verify exchange rates, and keep unmatched costs or missing expenses explicitly excluded.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/relocation-cost-comparison)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Itemized monthly budgets with source dates, assumptions, excluded expenses, and coverage limits.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
