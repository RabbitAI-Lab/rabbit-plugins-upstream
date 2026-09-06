## Description:

Generates Midjourney-style images through dLazy's hosted CLI, with controls for aspect ratio, bot type, and grid or upscale output selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request stylized image generations from dLazy's cloud service and retrieve generated image URLs or saved assets. It is suited for creative image generation workflows that need Midjourney-style outputs with configurable aspect ratio and output selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly passed media files can be uploaded to dLazy's cloud service.

Mitigation: Use the skill only with content appropriate for cloud processing, and avoid sending sensitive prompts or media unless the user accepts dLazy's service handling.

Risk: A dLazy API key may be saved in the local CLI configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY or the pinned npx command when persistent local configuration is undesirable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install persists an executable on the user's system.

Mitigation: Use the pinned npx form, npx @dlazy/cli@1.2.3, when a non-persistent install path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI homepage from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [JSON responses containing generated image URLs or asynchronous task status, with optional downloaded image files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication; prompts and explicitly provided media files are processed by dLazy's cloud service.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter is 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
