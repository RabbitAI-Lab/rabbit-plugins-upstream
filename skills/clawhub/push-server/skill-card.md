## Description:

Sends single or batched push notifications through push-server and lets agents read message history and manage channels when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[teakong](https://clawhub.ai/user/teakong)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers use this skill to send task results and important notifications to their push channels, deliver batch results separately, and retrieve or manage messages and channels on request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The channel code grants access to send notifications and obtain a token for reading or managing channels.

Mitigation: Treat the channel code like a password; do not publish it or include it in logs.

Risk: Deleting or resetting a channel can disrupt notifications or invalidate an existing channel code.

Mitigation: Only approve channel deletion or reset when it is intended.

Risk: Unpinned installations can change behavior across releases.

Mitigation: Pin the installation version when reproducibility matters.

## Reference(s):

- [push-server service and setup](https://push.phprm.com/mcp.html)
- [push-server release on ClawHub](https://clawhub.ai/teakong/skills/push-server)
- [HTTP API reference](references/api.md)
- [Push message examples](references/example.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Push notification title and optional Markdown, plain-text, or JSON body; conversational responses for lookups and channel management]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can send separate notifications for batch results and include an optional destination link.]

## Skill Version(s):

1.5.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
