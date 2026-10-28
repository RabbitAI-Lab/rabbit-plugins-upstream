## Description:

Post to X (Twitter) and schedule X (Twitter) tweets and threads from OpenClaw, Hermes, Claude Code or Codex.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sultanlive](https://clawhub.ai/user/sultanlive)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can draft, publish, schedule, and manage posts and threads on their connected X account. The skill also supports checking delivery status and editing or deleting posts where the network allows it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A disk file uploaded for a post becomes publicly accessible before the post is approved, and declining publication does not remove it.

Mitigation: Show the user the exact files before upload and wait for approval; upload only files they intend to make public.

Risk: Publishing to the wrong connected account or destination can expose content publicly, and some networks do not allow removal through the skill.

Mitigation: Review authorized accounts and destinations, then show the final content, target account, media, and schedule and get clear confirmation before publishing.

Risk: Retrying delivery can consume quota and may duplicate a post when delivery status is unknown.

Mitigation: Check the network before retrying an unknown delivery, and confirm the outcome with the user before taking a retry action.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sultanlive/skills/twitter)
- [1Social X publishing guide](https://1social.dev/post-to/x?ref=skill)
- [1Social MCP setup](https://1social.dev/mcp)
- [1Social pricing](https://1social.dev/pricing)

## Skill Output:

**Output Type(s):** [Text, API calls, Guidance]

**Output Format:** [Social post and thread text, scheduling or management requests, and delivery receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Post length, thread splitting, and media constraints are checked for the selected network; posts may be published immediately or scheduled up to 30 days ahead.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
