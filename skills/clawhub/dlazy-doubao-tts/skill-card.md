## Description:

使用豆包 (Doubao) TTS 文本转语音模型，将文字合成为自然流畅的语音播报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can turn supplied text into speech using the Doubao TTS service, select a supported voice and language, and save or retrieve the generated audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for speech generation is processed by dLazy and generation may consume paid credits.

Mitigation: Avoid sending text you are not comfortable sharing with the service, and check your account’s credit usage before generating audio.

Risk: The CLI uses a locally saved API key, and installation runs a third-party CLI.

Mitigation: Protect the local API key and review the pinned CLI release before installing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated speech audio, returned with a JSON result containing an output URL; audio format depends on the service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio can be saved to a local path; asynchronous requests can return a task identifier for later status checks.]

## Skill Version(s):

1.3.32 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
