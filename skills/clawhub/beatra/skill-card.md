## Description:

Creates and edits images, videos, music, and speech with Beatra, and retrieves public social media data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to generate or edit media, produce narration, manage finished assets, and research public social content through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic updates can replace installed package files without a separate prompt.

Mitigation: Review updates under strict change control or disable automatic updates using the documented command.

Risk: Prompts, uploaded media, and public social lookup requests are sent to Beatra; a persistent device token is stored locally.

Mitigation: Share only appropriate content and protect the local Beatra connection and device token.

Risk: Approved paid operations can consume Beatra credits.

Mitigation: Check live cost estimates and approve video or voice-cloning production cards before submitting paid work.

Risk: Voice cloning can be misused without the speaker's permission.

Mitigation: Clone a voice only after obtaining clear authorization from its owner.

## Reference(s):

- [Beatra Universal on ClawHub](https://clawhub.ai/beatra-ai/skills/beatra)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Speech and voices](references/speech-and-voices.md)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, Text, JSON]

**Output Format:** [Media artifact links and metadata, text, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports returned task status and actual credit usage when available.]

## Skill Version(s):

2.9.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
