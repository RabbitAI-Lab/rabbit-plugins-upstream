## Description:

Helps agents draft, publish, schedule, and analyze social posts across connected PostNext channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[postnextio](https://clawhub.ai/user/postnextio)

### License/Terms of Use:

MIT

## Use Case:

Social media teams and account owners use this skill to prepare media, publish or schedule posts to connected channels, and review post and audience analytics through PostNext.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key can act on real PostNext accounts and connected social channels.

Mitigation: Use a dedicated limited key if available, and keep it out of posts, logs, and shared prompts.

Risk: Publishing, scheduling, canceling, or deleting can happen without a built-in confirmation gate.

Mitigation: Confirm the provider, channel, text, media, and time with the user before each action; avoid acting on ambiguous or untrusted requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/postnextio/skills/postnext-social-manager)
- [PostNext](https://postnext.io)
- [Posts reference](references/posts.md)
- [Media reference](references/media.md)
- [Channels reference](references/channels.md)
- [Analytics reference](references/analytics.md)
- [Errors reference](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with commands and summaries of post status or analytics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing, scheduling, canceling, and deleting can change the connected account.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
