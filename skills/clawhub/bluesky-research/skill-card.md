## Description:

Researches public Bluesky profiles, posts, follower and follows graphs, account search, and trending topics through the Crawlora API, returning JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use this skill to retrieve public Bluesky profile, post, thread, follower, follows, account-search, and trending-topic data without scraping the Bluesky app directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested handles, post URIs, search terms, trending-topic requests, and usage may be visible to Crawlora.

Mitigation: Use the skill only for public Bluesky lookups, avoid private or sensitive data in request parameters, and install it only when Crawlora is an acceptable third-party service.

Risk: The Crawlora API key could be exposed if it is pasted into prompts, commands, query parameters, or committed files.

Mitigation: Store the key only in the CRAWLORA_API_KEY environment variable and use the bundled helper, which avoids putting the key in command-line arguments.

Risk: Trending-topic responses are less stable than the other Bluesky endpoints and may change shape over time.

Mitigation: Treat trending-topic output as time-sensitive public data and verify downstream parsing before relying on a fixed response structure.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/bluesky-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests access public Bluesky data through Crawlora's API.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
