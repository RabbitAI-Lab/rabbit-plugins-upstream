## Description:

Compare search interest, regional patterns, seasonality, and rising queries through Crawlora's Google Trends endpoints for topic-demand briefs, keyword comparisons, and trending-topic research with correctly interpreted relative indices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agent users use this skill to gather Google Trends comparisons, regional interest, seasonality signals, rising queries, and trending-topic details through Crawlora. It supports chart, table, or brief-style research outputs with explicit filters and relative-index interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected Google Trends queries and filters are sent to Crawlora under the user's Crawlora account.

Mitigation: Use only queries appropriate to share with Crawlora, and review Crawlora service terms and data handling expectations before installation.

Risk: The skill requires CRAWLORA_API_KEY for API access.

Mitigation: Keep CRAWLORA_API_KEY in the environment as instructed and avoid placing it in prompts, files, or shared command history.

Risk: Google Trends scores are relative and independently scaled requests are not directly comparable.

Mitigation: Compare terms in the same request when possible, label the axis as a relative index, and report filters, collection time, missing components, and any shared-anchor limitations.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown brief or chart/table with optional shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve terms, filters, collection time, source URL when available, missing components, and relative-index labeling.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
