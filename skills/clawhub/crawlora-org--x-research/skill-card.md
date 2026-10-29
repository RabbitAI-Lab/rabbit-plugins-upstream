## Description:

Retrieves public X profiles, recent profile posts, and individual post details through Crawlora as JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and developers use this skill to inspect public X account profiles, recent posts, and individual post engagement without browser automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The requested public X handles or post IDs and the Crawlora API key are sent to Crawlora.

Mitigation: Use only for public data you are comfortable sharing with Crawlora; keep the API key in CRAWLORA_API_KEY and out of chats, logs, URLs, and committed files.

Risk: Recent-post results cover only the first public profile page, so they may not represent a full posting history.

Mitigation: Treat the returned posts as a limited snapshot, not a complete timeline.

## Reference(s):

- [x-research endpoint reference](reference/endpoints.md)
- [x-research on ClawHub](https://clawhub.ai/crawlora-org/skills/x-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public profile details, recent posts, or a post's text and visible engagement; profile posts are limited to the first public page.]

## Skill Version(s):

1.0.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
