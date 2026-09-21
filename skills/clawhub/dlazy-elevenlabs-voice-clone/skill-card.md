## Description:

Creates an ElevenLabs Instant Voice Cloning voice from a clean speaker sample for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production agents use this skill to invoke the dLazy CLI for ElevenLabs voice cloning from a user-provided audio sample, then use the resulting custom voice with text-to-speech workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples can include sensitive speaker identity data and may be processed by dLazy or ElevenLabs infrastructure.

Mitigation: Use only samples from speakers who gave informed consent, avoid sensitive recordings, and review the applicable privacy, retention, and deletion terms before upload.

Risk: A persistent dLazy API key may be stored in the local CLI configuration.

Mitigation: Use the per-run DLAZY_API_KEY environment variable when persistent storage is not desired, and rotate or revoke organization keys when access should change.

Risk: The security evidence flags inconsistent documentation and unclear voice privacy and consent warnings.

Mitigation: Review the skill before installing, confirm current CLI behavior with dlazy elevenlabs-voice-clone -h, and require clearer privacy, consent, retention, and deletion guidance before treating the release as cleanly documented.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted result URLs or an asynchronous task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter shows 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
