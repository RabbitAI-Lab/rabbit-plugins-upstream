## Description:

Compare search interest, regional patterns, seasonality, and rising queries through Crawlora's Google Trends endpoints for topic-demand briefs, keyword comparisons, and trending-topic research with correctly interpreted relative indices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketers, and analysts use this skill to query Crawlora's Google Trends endpoints and produce chart, table, or brief-style comparisons by term, geography, time range, and search property.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the Crawlora API key and Trends request data to Crawlora.

Mitigation: Use a dedicated or revocable API key, avoid sensitive private query terms unless intended, and keep normal network-access controls around the skill.

Risk: Google Trends values are normalized and sampled, so independently scaled requests or missing data can be misread as absolute demand.

Mitigation: Compare terms in the same request when possible, label values as relative indices, preserve missing-data flags, and describe sampling or anchor-method limits.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/google-trends-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with tables, charts, JSON excerpts, and inline shell commands as requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should label Google Trends values as relative indices and include terms, filters, collection time, interpretation, and missing components when available.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
