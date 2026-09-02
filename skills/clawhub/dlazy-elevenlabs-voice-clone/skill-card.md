## Description:

ElevenLabs Instant Voice Cloning (IVC) uploads a clean voice sample to create a custom voice usable with ElevenLabs TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted ElevenLabs voice-cloning command from an agent workflow, supplying an audio URL or local audio path plus a voice name and optional description.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples can be sensitive biometric data and may be uploaded to dLazy-hosted infrastructure.

Mitigation: Use only voice samples you own or have explicit permission to clone, and avoid passing local audio paths unless upload is acceptable.

Risk: Saved dLazy API keys may remain in the local CLI configuration after use.

Mitigation: Prefer per-invocation credentials for temporary use, or rotate and revoke saved API keys when access is no longer needed.

Risk: The artifact documentation contains command and output mismatches for this voice-cloning workflow.

Mitigation: Check `dlazy elevenlabs-voice-clone -h` and use `--dry-run` where available before relying on examples or downstream automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when --no-wait is used; local audio paths may be uploaded to dLazy-hosted storage.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
