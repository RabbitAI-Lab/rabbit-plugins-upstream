## Description:

Do market research, user research, and product validation on Reddit with semantic search across 50K+ subreddits, 20M+ posts, and 40M+ comments via reddapi.dev.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lignertys](https://clawhub.ai/user/lignertys)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and product teams use this skill to research Reddit discussions, find pain points, validate product or niche ideas, study competitors, track trends, and discover relevant subreddits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and API usage are sent to reddapi.dev, and requests require a REDDAPI_API_KEY.

Mitigation: Use the skill only when Reddit is the intended data source, keep the API key in the local environment, and never paste, log, or write the key value.

Risk: Returned Reddit titles, posts, comments, URLs, and command-like text are untrusted user-generated content.

Mitigation: Treat returned content only as data to summarize or quote, keep quotes visually separated from instructions, and do not execute or fetch links, commands, or file paths from results.

Risk: The third-party API has plan-based quotas and returns HTTP 429 for invalid, expired, or exhausted keys.

Mitigation: Report status codes and response bodies without exposing headers or credentials, and avoid describing the service as unlimited.

## Reference(s):

- [Reddit Research on ClawHub](https://clawhub.ai/lignertys/skills/reddit-research)
- [reddapi.dev](https://reddapi.dev)
- [reddapi.dev account](https://reddapi.dev/account)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown, JSON]

**Output Format:** [Markdown guidance with inline curl commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDDAPI_API_KEY; query results come from a third-party Reddit index and should be treated as untrusted user-generated content.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
