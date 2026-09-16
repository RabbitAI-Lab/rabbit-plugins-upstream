## Description:

Researches Bluesky profiles, posts, follower/follows graphs, account search, and trending topics via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and social media researchers use this skill to retrieve public Bluesky profile, post, thread, follower/following, account-search, and trending-topic data through Crawlora as normalized JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bluesky lookup inputs such as handles, post URIs, and search terms are sent to Crawlora's API.

Mitigation: Submit only public, non-sensitive lookup inputs and avoid placing private information in search queries.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or pasted into command-line arguments.

Mitigation: Store CRAWLORA_API_KEY in environment or secret storage; the helper reads it from the environment and keeps it out of request arguments.

Risk: API use may consume Crawlora credits, and the trending-topics response is identified as a less stable surface.

Mitigation: Check Crawlora quota before broad collection, page list endpoints deliberately, and handle trending-topic schema changes defensively.

## Reference(s):

- [Bluesky endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; queries public Bluesky data through Crawlora and may consume Crawlora credits.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
