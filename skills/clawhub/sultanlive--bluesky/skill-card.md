## Description:

Post to Bluesky and schedule Bluesky posts and threads from OpenClaw, Hermes, Claude Code or Codex. Publishes to the user's own Bluesky account via the 1Social MCP server (OAuth, no API key), checks the Bluesky 300-character limit and thread rules first, schedules up to 30 days ahead and returns a delivery receipt. Use to post or schedule on Bluesky, publish a post or a thread, plan Bluesky content, or check, edit or delete Bluesky posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sultanlive](https://clawhub.ai/user/sultanlive)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can draft, publish, and schedule Bluesky posts and threads through their connected account, then review delivery status or manage scheduled and published posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public posting, deletion, and media uploads can affect the connected account or expose local files; uploaded files become publicly accessible immediately.

Mitigation: Check the authorized account and every destination, show the final post details, and get approval before publishing, deleting, or uploading local media.

Risk: Publishing after the free trial requires a paid plan.

Mitigation: Confirm the 1Social plan and pricing before continuing to publish after the trial.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sultanlive/skills/bluesky)
- [1Social MCP setup](https://1social.dev/mcp)
- [1Social pricing](https://1social.dev/pricing)
- [1Social Bluesky publishing](https://1social.dev/post-to/bluesky?ref=skill)

## Skill Output:

**Output Type(s):** [Text, API Calls, Guidance]

**Output Format:** [Bluesky post or thread text, plus scheduling, status, and delivery receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Posts are limited to 300 characters each; scheduling is supported up to 30 days ahead.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
