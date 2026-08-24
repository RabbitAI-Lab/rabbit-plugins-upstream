## Description:

Restore and verify the Chatterbox TTS browser/OpenAI-compatible bridge stack after upgrades, reinstalls, or damaged local state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinguy](https://clawhub.ai/user/pinguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to recover a local Chatterbox TTS browser, Voice Lab, and OpenAI-compatible bridge setup while preserving user voices, configuration, and service overrides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery actions may change local Chatterbox files, user systemd services, browser extension setup, or voice settings.

Mitigation: Review proposed reinstall and service changes before execution, and prefer targeted repairs over full-stack replacement.

Risk: Repairs can overwrite user-created voices, selected defaults, or local service overrides.

Mitigation: Back up managed voices and systemd drop-ins before destructive recovery, then restore only deliberate local configuration.

Risk: Exposing services beyond localhost or retaining a development bridge API key can increase access risk.

Mitigation: Keep services bound to loopback by default and replace development credentials before any non-local exposure.

## Reference(s):

- [Server-resolved source: pinguy/Skills](https://github.com/pinguy/Skills/tree/main/skills/chatterbox-tts-recovery)
- [ClawHub skill page](https://clawhub.ai/pinguy/skills/chatterbox-tts-recovery)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and recovery checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on inspection, backup, targeted repair, configuration restoration, and acceptance checks for a local TTS stack.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
