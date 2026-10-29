## Description:

Postemi schedules and publishes social posts from the command line to 25+ platforms, including Facebook, Instagram, X, LinkedIn, TikTok, YouTube, Threads, Bluesky, Pinterest and Mastodon.

This skill is ready for commercial/non-commercial use.

## Publisher:

[norbertlevente](https://clawhub.ai/user/norbertlevente)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this agent skill to authenticate to Postemi, manage connected social channels, upload media, schedule or publish posts, and review post analytics through the Postemi CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing or deleting posts can affect connected social channels immediately.

Mitigation: Limit access to the workspaces and channels needed, review content as drafts when appropriate, and confirm destinations before publishing or deleting.

Risk: Uploaded media may be used in posts sent to connected channels.

Mitigation: Upload only intended media and check the post content and channel before scheduling or publishing.

## Reference(s):

- [Postemi official website](https://postemi.com)
- [Postemi API](https://api.postemi.com)
- [Postemi MCP server](https://mcp.postemi.com/mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown with shell command examples and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require an authenticated Postemi account and connected channels; media must be uploaded before publishing.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
