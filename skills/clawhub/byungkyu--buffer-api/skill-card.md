## Description:

Helps agents manage Buffer channels, schedule social posts, and create content ideas through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People managing social media use this skill to review Buffer accounts and channels, prepare and schedule posts, and set up approved automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A post or schedule change could target the wrong channel or contain unintended content.

Mitigation: Confirm the exact channel, content, and timing with the user before making changes.

Risk: Persistent automations can keep forwarding future events to a destination.

Mitigation: Confirm the trigger scope and destination, and remove unused triggers, functions, and connections.

Risk: Long-lived API keys can be exposed if handled outside the approved authentication flow.

Mitigation: Prefer OAuth, review connection scopes, and avoid exposing credentials in commands or destinations.

## Reference(s):

- [Buffer skill on ClawHub](https://clawhub.ai/byungkyu/skills/buffer-api)
- [Buffer API documentation](https://developers.buffer.com/reference.html)
- [Buffer API getting started](https://developers.buffer.com/guides/getting-started.html)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Buffer account, channel, post, and scheduling details returned by an authorized connection.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
