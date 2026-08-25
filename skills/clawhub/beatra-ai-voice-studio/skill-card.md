## Description:

Beatra AI Voice Studio helps an agent plan and run Beatra text-to-speech work, including short voiceovers, ordered long-form narration, supplied multilingual speech, and consented reusable voice cloning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, educators, and agents use this skill to prepare and deliver ready-to-edit speech audio through Beatra. It supports voice selection, price estimation, paid task approval, long-form and multilingual production ledgers, and consented voice cloning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad Beatra account authority and stores a local bearer token under ~/.beatra.

Mitigation: Install only if this authorization is acceptable, and review Beatra account and device revocation controls before use.

Risk: Voice samples and generated-task data are sent to Beatra.

Mitigation: Use only samples and task data that the user is authorized to send, and obtain explicit voice-cloning consent before upload.

Risk: The installed package performs default-on self-updates.

Mitigation: Review the update behavior before installation and disable automatic updates with the documented update --auto off command when that is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/beatra-ai-voice-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/beatra-ai-voice-studio)
- [Intent and Routing](references/intent-and-routing.md)
- [Voice Casting and Delivery](references/voice-casting-and-delivery.md)
- [Long-Form and Multilingual Production](references/long-form-and-multilingual.md)
- [Voice Cloning and Review](references/voice-cloning-and-review.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and structured production cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task facts, audio artifact metadata, billing facts, and voice identifiers returned by Beatra.]

## Skill Version(s):

0.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
