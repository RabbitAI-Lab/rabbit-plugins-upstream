## Description:

Connects an OpenClaw agent to a user's phone for messaging, calls, contacts, media and file control, with optional local voice cloning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nj070574-gif](https://clawhub.ai/user/nj070574-gif)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers operating their own Linux host and phone use this skill to let an OpenClaw agent receive and send messages, manage calls and media, transfer files, and optionally synthesize speech in their voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic replies or call handling may send texts or reject calls without the manual review users expect.

Mitigation: Review or disable LLM auto-reply and trusted-call auto-handler paths before enabling services.

Risk: Phone control and trusted-number permissions can expose private communications or enable unintended actions.

Mitigation: Install only on a single-user machine with a phone you control, and keep the trusted-numbers list very small.

Risk: A stored phone PIN could allow unintended device access.

Mitigation: Avoid storing a phone PIN unless you accept the risk.

Risk: Cloned speech can be mistaken for the phone owner's authentic voice.

Mitigation: Obtain clear consent and disclose when output is voice-cloned.

## Reference(s):

- [Paired on ClawHub](https://clawhub.ai/nj070574-gif/skills/paired)
- [Voice setup guide](docs/VOICE-SETUP.md)
- [VoxCPM2 model card](https://huggingface.co/openbmb/VoxCPM2)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Audio files]

**Output Format:** [Markdown guidance and structured command output; optional synthesized audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Configured actions can send texts, place calls, and synthesize cloned speech.]

## Skill Version(s):

2.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
