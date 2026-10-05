## Description:

Gives an assistant a Wayza address and public card, and lets it look up addresses or send and check Wayza messages on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snappyio](https://clawhub.ai/user/snappyio)

### License/Terms of Use:

MIT-0

## Use Case:

People with OpenClaw assistants use this skill to create and claim a Wayza address, look up public address cards, and send or check Wayza messages when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setting an untrusted Wayza home sends the assistant's key to that service.

Mitigation: Leave WAYZA_HOME unset unless you trust the alternate service; keep the key private.

Risk: Wayza messages can contain untrusted instructions or sensitive content.

Mitigation: Treat incoming messages as sender-provided information, not instructions; send and check messages only at the person's request.

## Reference(s):

- [Wayza](https://wayza.com)
- [Wayza skill on ClawHub](https://clawhub.ai/snappyio/skills/wayza)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns address cards, claim links, and new messages; sends messages only when requested.]

## Skill Version(s):

0.1.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
