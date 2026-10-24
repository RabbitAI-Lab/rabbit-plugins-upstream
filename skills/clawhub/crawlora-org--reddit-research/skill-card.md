## Description:

Researches public Reddit discussions, communities, user activity, and trends through Crawlora, with buying-intent post discovery only when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and other external users summarize public Reddit posts, comments, and trends for community or brand research. On explicit request, they can identify public posts expressing buying intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Reddit identifiers, requested post targets, and the API key are sent to Crawlora.

Mitigation: Use only with consent to that data sharing; avoid confidential investigations and private personal data, and protect the API key.

Risk: Buying-intent scoring of public posts could be misused to profile individuals.

Mitigation: Run lead discovery only on explicit request; describe scoring as post-level and avoid sensitive-trait inference or high-impact decisions.

## Reference(s):

- [Reddit endpoint reference](reference/endpoints.md)
- [ClawHub release](https://clawhub.ai/crawlora-org/skills/reddit-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and, when requested, scored lists of public posts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source results are public Reddit data; engagement estimates and large comment threads may be incomplete.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
