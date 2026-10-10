## Description:

Research observed Steam price history and compare current game editions or PlayStation offers using Crawlora, preserving currency, edition, region, and observation dates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Players, shoppers, and researchers use this skill to prepare dated Steam discount briefs, analyze observed price ranges, and compare current game editions or PlayStation offers without conflating regions, currencies, or subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Game queries and the Crawlora API key are sent to Crawlora when retrieving prices.

Mitigation: Use a key scoped to Crawlora, avoid unnecessary query details, and revoke or rotate the key when no longer needed.

Risk: Missing observations, regional differences, or mismatched editions can make price comparisons misleading.

Mitigation: Report observed date coverage and gaps; compare matching editions and currencies, and distinguish historical Steam observations from current regional offers.

## Reference(s):

- [Crawlora game-price endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/game-price-history-research)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown price-history briefs and offer comparisons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dated observations, currency, edition and region distinctions, and history-coverage caveats.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
