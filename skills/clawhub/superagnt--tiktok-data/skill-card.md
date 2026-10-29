## Description:

TikTok videos, creators, sounds, and trend data for agents — content and creator research as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and research teams use the skill to retrieve TikTok video and creator details, collect account videos, and search accounts or videos for content and trend research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service receives the API credential with requests.

Mitigation: Keep the API key private and provide it through the documented environment variable.

Risk: Research requests may consume account credits.

Mitigation: Review expected costs and check the account balance before running requests.

Risk: The optional MCP connection may request permissions, and example commands may need correction before use.

Mitigation: Review the MCP permissions and correct the example commands before authorizing or running them.

## Reference(s):

- [TikTok Data documentation](https://superagnt.com/r/ch-tiktok-data-docs)
- [TikTok Data scoped MCP server](https://mcp.superagnt.com/mcp/tiktok)
- [TikTok Data installation guide](https://www.superagnt.com/install?facet=tiktok)
- [API key setup](https://superagnt.com/r/ch-tiktok-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/tiktok-data)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Guidance]

**Output Format:** [Structured JSON results with Markdown setup and request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested TikTok data and the connected account's access and credits.]

## Skill Version(s):

2.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
