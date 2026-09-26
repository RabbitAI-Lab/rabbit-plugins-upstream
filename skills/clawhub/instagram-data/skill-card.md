## Description:

Instagram profiles, posts, reels, and audience data for agents - influencer and brand research without a headless browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketing teams, researchers, and data teams use this skill to access Instagram profile, post, reel, hashtag, location, and audience data through superagnt for social listening, creator intelligence, dashboards, alerts, and analytics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instagram research targets and the superagnt API key are sent to superagnt for API requests.

Mitigation: Use the SUPERAGNT_API_KEY environment variable, avoid pasting secrets into prompts or logs, and review superagnt handling requirements before use.

Risk: The download-link endpoint can retrieve Instagram media.

Mitigation: Use the download-link endpoint only when the user has the right to retrieve that media.

## Reference(s):

- [Documentation](https://superagnt.com/r/ch-instagram-data-docs)
- [Scoped MCP Server](https://mcp.superagnt.com/mcp/instagram)
- [MCP Client Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub Listing](https://clawhub.ai/superagnt/skills/instagram-data)

## Skill Output:

**Output Type(s):** [API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON tool schemas and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl; API calls return structured JSON from superagnt endpoints.]

## Skill Version(s):

2.0.6 (source: frontmatter, release evidence, artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
