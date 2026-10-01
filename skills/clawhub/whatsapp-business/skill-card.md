## Description:

Helps agents connect to WhatsApp Business to send messages, manage templates, and handle customer conversations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Businesses and developers use this skill to interact with customers through a connected WhatsApp Business account, manage message templates, and set up approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages reach real recipients and can incur costs or affect account standing.

Mitigation: Confirm each recipient and message content before sending; do not send in bulk without per-recipient approval.

Risk: Connection setup, template changes, and deletions can alter live account state.

Mitigation: Require explicit approval for connections and each write after reviewing the target and intended effect.

Risk: Trigger destinations can continuously forward future event data.

Mitigation: Disclose the destination, data, and persistence, and obtain separate approval before creating or changing a destination.

## Reference(s):

- [WhatsApp Business skill release](https://clawhub.ai/byungkyu/skills/whatsapp-business)
- [Maton](https://maton.ai)
- [WhatsApp Business API overview](https://developers.facebook.com/docs/whatsapp/cloud-api/overview)
- [Maton documentation](https://docs.maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Conversational text and Markdown with commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose account actions or automations requiring explicit user approval.]

## Skill Version(s):

1.2.8 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
