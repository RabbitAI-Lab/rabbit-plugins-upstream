## Description:

Instagram profiles, posts, reels, and audience data for agents — influencer and brand research without a headless browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and research teams use the skill to retrieve Instagram profile and media data for creator and brand research, social listening, and content analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests send the user's Superagnt API key and may consume workspace credits.

Mitigation: Provide the key through environment configuration rather than chat, and check the workspace's credit balance before use.

Risk: The documented MCP option requests permissions during OAuth setup; live server behavior was not verified.

Mitigation: Review the MCP server's requested permissions before approving access.

## Reference(s):

- [Instagram Data documentation](https://superagnt.com/r/ch-instagram-data-docs)
- [Instagram Data MCP server](https://mcp.superagnt.com/mcp/instagram)
- [MCP installation instructions](https://www.superagnt.com/install?facet=instagram)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/instagram-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions]

**Output Format:** [Markdown instructions with curl commands; API responses in JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live Instagram data returned by the selected endpoint; usage may consume API credits.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
