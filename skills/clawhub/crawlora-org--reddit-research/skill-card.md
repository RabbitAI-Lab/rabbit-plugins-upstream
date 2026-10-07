## Description:

Researches public Reddit discussions, communities, user activity, and trends through Crawlora, with buying-intent lead discovery only when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and other users can examine public Reddit posts, comments, communities, and trends for community insights or sentiment. They can also request buying-intent discovery from public posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and investigation terms are sent to Crawlora, a third-party service.

Mitigation: Do not submit confidential, sensitive, or regulated terms unless you intend to share them with Crawlora.

Risk: Exposure of the Crawlora API credential could allow unauthorized use.

Mitigation: Protect CRAWLORA_API_KEY as a secret; do not publish or include it in queries.

Risk: Buying-intent scores could be misused to profile people or support high-impact decisions.

Mitigation: Use lead discovery only on explicit request, describe scores as post-level signals, and do not infer sensitive traits or rank people for high-impact decisions.

## Reference(s):

- [Reddit Research on ClawHub](https://clawhub.ai/crawlora-org/skills/reddit-research)
- [Reddit endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown research summaries or structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public Reddit data; engagement metrics can be approximate and some threads incomplete.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
