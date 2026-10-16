## Description:

Helps agents create and manage AI images, video, music, and speech, and retrieve public social data through Beatra.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and other users can ask an agent to generate or edit media, synthesize or clone voices with consent, and look up public social posts and accounts. The agent returns task results, asset links, and actual credit usage when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent device connection grants Beatra access to account tasks and selected local uploads.

Mitigation: Connect only if comfortable with that access; revoke the device in the Beatra Console when no longer needed.

Risk: The client silently updates local executable files by default.

Mitigation: Review automatic-update behavior and disable it with the documented update command if manual approval is preferred.

Risk: Media and social-data tasks may incur charges, and voice cloning may affect someone else's voice rights.

Mitigation: Review costs before paid requests and use voice cloning only with the speaker's consent.

## Reference(s):

- [Beatra Universal release](https://clawhub.ai/beatra-ai/skills/beatra)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Speech and voices](references/speech-and-voices.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Media asset links, Guidance]

**Output Format:** [Markdown responses with asset links and JSON for public social data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports returned task status, asset details, and actual credit use when available.]

## Skill Version(s):

2.9.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
