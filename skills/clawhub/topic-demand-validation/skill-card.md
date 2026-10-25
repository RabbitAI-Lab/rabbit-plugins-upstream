## Description:

Validate a topic, product category, or content idea by comparing autocomplete intent, Google Trends movement, search-result competition, and a bounded sample of Reddit, TikTok, or YouTube discussion. Use for questions like “is there demand for this?”, “what topic should we test next?”, or “what are people searching and discussing?”; use brand-mention-research for a known entity’s mentions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and product or content teams use this skill to assess whether a topic merits further exploration by comparing search phrasing, relative interest, search competition, and a bounded public discussion sample. It supports a next validation step while keeping those signals separate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms may disclose confidential names or customer details to Crawlora and the relevant search services.

Mitigation: Use search terms that are safe to share; remove confidential details and provide your own Crawlora API key.

Risk: Successful API calls may incur charges.

Mitigation: Keep collection bounded and account for billable requests before expanding searches or paging.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/crawlora-org/skills/topic-demand-validation)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Crawlora API site](https://crawlora.net)
- [Endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Compact Markdown evidence brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates autocomplete, Trends, search-result, and social-sample evidence; includes scope, synthesis, and a next validation step. Does not establish sales, market size, or future growth.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
