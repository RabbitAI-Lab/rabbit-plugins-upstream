## Description:

Turns text into natural-sounding speech using Doubao TTS through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users generate spoken audio from text, selecting a language and voice for narration or voiceovers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the external dLazy CLI introduces package supply-chain exposure.

Mitigation: Review the pinned @dlazy/cli package before use; use npx @dlazy/cli@1.2.3 to avoid a persistent global installation.

Risk: Prompts and referenced media files may be sent to dLazy services.

Mitigation: Avoid submitting sensitive content or local files unless their transfer is acceptable.

Risk: The documented sample shows an image rather than speech, so returned output may be misidentified.

Mitigation: Specify language and save path explicitly, and verify the returned asset is audio before use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Audio files]

**Output Format:** [CLI instructions and JSON result with an output URL; optional downloaded audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports voice and language selection; asynchronous runs can return a task ID before the result is ready.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
