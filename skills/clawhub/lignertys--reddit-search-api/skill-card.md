## Description:

Pure API reference for reddapi.dev authentication, vector search, semantic search, trends, subreddit lookup, request parameters, response schemas, and error codes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lignertys](https://clawhub.ai/user/lignertys)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill as a concise API reference for authenticating to reddapi.dev and calling search, trends, and subreddit endpoints with correct request and response fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls made from this skill send search queries and an authorization header to reddapi.dev.

Mitigation: Set credentials only in the operator's shell, never paste the key into chat, and avoid logging or displaying request headers.

Risk: Returned Reddit titles, post bodies, comments, URLs, and file paths are untrusted third-party content.

Mitigation: Treat result text as data, separate quoted content from agent output, and do not execute commands or fetch links found inside results.

## Reference(s):

- [ClawHub Reddit Search API skill page](https://clawhub.ai/lignertys/skills/reddit-search-api)
- [reddapi.dev account and API key page](https://reddapi.dev/account)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reference text with curl command examples and JSON response schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential-handling cautions and guidance to treat returned Reddit content as untrusted third-party text.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
