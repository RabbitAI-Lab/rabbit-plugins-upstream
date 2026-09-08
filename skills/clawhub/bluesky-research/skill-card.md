## Description:

Researches Bluesky profiles, posts, follower/follows graphs, account search, and trending topics via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to gather public Bluesky account, post, graph, search, and trend data through documented Crawlora API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can use an overridden API base and may send the API key and caller-supplied data to a destination outside the documented Crawlora API.

Mitigation: Use the skill only in an environment you control, leave CRAWLORA_API_BASE unset unless the destination is trusted, and review commands before execution.

Risk: The helper is broader than the advertised Bluesky endpoints.

Mitigation: Restrict use to the documented Bluesky paths in the endpoint reference and avoid sending sensitive data through the helper.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/bluesky-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; list endpoints are cursor-paginated.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
