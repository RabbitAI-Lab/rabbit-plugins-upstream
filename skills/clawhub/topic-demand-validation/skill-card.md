## Description:

Compares search intent, trend movement, search results, and sampled public discussion to assess whether a topic or content idea merits further testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and product researchers use this skill to compare search and public discussion signals for a topic, product category, or content idea before choosing a focused validation test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Topics, search queries, and selected public post or video IDs are sent to Crawlora.

Mitigation: Use the skill only when external API use is acceptable; avoid confidential product ideas.

Risk: Successful API calls may be billable against a Crawlora account.

Mitigation: Start with a bounded sample and agree on a larger collection budget before expanding searches or pagination.

Risk: Search and social samples can be incomplete or misleading as evidence of demand.

Mitigation: Keep metrics separate, report coverage limits, and do not claim commercial validation from these signals alone.

## Reference(s):

- [Topic Demand Validation on ClawHub](https://clawhub.ai/crawlora-org/skills/topic-demand-validation)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown evidence brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scope and sampling limits, search and discussion findings, counter-signals, and a next validation step.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
