## Description:

Convert images into WebP stickers and send native WhatsApp stickers through an existing Baileys bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sakumdisinipa](https://clawhub.ai/user/sakumdisinipa)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users with an existing authenticated WhatsApp bridge can convert a local image to a WebP sticker and request delivery to a user-confirmed chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed or untrusted bridge could send media through the user's account without authorization.

Mitigation: Use a bridge you control; keep it on localhost or secure remote access and do not disable hash checking without trusting the bridge.

Risk: A mistaken recipient ID could disclose the image to the wrong chat.

Mitigation: Confirm the recipient chat ID with the user before sending.

Risk: WhatsApp session data or personal information could be exposed.

Mitigation: Keep session files, credentials, private chat IDs, and personal data out of public files and logs.

## Reference(s):

- [ClawHub release](https://clawhub.ai/sakumdisinipa/skills/whatsapp-sticker)
- [Server-resolved source repository](https://github.com/SakumDisiniPa/whatsapp-sticker)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow creates a temporary WebP sticker and reports the bridge's send result; bridge success does not guarantee recipient receipt.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
