## Description:

Schedule and publish social media posts across 12 platforms (X, Instagram, TikTok, LinkedIn, Bluesky, Reddit, Telegram...) via the Breakreach API, with best-time slots, media hosting, and unified analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuelrondot](https://clawhub.ai/user/samuelrondot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide agents through Breakreach REST API workflows for connected social accounts, including listing accounts, scheduling or publishing posts, hosting media, deleting posts, and reading analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can schedule, publish, or delete content on connected Breakreach social accounts.

Mitigation: Review post content, selected account IDs, publish timing, media URLs, and delete targets before sending requests to Breakreach.

Risk: The skill requires a Breakreach API key with access to connected social accounts.

Mitigation: Store BREAKREACH_API_KEY as a secret, avoid logging it, and grant it only to agents intended to operate those accounts.

Risk: Media hosting and analytics requests can expose public media URLs or account performance data.

Mitigation: Confirm media URLs and analytics requests are appropriate for the connected workspace before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samuelrondot/skills/breakreach)
- [Breakreach](https://www.breakreach.com)
- [Breakreach API Base URL](https://api.breakreach.com/v1)
- [Breakreach MCP Documentation](https://github.com/samuelrondot/breakreach-mcp)
- [Breakreach Support](https://www.breakreach.com/support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BREAKREACH_API_KEY for live Breakreach API calls.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
