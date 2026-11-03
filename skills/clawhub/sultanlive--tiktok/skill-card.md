## Description:

Post to TikTok and schedule TikTok videos and photo carousels from OpenClaw, Hermes, Claude Code or Codex. Publishes to the user's own TikTok account via the 1Social MCP server (OAuth, no API key), checks the TikTok caption and media-format rules first, schedules up to 30 days ahead and returns a delivery receipt. Use to post or schedule on TikTok, publish a video or photos, plan TikTok content, or check, edit or delete TikTok posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sultanlive](https://clawhub.ai/user/sultanlive)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and social media managers can use the skill from OpenClaw, Hermes, Claude Code, or Codex to prepare, publish, schedule, and manage posts on their connected TikTok accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading local media creates a public link immediately, even if the post is later declined.

Mitigation: Show the user the exact files to be uploaded and wait for their approval before uploading.

Risk: A published TikTok cannot be removed through 1Social and may require manual removal by the account owner.

Mitigation: Before publishing, confirm the final caption, destination account, media, and timing with the user; explain that removal may need to be done in TikTok.

Risk: Publishing after the 1Social free trial requires a paid plan.

Mitigation: Check the connected account's plan and quota before scheduling or publishing, and surface any plan requirement to the user.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sultanlive/skills/tiktok)
- [Publisher profile](https://clawhub.ai/user/sultanlive)
- [1Social TikTok integration](https://1social.dev/post-to/tiktok?ref=skill)
- [1Social MCP setup](https://1social.dev/mcp)
- [1Social pricing](https://1social.dev/pricing)

## Skill Output:

**Output Type(s):** [Text, API Calls, Status reports]

**Output Format:** [TikTok captions and structured posting or scheduling receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Posts require video or photo media; scheduling supports up to 30 days ahead.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
