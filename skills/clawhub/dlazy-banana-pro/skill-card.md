## Description:

Generate/edit images with Nano Banana Pro. Supports text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through the dLazy CLI using text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected media, API credentials, and billing credits are involved when using the hosted dLazy API.

Mitigation: Use the skill only for intended image-generation work, avoid submitting sensitive local files, and rotate or revoke dLazy API keys from the provider dashboard when needed.

Risk: The skill installs or invokes an npm-distributed CLI, which carries ordinary package supply-chain risk.

Mitigation: Prefer the pinned on-demand npx invocation when possible and review the referenced CLI repository or npm package before global installation.

Risk: Local image paths passed to the CLI may be uploaded to dLazy media storage for model processing.

Mitigation: Confirm files are appropriate to upload before passing them as image inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dLazy CLI invocations and saved image assets through the CLI when requested.]

## Skill Version(s):

1.2.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
