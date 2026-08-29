## Description:

ElevenLabs Instant Voice Cloning (IVC). Upload a clean voice sample to clone a custom voice usable with ElevenLabs TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call the dLazy CLI for ElevenLabs instant voice cloning from a clean voice sample and receive generated result metadata for TTS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning can enable impersonation or non-consensual use of a person's voice.

Mitigation: Use the skill only with voices you own or have explicit permission to clone, and reject requests involving sensitive third-party audio.

Risk: Audio samples and prompts may be sent to hosted dLazy and ElevenLabs services, creating privacy and retention considerations.

Mitigation: Review dLazy and ElevenLabs retention, deletion, and data-use terms before submitting sensitive audio.

Risk: Persistently stored API keys can be exposed if the local account or configuration file is compromised.

Mitigation: Prefer per-run DLAZY_API_KEY use for sensitive environments, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, API Calls, Guidance]

**Output Format:** [JSON result metadata with optional shell commands and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy API authentication; local audio paths may be uploaded to dLazy-hosted media storage for processing.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
