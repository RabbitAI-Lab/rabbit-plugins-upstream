## Description:

Helps agents use WhatsApp Business to send messages, manage templates and media, and work with customer conversations through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business teams use this skill to work with an authorized WhatsApp Business account, including sending customer messages, managing message templates and media, and setting up approved scheduled or cross-app actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the wrong account or granting more WhatsApp Business access than intended.

Mitigation: Confirm the specific account and requested access with the user before connecting it.

Risk: Messages, template or media changes, and automated actions can affect customers or persist beyond the current task.

Mitigation: Review and confirm the exact recipient, target, payload, and persistence behavior before writes or setting up triggers and destinations.

## Reference(s):

- [WhatsApp Business skill release](https://clawhub.ai/byungkyu/skills/whatsapp-business)
- [WhatsApp Business Cloud API overview](https://developers.facebook.com/docs/whatsapp/cloud-api/overview)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)
- [Time-based trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions use the user's authorized WhatsApp Business connection.]

## Skill Version(s):

1.2.7 (source: ClawHub server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
