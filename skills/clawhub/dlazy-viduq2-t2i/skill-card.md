## Description:

Generate high-quality images with Vidu Q2. Supports text-to-image and image-to-image. 使用 Vidu Q2 生成高质量图像，支持丰富的文生图与图生图指令。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Vidu Q2 images through the dLazy CLI from text prompts or optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and local media paths supplied to the CLI may be sent to dLazy cloud services for generation.

Mitigation: Use the skill only for inputs appropriate for dLazy/Vidu Q2, and avoid sending sensitive prompts or media unless the user accepts that service flow.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use OS-user-restricted config, rotate or revoke keys from the dLazy dashboard when needed, or pass DLAZY_API_KEY per invocation when persistent local storage is undesirable.

Risk: API usage may consume account credits or fail when credits are insufficient.

Mitigation: Use dry-run or cost-estimate behavior when appropriate and direct users to the dLazy credits dashboard if the service reports insufficient balance.

Risk: The skill depends on a third-party pinned npm CLI and hosted API endpoints.

Mitigation: Install only when dLazy/Vidu Q2 generation is intended, prefer the pinned @dlazy/cli version declared by the skill, and review the package/source links before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Image files, URLs, Configuration guidance]

**Output Format:** [Markdown guidance with shell commands and JSON responses that include generated image URLs or saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when --no-wait is used; generated assets are hosted on files.dlazy.com or saved locally when --save is provided.]

## Skill Version(s):

1.3.19 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
