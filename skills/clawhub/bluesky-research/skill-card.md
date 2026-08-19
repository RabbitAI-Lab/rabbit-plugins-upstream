## Description:

Researches Bluesky profiles, posts, follower/follows graphs, account search, and trending topics via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to research public Bluesky accounts, posts, reply threads, follower and following graphs, account search results, and trending topics through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper is broader than the Bluesky-only purpose and can send arbitrary requests through Crawlora.

Mitigation: Restrict usage to the documented Bluesky endpoints and review the helper before installation.

Risk: Queries or JSON request bodies could include private or sensitive data.

Mitigation: Use the skill only for public Bluesky research and avoid passing private data to Crawlora.

Risk: The skill requires a Crawlora API key.

Mitigation: Use a minimally scoped key where available and keep it in CRAWLORA_API_KEY rather than hardcoding or committing it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/bluesky-research)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY and operates on public Bluesky data endpoints.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
