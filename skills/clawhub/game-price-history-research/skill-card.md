## Description:

Research observed Steam price history and compare current game editions or PlayStation offers using Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and game buyers use this skill to prepare dated Steam discount briefs and compare current game editions and PlayStation offers while preserving currency, region, subscription, and observation context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Game lookup terms and related request metadata are sent to Crawlora using an API key.

Mitigation: Use the skill only when comfortable sharing these details with Crawlora, and protect the API key.

Risk: Broad queries can consume Crawlora credits.

Mitigation: Bound page sizes, date ranges, and calls to the research scope and credit budget.

Risk: Mismatched editions, regions, currencies, or subscription labels can make price comparisons misleading.

Mitigation: Verify each offer's edition, region, currency, and subscription terms, and distinguish stored observations from current prices.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/game-price-history-research)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Dated price research brief or offer comparison in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source dates, observed coverage, currency, edition, region, and subscription qualifications.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
