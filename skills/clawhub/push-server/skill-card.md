## Description:

Helps an agent send push notifications, deliver batch updates, review sent messages, and manage a user's push channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[teakong](https://clawhub.ai/user/teakong)

### License/Terms of Use:

MIT

## Use Case:

People and developers use this skill to receive task results and important notifications through their own push channels, send separate updates for batch jobs, and review sent messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A disclosed channel code could let someone send messages to the channel.

Mitigation: Treat the 32-character channel code as a credential; use only the user's own channel and keep it out of public content.

Risk: Deleting a channel cannot be undone, and resetting one invalidates its old code.

Mitigation: Confirm the target channel before deleting, resetting, or editing it, and give the user the new code after a reset.

Risk: Installing a different release or installing globally broadens exposure to an untrusted source.

Mitigation: Install only from the intended publisher and prefer project-local installation.

## Reference(s):

- [Push Server on ClawHub](https://clawhub.ai/teakong/skills/push-server)
- [Push service documentation](https://push.phprm.com/mcp.html)
- [API reference](references/api.md)
- [Usage examples](references/example.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Push notification title and text, Markdown, or JSON body with an optional link; conversational guidance and message history on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can send one notification or separate notifications for batch results.]

## Skill Version(s):

1.6.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
