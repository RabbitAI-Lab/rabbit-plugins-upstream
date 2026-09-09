## Description:

Generate exquisite images with Kling o1 model. Supports text-to-image and image-to-image. 使用可灵 (Kling) o1 模型生成精美图像，支持文生图与参考图生图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through the Kling o1 model from text prompts and optional reference images. It invokes the dLazy CLI/API and returns generated image output metadata, URLs, or saved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image files may be sent to dLazy's hosted image-generation service.

Mitigation: Avoid passing private or sensitive files unless the user intends to upload them to the service.

Risk: The dLazy CLI may store an API key locally.

Mitigation: Use the documented login or auth flow, keep the key in the user-scoped configuration, and rotate or revoke the key when needed.

Risk: API calls may consume dLazy credits.

Mitigation: Use dry-run or cost-estimate behavior when appropriate and confirm credit-sensitive requests before execution.

Risk: The skill depends on a third-party CLI package.

Mitigation: Prefer the pinned npx invocation or a non-privileged install, and review the linked CLI source before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON response with generated image URLs and optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous generation identifier when invoked with no-wait mode.]

## Skill Version(s):

1.3.14 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
