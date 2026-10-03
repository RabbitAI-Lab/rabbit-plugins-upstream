## Description:

Helps users plan and produce voiceovers, long-form narration, multilingual speech, and authorized reusable voices from approved text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to select voices, estimate costs, and generate ready-to-edit narration from approved scripts. It also coordinates chapter-by-chapter and multilingual deliveries and consent-based voice cloning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared device token grants broad media-generation access beyond voiceover tasks.

Mitigation: Review the requested account permissions before connecting Beatra and keep the device token private.

Risk: Automatic updates can replace local skill files without separate confirmation.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if changes require review first.

Risk: Voice-cloning samples contain sensitive biometric data and could be used without the speaker's consent.

Mitigation: Obtain clear speaker authorization before uploading any sample and handle samples as sensitive data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/voiceover-narration-studio)
- [Voice casting and delivery](references/voice-casting-and-delivery.md)
- [Voice cloning and review](references/voice-cloning-and-review.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with production plans, task details, and links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report returned audio artifact details or reusable voice IDs; generated audio is delivered by Beatra.]

## Skill Version(s):

0.2.2 (source: ClawHub release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
