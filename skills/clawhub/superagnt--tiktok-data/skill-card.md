## Description:

Public TikTok creator profiles for agents — follower, video, and like counts as structured JSON, with no TikTok key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research or marketing teams can use the skill to retrieve TikTok creator profiles, videos, collections, and account or video search results for social listening and creator research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that the brief profile-statistics description does not fully convey the documented video, collection, and search capabilities.

Mitigation: Review the documented endpoint scope and decide whether these additional capabilities fit the intended use.

Risk: Using the documented API sends an API key to an external service, and the setup guidance includes a credit-related request.

Mitigation: Protect the API key and review the account's credit use and balance before making requests.

## Reference(s):

- [TikTok Data documentation](https://superagnt.com/r/ch-tiktok-data-docs)
- [TikTok Data scoped MCP server](https://mcp.superagnt.com/mcp/tiktok)
- [API key setup](https://superagnt.com/r/ch-tiktok-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/tiktok-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured JSON API responses and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY for documented curl usage; API access is credit-based.]

## Skill Version(s):

2.0.18 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
