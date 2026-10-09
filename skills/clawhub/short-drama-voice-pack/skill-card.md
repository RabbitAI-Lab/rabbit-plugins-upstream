## Description:

Turns a short-drama episode script into labeled dialogue clips with a consistent voice for each role.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Editors and creators use this skill to turn attributed short-drama episode scripts into ordered, role-labeled voiceover clips for editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Beatra connection retains a device token and requests media, voice, task, and wallet permissions beyond voiceover alone.

Mitigation: Review the requested account access before approving and disconnect the skill when no longer needed.

Risk: The skill may install updates without a separate confirmation.

Mitigation: Disable automatic updates with the documented update command if changes require prior review.

Risk: Speech generation and optional voice cloning may charge credits; cloning uploads a local voice sample.

Mitigation: Confirm the live estimate and voice rights before paid work; obtain speaker consent before uploading a sample.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/short-drama-voice-pack)
- [Beatra skill homepage](https://beatra.ai/skills/short-drama-voice-pack)
- [Short-drama voice-pack workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Audio clips, Text]

**Output Format:** [Numbered MP3 clip links or artifacts with role and line labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each clip reports its duration, MIME type, resolved model, and credits charged; voices remain consistent per role.]

## Skill Version(s):

0.1.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
