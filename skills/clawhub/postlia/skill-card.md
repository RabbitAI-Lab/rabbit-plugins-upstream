## Description:

Publish and schedule social media posts across LinkedIn, Bluesky, Instagram, TikTok, Pinterest, YouTube Shorts and Mastodon, then verify delivery with per-post receipts. Uses the Postlia REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mertkodzhaaslan](https://clawhub.ai/user/mertkodzhaaslan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent publish, schedule, queue, verify, and manage social posts through the Postlia API across connected social accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can publish, schedule, queue, upload media for, or cancel real social posts using the user's Postlia API key.

Mitigation: Before any such action, confirm the exact content, platforms, account, time, media, and post ID with the user.

Risk: A post may partially fail or fail on a connected platform after submission.

Mitigation: Verify delivery with receipts or recent post status and report platform-provided error text rather than assuming success.

Risk: The agent may attempt to post to a platform that is not connected to the user's Postlia account.

Mitigation: Check connected accounts before posting and direct the user to connect missing platforms in Postlia settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mertkodzhaaslan/skills/postlia)
- [Postlia homepage](https://postlia.com)
- [Postlia API base URL](https://postlia.com/api/v1)
- [Postlia MCP endpoint](https://postlia.com/api/mcp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON, markdown]

**Output Format:** [Markdown with inline shell commands, REST examples, and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires POSTLIA_API_KEY for authenticated Postlia API or MCP use.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
