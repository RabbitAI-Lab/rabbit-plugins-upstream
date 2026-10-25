## Description:

TikTok videos, creators, sounds, and trend data for agents — content and creator research as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and research teams can use this skill to retrieve TikTok video and creator details, account videos, collections, and search results for content research, trend monitoring, and social listening workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if shared in prompts, command output, or logs.

Mitigation: Configure SUPERAGNT_API_KEY locally and avoid printing or sharing its value.

Risk: API requests may incur provider charges, and queries may disclose research interests to the service.

Mitigation: Check provider billing and send only queries appropriate to share with the service.

Risk: The documented curl examples need correction, and the optional hosted MCP runtime was not verified.

Mitigation: Review and correct commands before running them; inspect requested permissions and behavior before connecting to the MCP server.

## Reference(s):

- [TikTok Data documentation](https://superagnt.com/r/ch-tiktok-data-docs)
- [API key setup](https://superagnt.com/r/ch-tiktok-data-key)
- [TikTok Data API endpoint](https://api.superagnt.com/v1/data/tiktok)
- [Optional TikTok Data MCP server](https://mcp.superagnt.com/mcp/tiktok)
- [Client installation guide](https://www.superagnt.com/install?facet=tiktok)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/tiktok-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [JSON data from TikTok endpoints, with Markdown setup guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Response fields depend on the selected video, creator, collection, or search endpoint.]

## Skill Version(s):

2.0.8 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
