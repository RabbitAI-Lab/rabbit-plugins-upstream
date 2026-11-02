## Description:

Helps users plan and produce text-to-speech narration, multilingual or long-form audio, and authorized reusable voice clones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users creating narration from approved scripts can use the skill to plan short-form, long-form, or multilingual audio and manage an explicitly authorized reusable voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approval may grant broader media-generation and spending access than a voice-only task needs, and scripts or samples are sent to Beatra.

Mitigation: Prefer a release with voice-only permissions; review the requested access and understand the data transfer before approving paid work or uploading a sample.

Risk: Removing this package could disconnect other Beatra skills if their shared inventory is malformed.

Mitigation: Review the shared Beatra skill inventory before uninstalling when other Beatra skills are in use.

Risk: Installation analytics run automatically.

Mitigation: Review the package's installation analytics disclosure before installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/voiceover-narration-studio)
- [Beatra skill overview](https://beatra.ai/skills/voiceover-narration-studio)
- [Intent and routing](artifact/references/intent-and-routing.md)
- [Voice casting and delivery](artifact/references/voice-casting-and-delivery.md)
- [Long-form and multilingual production](artifact/references/long-form-and-multilingual.md)
- [Voice cloning and review](artifact/references/voice-cloning-and-review.md)
- [Updates and security](artifact/references/updates-and-security.md)

## Skill Output:

**Output Type(s):** [Audio, Text, Production guidance]

**Output Format:** [Narration audio files and concise text with production or delivery details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-form and multilingual deliverables follow the approved chapter, language, and segment order.]

## Skill Version(s):

0.2.9 (source: manifest and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
