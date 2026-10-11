## Description:

Helps users select voices, plan and generate narration from approved text, and create authorized reusable voices with Beatra.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to choose voices, estimate costs, and turn approved scripts into short, long-form, or multilingual narration; they can also create a reusable voice with the speaker's consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Beatra grants a broad account token with spending and multiple media-generation scopes, stored on the local device.

Mitigation: Review the requested access and secure local credentials before connecting; use a dedicated account if narrower access is needed.

Risk: The bundled client can silently install updates from Beatra's release channel.

Mitigation: Use only if you trust that update channel, or disable automatic updates with the provided update command and review releases before updating.

Risk: Paid voice generation and cloning rely on agent instructions rather than code-enforced approval gates.

Mitigation: Review the text, voice or sample, live price estimate, and speaker consent before approving each paid operation; monitor account charges.

## Reference(s):

- [Beatra AI Voice Studio on ClawHub](https://clawhub.ai/beatra-ai/skills/beatra-ai-voice-studio)
- [Beatra AI Voice Studio](https://beatra.ai/skills/beatra-ai-voice-studio)
- [Voice casting and delivery](references/voice-casting-and-delivery.md)
- [Voice cloning and review](references/voice-cloning-and-review.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Audio links]

**Output Format:** [Markdown with narration plans, cost estimates, and links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May organize results by chapter, language, and use case.]

## Skill Version(s):

0.3.0 (source: server-resolved release and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
