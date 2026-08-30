## Description:

Post to X, LinkedIn, Facebook, TikTok, and Instagram through the Claw Post API, comment on Reddit threads through the user's browser, and post to Facebook groups the user already belongs to.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daydreamnationtechlabs](https://clawhub.ai/user/daydreamnationtechlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to publish social posts, upload media, poll publishing jobs, and submit Reddit comments through a paired Claw Post browser extension and API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish posts and Reddit comments through real logged-in browser sessions.

Mitigation: Require explicit user confirmation for every post, comment, upload, and target destination before submitting a job.

Risk: Facebook group automation may be misused if an agent searches for groups, joins them, and posts without human intent.

Mitigation: Restrict use to Facebook group URLs supplied by the user and do not permit automated search-to-join-to-post workflows.

Risk: The required Claw Post API key authorizes actions for a single account.

Mitigation: Store CLAWPOST_API_KEY in the agent's secret store or environment, rotate it from the dashboard when needed, and never paste live keys into skill files.

## Reference(s):

- [Claw Post API documentation](https://clawpost.net/api-docs)
- [Claw Post MCP endpoint](https://mcp.clawpost.net/mcp)
- [ClawHub skill listing](https://clawhub.ai/daydreamnationtechlabs/skills/clawpost)
- [ClawHub publisher profile](https://clawhub.ai/user/daydreamnationtechlabs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API examples and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CLAWPOST_API_KEY for REST API use, or MCP OAuth for compatible MCP clients.]

## Skill Version(s):

2.2.0 (source: target metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
