## Description:

Search X, read tweets and their replies and retweeters, pull user profiles and their tweets, replies, media, followers, and followings, and get trending topics as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve structured X data for tweet search, profile lookup, social graph analysis, trending-topic discovery, brand monitoring, sentiment workflows, and RAG pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: X lookup requests and returned social data are sent through Scavio using the user's API key.

Mitigation: Use the skill only for legitimate, user-authorized purposes and avoid sending unnecessary or sensitive lookup requests.

Risk: Follower, following, profile, retweeter, and pagination workflows can increase privacy exposure and credit usage.

Mitigation: Limit pagination to the data needed for the task and inform users before retrieving many pages.

Risk: The optional LangChain integration adds a package dependency to the agent environment.

Mitigation: Install optional dependencies in an isolated environment before use.

## Reference(s):

- [Scavio X API documentation](https://scavio.dev/docs/x-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitter-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitter-scraper-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/twitter-scraper-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON response shapes, Python examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; endpoints return structured JSON and paginated cursors where available.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
