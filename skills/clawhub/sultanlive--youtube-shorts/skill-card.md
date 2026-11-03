## Description:

Post to YouTube Shorts and schedule YouTube Shorts Shorts from OpenClaw, Hermes, Claude Code or Codex. Publishes to the user's own YouTube Shorts account via the 1Social MCP server (OAuth, no API key), checks the YouTube Shorts vertical-video, length and title rules first, schedules up to 30 days ahead and returns a delivery receipt. Use to post or schedule on YouTube Shorts, publish a vertical video, plan YouTube Shorts content, or check, edit or delete YouTube Shorts posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sultanlive](https://clawhub.ai/user/sultanlive)

### License/Terms of Use:

MIT

## Use Case:

External users and creators use this skill to prepare, preview, publish, and schedule YouTube Shorts through their connected 1Social account. They can also check delivery status and manage scheduled posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading local media creates a public link immediately, and canceling a post does not remove the uploaded file.

Mitigation: Show the exact files and obtain the user's approval before upload; upload only media suitable for public links.

Risk: Publishing is public, and published YouTube videos must be removed directly on YouTube.

Mitigation: Preview the final post and confirm the destination account, media, text, and timing with the user before publishing.

Risk: Publishing after the free trial requires a paid 1Social plan.

Mitigation: Check the connected account's plan and quota before publishing, and tell the user when a paid plan is required.

## Reference(s):

- [1Social YouTube publishing](https://1social.dev/post-to/youtube?ref=skill)
- [1Social MCP setup](https://1social.dev/mcp)

## Skill Output:

**Output Type(s):** [Text, API Calls, Guidance]

**Output Format:** [Markdown text and structured publishing actions with delivery receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A single YouTube Shorts video per post; supports immediate publishing or scheduling up to 30 days ahead.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
