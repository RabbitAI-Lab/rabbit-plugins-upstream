## Description:

Post to LinkedIn and schedule LinkedIn posts from OpenClaw, Hermes, Claude Code or Codex. Publishes to the user's own LinkedIn account via the 1Social MCP server (OAuth, no API key), checks the LinkedIn 3,000-character limit and formatting first, schedules up to 30 days ahead and returns a delivery receipt. Use to post or schedule on LinkedIn, publish a post, plan LinkedIn content, or check, edit or delete LinkedIn posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sultanlive](https://clawhub.ai/user/sultanlive)

### License/Terms of Use:

MIT-0

## Use Case:

People managing their LinkedIn presence use this skill to draft, preview, publish, schedule, inspect, edit, or remove posts through 1Social.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading local media makes it publicly accessible before a post is approved, and canceling the post does not remove the upload.

Mitigation: Get approval for the exact files before uploading and use only files suitable for public sharing.

Risk: A post could be sent to an unintended connected account or destination.

Mitigation: Connect only intended accounts and verify the destination and final post before approving publication.

## Reference(s):

- [1Social LinkedIn publishing](https://1social.dev/post-to/linkedin?ref=skill)
- [1Social MCP setup](https://1social.dev/mcp)
- [ClawHub skill release](https://clawhub.ai/sultanlive/skills/linkedin)

## Skill Output:

**Output Type(s):** [Text, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with post drafts, setup commands, and delivery receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checks LinkedIn formatting and the 3,000-character limit; supports scheduling up to 30 days ahead.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
