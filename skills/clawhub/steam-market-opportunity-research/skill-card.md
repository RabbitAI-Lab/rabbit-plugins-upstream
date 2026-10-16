## Description:

Evaluate Steam game niches using Crawlora's game catalog, chart and player-count history, live pricing, reviews, and release news for evidence-backed opportunity research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers, publishers, and market researchers use this skill to compare Steam titles, assess activity and pricing, identify review themes, and develop testable game opportunity hypotheses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and the Crawlora API key are sent to Crawlora's API.

Mitigation: Keep the key in the environment, avoid secrets in query values, and use the skill only if this data sharing is acceptable.

Risk: Large searches may consume billable Crawlora credits.

Mitigation: Review Crawlora's billing and credit behavior before running large searches.

Risk: Estimated owners and sampled player counts can be mistaken for audited sales, revenue, or retention.

Mitigation: Label estimates and observation windows, and validate opportunity hypotheses with additional evidence.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/steam-market-opportunity-research)
- [Crawlora](https://crawlora.net)
- [Steam endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown opportunity brief with comparison tables and supporting evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observed metrics, third-party estimates, and commercial hypotheses.]

## Skill Version(s):

1.0.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
