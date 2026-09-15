## Description:

Compare search interest, regional patterns, seasonality, and rising queries through Crawlora's Google Trends endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and marketing analysts use this skill to collect and interpret Google Trends data for topic-demand briefs, keyword comparisons, seasonality checks, and trending-topic research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, request bodies, and the Crawlora API key are sent to Crawlora's API.

Mitigation: Use the skill only for topics acceptable to send to Crawlora, keep CRAWLORA_API_KEY private, and avoid sensitive internal research unless approved for the use case.

Risk: Google Trends values are relative indices and can be misleading when independently scaled requests are compared directly.

Mitigation: Compare terms in the same request when possible, label charts as relative indices, preserve missing-data flags, and state sampling or anchoring limits.

Risk: Rapid retries or broad concurrent widget calls can amplify throttling or partial-result failures.

Mitigation: Honor Retry-After on 429 or 503 responses, use bounded retries, and report missing components instead of fabricating completed comparisons.

## Reference(s):

- [Crawlora skill page](https://clawhub.ai/crawlora-org/skills/google-trends-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve query filters, collection time, missing-data flags, and relative-index labeling.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
