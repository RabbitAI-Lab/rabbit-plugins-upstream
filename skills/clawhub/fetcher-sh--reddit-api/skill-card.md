## Description:

A Reddit API alternative on fetcher.sh for Reddit post, subreddit, user, feed, profile, and comment-tree retrieval through paid HTTP or MCP calls without Reddit OAuth app registration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Reddit content, inspect subreddit and user data, fetch posts with comments, and configure HTTP or MCP access for Reddit data pipelines, social listening, monitoring, and sentiment-analysis inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit search terms, usernames, subreddit names, post IDs, and Bearer keys may be sent to reddit.fetcher.sh.

Mitigation: Avoid submitting secrets, confidential internal terms, regulated personal data, or unnecessary Bearer credentials; scope and rotate keys where possible.

Risk: The skill describes prepaid credits and x402 pay-per-call flows that can trigger paid API usage.

Mitigation: Keep control over prepaid credits, wallet signing, and MCP tools that can make paid calls; monitor balances and review cost behavior before broad deployment.

Risk: The artifact notes no refunds on upstream failures because settlement precedes delivery.

Mitigation: Use test calls with low-risk queries before relying on the API for production workflows, and design callers to handle upstream or payment failures gracefully.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fetcher-sh/skills/reddit-api)
- [Server-Resolved GitHub Provenance](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/reddit-api)
- [Full Agent Setup](https://reddit.fetcher.sh/skill.md)
- [OpenAPI 3.1 Contract](https://reddit.fetcher.sh/openapi.json)
- [Condensed Catalog](https://reddit.fetcher.sh/llms.txt)
- [Reddit Fetcher Site](https://reddit.fetcher.sh)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with bash, JSON, endpoint, and URL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may result in paid third-party HTTP or MCP calls that return JSON Reddit data.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
