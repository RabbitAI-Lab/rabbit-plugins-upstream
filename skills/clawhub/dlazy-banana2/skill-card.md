## Description:

Generate/edit high-quality images with Nano Banana 2.0. Supports text-to-image and image-to-image. 使用 Nano Banana 2.0 生成/编辑高质量图片，支持文生图与图生图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through dLazy's Nano Banana 2.0 CLI using text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media may be sent to dLazy's hosted service for image generation.

Mitigation: Only submit prompts and files that are appropriate for third-party processing, and review dLazy service policies before use.

Risk: The CLI can store a dLazy API key in a local configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable or per-use npx invocation when persistent local credentials are not desired; rotate or revoke keys if exposed.

Risk: A global npm install adds a third-party command-line binary to the user's environment.

Mitigation: Confirm trust in the dLazy CLI and npm package, avoid elevated privileges, and prefer the pinned npx command for one-off use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs, asynchronous task IDs, or saved local image files through the dLazy CLI.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
