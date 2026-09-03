## Description:

Synthesize text into natural and fluent speech using Doubao TTS. 使用豆包 (Doubao) TTS 文本转语音模型，将文字合成为自然流畅的语音播报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to synthesize supplied text into natural speech through the dLazy hosted Doubao TTS service, with selectable language, voice, speed, async polling, and save-path options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for synthesis and any files explicitly passed to the CLI may be processed by dLazy's hosted service.

Mitigation: Use the skill only for content that can be shared with dLazy, and avoid passing sensitive files unless that processing is approved.

Risk: Authentication stores a dLazy API key in the user's CLI configuration or uses the DLAZY_API_KEY environment variable.

Mitigation: Prefer the npx option when avoiding a persistent global install, restrict local config access, and rotate or revoke the API key from dLazy when needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, Files]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as a hosted URL and can be saved to a local path when requested.]

## Skill Version(s):

1.3.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
