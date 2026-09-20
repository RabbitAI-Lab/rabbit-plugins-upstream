## Description:

Researches public Threads profiles, posts, replies, and search results through the Crawlora API and returns normalized JSON instead of scraping the Threads app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and social-listening teams use this skill to retrieve public Threads profile metadata, posts, replies, single-post details, and keyword search results through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Threads lookup inputs and the Crawlora API key are sent to Crawlora.

Mitigation: Install and use the skill only when that third-party API use is acceptable, keep the key in CRAWLORA_API_KEY, and do not hardcode or commit credentials.

Risk: The skill is designed for public Threads data and may be unsuitable for private or sensitive content.

Mitigation: Use it only for public profiles, posts, replies, and searches, and respect Threads' terms and applicable privacy requirements.

## Reference(s):

- [threads-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and restricts helper requests to documented public Threads endpoints.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
