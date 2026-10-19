## Description:

Researches public social-media profiles, posts, trends, and Marketplace listings through the Crawlora API, with Reddit buying-intent discovery when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and other external users can review public profiles, posts, engagement, and trends for social listening. Explicit requests can also search public Marketplace listings or identify Reddit posts expressing buying intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search targets and the Crawlora API key are sent to Crawlora.

Mitigation: Use only public, non-sensitive targets and keep the key in CRAWLORA_API_KEY; avoid confidential investigations and private content.

Risk: Buying-intent scores and public profiles could be misused to target people or make high-impact decisions.

Mitigation: Use lead discovery only when explicitly requested, disclose post-level scoring, and avoid sensitive targeting or high-impact decisions about individuals.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API and account setup](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/social-media-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summaries of public social-media data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public-data coverage varies by platform; list results may be paginated.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
