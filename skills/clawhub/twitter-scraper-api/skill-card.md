## Description:

Search X, read tweets and their replies and retweeters, pull user profiles and their tweets, replies, media, followers, and followings, and get trending topics as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to search X, retrieve tweet, profile, and social-graph data, monitor brands or campaigns, and build RAG or sentiment workflows with structured JSON from Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests and the Scavio API key are sent to a third-party service.

Mitigation: Install and use the skill only when that third-party data flow is acceptable; keep SCAVIO_API_KEY in an environment variable or secret store.

Risk: Follower, following, profile, and tweet collection can create privacy or policy risk even when the data is public.

Mitigation: Use the skill only for authorized, policy-compliant X research; avoid unnecessary bulk social-graph collection and do not store or share data without a clear need and lawful basis.

Risk: Paginating across many pages can consume API credits quickly.

Mitigation: Inform the user before broad pagination and monitor credits_remaining in API responses.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/twitter-scraper-api)
- [Scavio X API documentation](https://scavio.dev/docs/x-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with bash and Python code blocks plus structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses use JSON envelopes with pagination cursors and credit counters.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
