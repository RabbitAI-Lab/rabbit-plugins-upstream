## Description:

Researches public social-media profiles, posts, engagement, platform search results, trending topics, and social-listening signals across supported platforms through the Crawlora API, returning JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and marketing teams use this skill to query public social-media profiles, posts, searches, trends, and engagement data for social listening, competitor review, influencer vetting, and brand research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search terms, usernames, IDs, listing filters, and a Crawlora API key to Crawlora.

Mitigation: Use only data and credentials appropriate for Crawlora processing, and keep the API key in CRAWLORA_API_KEY rather than prompts, query parameters, or committed files.

Risk: Prospecting or leads-oriented endpoints could be misused for spam, harassment, or sensitive-person targeting.

Mitigation: Use prospecting features only for legitimate, consent-aware public research and avoid sensitive-person targeting.

Risk: Platform coverage and result completeness vary by endpoint and upstream public surfaces.

Mitigation: Check the endpoint reference before relying on a platform surface, and treat paginated or limited results as partial until cursors or documented limits are handled.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/social-media-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API for public-data endpoints.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
