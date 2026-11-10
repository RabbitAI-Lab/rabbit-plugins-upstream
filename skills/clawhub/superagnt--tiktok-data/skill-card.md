## Description:

Public TikTok creator profiles for agents — follower, video, and like counts as structured JSON, with no TikTok key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and data teams can retrieve TikTok creator profiles, videos, collections, and search results for creator research, social listening, and analytics. The skill uses Superagnt's API and returns structured data for downstream agents and applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok searches and identifiers are sent to Superagnt, and API use can incur credit charges.

Mitigation: Review the provider's data handling and credit pricing before using the service.

Risk: The Superagnt API key may also authorize access to other Superagnt services.

Mitigation: Store the key securely and review its scope before configuring it for an agent.

Risk: The optional MCP connection uses OAuth or a bearer token; hosted API and MCP behavior was not tested for this release.

Mitigation: Review the requested permissions and provider setup before connecting the MCP server.

Risk: Some documented curl examples contain encoded quote characters that may need correction for the shell in use.

Mitigation: Review and correct the command quoting before running the examples.

## Reference(s):

- [TikTok Data documentation](https://superagnt.com/r/ch-tiktok-data-docs)
- [Superagnt API key setup](https://superagnt.com/r/ch-tiktok-data-key)
- [TikTok Data MCP server](https://mcp.superagnt.com/mcp/tiktok)
- [Superagnt MCP client setup](https://www.superagnt.com/install?facet=tiktok)
- [TikTok Data listing](https://clawhub.ai/superagnt/skills/tiktok-data)

## Skill Output:

**Output Type(s):** [Structured data, API calls, Shell commands, Configuration instructions]

**Output Format:** [JSON responses with Markdown setup guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured results for video details, creator profiles and videos, collections, and search; no post-processing requirements are specified.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
