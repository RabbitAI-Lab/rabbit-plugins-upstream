## Description:

Researches public Threads profiles, posts, replies, and search results through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to research public Threads profiles, posts, replies, and keyword search results without scraping the Threads app directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public Threads lookup queries and the Crawlora API key to Crawlora.

Mitigation: Use only if this data sharing is acceptable, store the API key in CRAWLORA_API_KEY, and treat the key like a billing credential.

Risk: The helper has a minor overbroad POST capability.

Mitigation: Avoid POST unless Crawlora documents a specific POST-capable Threads endpoint for this skill.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/threads-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands for API calls that return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API for public Threads data.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
