## Description:

TikTok videos, creators, sounds, and trend data for agents - content and creator research as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data teams, and marketing researchers use this skill to query TikTok videos, creator profiles, account search, video search, collections, and continuation results through Superagnt's API or optional MCP endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok queries and identifiers to Superagnt's API.

Mitigation: Use it only when the user is comfortable sharing those inputs with Superagnt, and avoid submitting sensitive or unnecessary identifiers.

Risk: SUPERAGNT_API_KEY is a paid API credential used to authorize requests.

Mitigation: Store it as an environment variable or secret, avoid logging it, and rotate it if exposure is suspected.

Risk: The optional MCP/OAuth setup uses an external provider path outside the reviewed artifact.

Mitigation: Enable the MCP path only after confirming the Superagnt endpoint and OAuth flow are acceptable for the deployment.

## Reference(s):

- [Superagnt TikTok Data Documentation](https://superagnt.com/r/ch-tiktok-data-docs)
- [TikTok Data MCP Server](https://mcp.superagnt.com/mcp/tiktok)
- [MCP Client Setup Prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub TikTok Data Listing](https://clawhub.ai/superagnt/skills/tiktok-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with curl commands and JSON tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and SUPERAGNT_API_KEY; API responses are structured JSON returned by Superagnt.]

## Skill Version(s):

2.0.6 (source: server release evidence, _meta.json, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
