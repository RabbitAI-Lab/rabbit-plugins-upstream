## Description:

Researches Bluesky profiles, posts, follower and follows graphs, account search, and trending topics via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve normalized JSON for public Bluesky profiles, author feeds, post threads, follower and follows graphs, account search, and trending topics through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authenticated Crawlora helper can send the API key outside the documented endpoint if CRAWLORA_API_BASE is changed.

Mitigation: Use the skill only in an environment you control, leave CRAWLORA_API_BASE unset unless the destination is trusted, and prefer a version that hardcodes or allowlists the documented Bluesky endpoints.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/bluesky-research)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown usage guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; list endpoints are cursor-paginated.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
