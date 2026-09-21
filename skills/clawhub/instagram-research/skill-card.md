## Description:

Researches Instagram profiles, posts, and Reels via the Crawlora API, returning clean JSON for public Instagram profile, post, and Reels lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to retrieve normalized public Instagram profile, post, and Reels data for influencer vetting, competitor social audits, brand monitoring, and post-level engagement checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Instagram lookup requests to Crawlora as a third-party service.

Mitigation: Install and use it only when third-party processing by Crawlora is acceptable for the intended workflow.

Risk: The helper requires a Crawlora API key.

Mitigation: Store CRAWLORA_API_KEY in the environment, avoid hardcoding or committing it, and keep it out of query parameters.

Risk: Instagram lookups are limited to public data and must respect applicable platform terms.

Mitigation: Use the skill only for public profiles, posts, and Reels, and verify that the intended use complies with relevant terms and policies.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/instagram-research)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns public Instagram data through Crawlora.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
