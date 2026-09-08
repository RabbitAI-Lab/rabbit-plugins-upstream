## Description:

Suno music generation model. Supports inspiration mode (auto lyrics) and custom mode (manual lyrics), generating music with or without vocals. Suno 音乐生成模型。支持灵感模式（自动作词）和自定义模式（手动填词），可生成包含人声或纯器乐的音乐。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Suno-style music from prompts, either with automatically generated lyrics or with custom lyrics and style controls. It can request vocal or instrumental output through the pinned dLazy CLI and hosted dLazy API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a pinned third-party dLazy CLI and sends prompts to dLazy services.

Mitigation: Review the dLazy CLI source or npm package when supply-chain trust matters, and prefer npx or another non-global invocation path when possible.

Risk: Local media files supplied to image, video, or audio parameters may be uploaded to dLazy-hosted storage.

Mitigation: Only pass files intended for upload to dLazy and avoid submitting sensitive or restricted media.

Risk: The dLazy API key can be saved in local CLI configuration or passed through an environment variable.

Mitigation: Use a scoped, revocable API key and rotate or revoke it from the dLazy dashboard when access should change.

## Reference(s):

- [dLazy CLI GitHub project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs or an asynchronous generation ID; saved assets require an explicit --save path.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
