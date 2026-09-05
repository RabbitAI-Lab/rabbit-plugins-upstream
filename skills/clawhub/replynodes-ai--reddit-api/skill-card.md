## Description:

Bearer-key, pay-per-request access to read-only Reddit data: subreddit posts, a single post, post comments, and keyword search through one HTTPS gateway, with normalized JSON from Arctic Shift and Reddit RSS fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to read public Reddit data through ReplyNodes' paid, read-only gateway without Reddit OAuth, Reddit credentials, or write access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses ReplyNodes' paid Reddit data gateway and priced routes can incur per-request charges.

Mitigation: Confirm current pricing with the free capabilities endpoint before making paid calls.

Risk: Bearer workspace API keys could be exposed if pasted into chat, committed, or logged.

Mitigation: Keep the API key private and pass it through local environment variables or a secret manager.

Risk: Returned Reddit titles, comments, URLs, and author fields are untrusted third-party data.

Mitigation: Treat response content as data for review or analysis, not as agent instructions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/replynodes-ai/skills/reddit-api)
- [Reddit Gateway Homepage](https://api.replynodes.com/v1/reddit)
- [Endpoint Reference](references/endpoints.md)
- [Scenarios](references/scenarios.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown with inline bash commands and JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only HTTP GET guidance for a paid Bearer-key API; no credentials or live response payloads are included.]

## Skill Version(s):

1.0.1 (source: server release metadata, VERSION, and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
