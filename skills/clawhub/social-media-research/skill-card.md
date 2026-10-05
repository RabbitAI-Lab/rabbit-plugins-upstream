## Description:

Researches public social-media profiles, posts, engagement, searches, and trends across eleven platforms through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, marketers, and other users research public profiles, posts, engagement, brand mentions, competitors, and trending topics across social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public profile handles and search terms are sent to Crawlora when researching social platforms.

Mitigation: Submit only public-data queries you are comfortable sharing with Crawlora.

Risk: The Crawlora API key could be exposed if copied into prompts, URLs, or shared files.

Mitigation: Keep the key in CRAWLORA_API_KEY and do not hardcode or commit it.

Risk: Some cataloged endpoints cover marketing or marketplace research rather than social posts.

Mitigation: Check the endpoint reference and distinguish listings from social-media results.

## Reference(s):

- [Social media endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, JSON data, Guidance]

**Output Format:** [JSON API results and concise Markdown research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public data only; platform coverage varies and list results may require pagination.]

## Skill Version(s):

1.0.20 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
