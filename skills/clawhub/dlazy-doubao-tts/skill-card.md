## Description:

Synthesize text into natural and fluent speech using Doubao TTS. 使用豆包 (Doubao) TTS 文本转语音模型，将文字合成为自然流畅的语音播报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can turn text into Chinese or English speech with selectable voices and speaking speed, then retrieve the generated audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial: it could not inspect the CLI package or resolve several references, and it found no direct evidence tying the reported login or generic CLI calls to Doubao speech synthesis.

Mitigation: Review the CLI package and confirm the command behavior before installing or invoking it; use the documented dry-run option to inspect a request before generation.

Risk: Text supplied for synthesis is sent to the hosted dLazy service.

Mitigation: Avoid submitting confidential text unless the service is approved for that data and its terms are acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy service](https://dlazy.com)
- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands]

**Output Format:** [Generated speech audio with a hosted URL or saved file, plus command result and task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese or English voice options and adjustable speed; generation may complete asynchronously.]

## Skill Version(s):

1.3.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
