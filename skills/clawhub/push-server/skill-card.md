## Description:

Sends task updates and selected content to a user's configured notification or webhook channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[teakong](https://clawhub.ai/user/teakong)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users can send task summaries or selected structured content to their own configured notification or webhook channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notifications or webhook payloads may expose private or proprietary content to the configured destination.

Mitigation: Verify the destination and review content before sending; exclude secrets, personal data, proprietary content, and full logs unless explicitly approved.

Risk: A disclosed channel code could let someone send messages to that channel.

Mitigation: Treat the channel code as a credential; keep it out of messages, logs, and committed files.

## Reference(s):

- [Source repository (server-resolved provenance)](https://github.com/teakong/push-skill)
- [ClawHub skill release](https://clawhub.ai/teakong/skills/push-server)
- [Push service setup](https://push.phprm.com/mcp.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Plain-text title with optional Markdown or JSON body and a link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A configured push channel is required; title, body, and link have length limits.]

## Skill Version(s):

0.1.0 (source: ClawHub release; bundled skill frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
