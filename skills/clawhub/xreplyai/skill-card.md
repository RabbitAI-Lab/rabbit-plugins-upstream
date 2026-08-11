## Description:

Generate, schedule, and publish posts across 15 platforms including X, LinkedIn, Instagram, Threads, Facebook, YouTube, TikTok, Pinterest, Bluesky, Mastodon, Discord, Telegram, Tumblr, Google Business, and Slack in the user's voice using AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jmoon90](https://clawhub.ai/user/jmoon90)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create AI-generated social post drafts, manage queues and schedules, publish to connected social accounts, adjust writing preferences, and check quota or billing status through the XreplyAI MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish, schedule, update, and delete posts on connected social accounts.

Mitigation: Preview drafts, confirm the target account and platform, prefer scheduled_at or use_next_slot unless immediate publishing is explicitly intended, and require confirmation before delete or recurring content-plan actions.

Risk: The skill depends on an XREPLY_TOKEN with access to XreplyAI and connected social accounts.

Mitigation: Install only if the user trusts XreplyAI with the token and connected accounts, and keep the token secret in the skill configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jmoon90/skills/xreplyai)
- [XreplyAI homepage](https://xreplyai.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with mcporter shell command examples and structured MCP responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires XREPLY_TOKEN and mcporter or npx. The artifact documents @xreplyai/mcp version 0.16.1 for MCP tool invocation.]

## Skill Version(s):

0.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
