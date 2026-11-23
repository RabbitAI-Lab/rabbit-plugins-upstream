## Description:

Research public TikTok profiles, videos, comments, hashtags, search results, trending feeds, and Creative Center signals through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and developers use this skill to investigate public TikTok content and trends, verify profiles or videos, and compare bounded samples with source links and retrieval context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and filters are sent to Crawlora with the user's API key.

Mitigation: Use the skill only if this disclosure is acceptable; keep the key in the environment and out of shared outputs.

Risk: Public TikTok results are sampled and time-dependent and can be mistaken for complete or current coverage.

Mitigation: Report retrieval time, filters, sample size, source links, and any unavailable or partial coverage.

## Reference(s):

- [TikTok endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/tiktok-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with source URLs or stable IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Include retrieval time, filters, sample size, and qualifications for partial or time-dependent results.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
