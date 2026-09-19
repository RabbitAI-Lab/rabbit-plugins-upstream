## Description:

Researches social-media profiles, posts, and engagement across Instagram, TikTok, Threads, Bluesky, X, Pinterest, LinkedIn, Facebook, Reddit, Bilibili, and Patreon via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public social-media profiles, posts, engagement, platform searches, trending topics, and competitor or brand-mention signals through Crawlora instead of scraping individual apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-profile targets, post IDs, marketplace locations, and search terms are sent to Crawlora under the user's API key.

Mitigation: Use only public targets approved for third-party processing, and avoid secrets, regulated identifiers, private content, and sensitive internal investigations unless policy allows Crawlora as a processor.

Risk: The helper requires a Crawlora API key to call third-party endpoints.

Mitigation: Provide the key through CRAWLORA_API_KEY, do not hardcode or commit it, and review command inputs before execution.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/social-media-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET endpoints for public social-media data.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
