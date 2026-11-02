## Description:

Instagram profiles, posts, reels, and audience data for agents — influencer and brand research without a headless browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and data teams use the skill to retrieve Instagram profile, media, audience, and location data for creator research, social monitoring, and analytics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key is a bearer credential and also works with other provider services.

Mitigation: Supply it through the environment, avoid exposing it in shared prompts or logs, and review which provider services can use the key.

Risk: API requests can consume account credits.

Mitigation: Check the account balance and review credit costs before running repeated or broad queries.

Risk: The documented curl examples include escaped quoting and token expansion that may need correction before use.

Mitigation: Correct the shell quoting and confirm the environment variable expands in the Authorization header before sending a request.

## Reference(s):

- [Instagram Data documentation](https://superagnt.com/r/ch-instagram-data-docs)
- [Scoped Instagram MCP server](https://mcp.superagnt.com/mcp/instagram)
- [Instagram MCP installation guide](https://www.superagnt.com/install?facet=instagram)
- [API key setup](https://superagnt.com/r/ch-instagram-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/instagram-data)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands]

**Output Format:** [Structured JSON data from the API, with Markdown setup and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live requests require SUPERAGNT_API_KEY and may consume account credits.]

## Skill Version(s):

2.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
