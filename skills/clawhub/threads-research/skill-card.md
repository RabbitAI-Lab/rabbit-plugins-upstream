## Description:

Researches public Threads (Meta) profiles, posts, replies, and search results via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Threads profiles, posts, replies, and keyword search results through Crawlora without scraping the Threads app.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included Crawlora helper can call non-Threads Crawlora paths beyond the documented Threads endpoints.

Mitigation: Restrict or replace the helper so agents can call only the documented Threads endpoints.

Risk: The skill requires access to a Crawlora API key.

Mitigation: Provide the key through CRAWLORA_API_KEY only, avoid committing it, and monitor Crawlora usage and credits.

Risk: Public Threads data may be incomplete because search has no continuation cursor and reply pagination can be unavailable.

Mitigation: Use results as public-web research context, cite source URLs where possible, and avoid treating partial results as complete coverage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/threads-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; covers public Threads data only; search results are first page only and some reply pagination may be unavailable.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
