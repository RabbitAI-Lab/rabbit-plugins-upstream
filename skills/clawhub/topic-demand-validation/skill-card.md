## Description:

Helps assess demand for a topic, product category, or content idea using search suggestions, relative search trends, search results, and sampled public discussions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Content strategists, product teams, and researchers use this skill to assess whether a topic merits further testing by comparing search intent, relative interest, competing results, and a bounded sample of public discussion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Topic queries and an API key are sent to Crawlora's external service.

Mitigation: Limit searches to non-sensitive public topics, protect the API key, and review the service's terms and privacy posture before use.

Risk: Successful API calls may incur charges.

Mitigation: Set an API budget and agree on wider collection before expanding searches or pagination.

Risk: Relative search indices and sampled discussions can be mistaken for market size or commercial validation.

Mitigation: Keep signals distinct, describe sampling limits, and validate business demand through a separate test.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/topic-demand-validation)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown evidence brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scope, source coverage, distinct search and discussion signals, limitations, and a recommended next validation step.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
