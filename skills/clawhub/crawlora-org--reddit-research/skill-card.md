## Description:

Researches public Reddit posts, comments, users, domains, trends, and lead-style searches through Crawlora API endpoints and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and community researchers use this skill to gather public Reddit discussion, sentiment, trends, user history, domain mentions, and post comment threads through Crawlora without scraping Reddit directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected Reddit search terms, public usernames, subreddit names, domains, post IDs, and the Crawlora API key to Crawlora.

Mitigation: Install only if this data sharing is acceptable, avoid sensitive private identifiers in queries, and keep CRAWLORA_API_KEY in the environment.

Risk: The endpoint catalog includes /reddit/leads for lead-generation and prospecting workflows.

Mitigation: Review use of /reddit/leads before deployment and avoid it when lead generation or prospecting is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/reddit-research)
- [Crawlora website](https://crawlora.net)
- [Reddit endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and documented Crawlora Reddit endpoints; API responses are normalized JSON.]

## Skill Version(s):

1.0.15 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
