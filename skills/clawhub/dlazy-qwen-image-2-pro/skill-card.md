## Description:

This skill lets agents generate images with Alibaba Bailian qwen-image-2.0-pro, including complex text rendering, mixed Chinese and English layouts, photorealistic detail, and semantically faithful designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent call the dLazy qwen-image-2-pro CLI for text-to-image generation, optional image inputs, async generation, and saved image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party npm CLI and a dLazy cloud account.

Mitigation: Use the pinned npx invocation or an isolated environment before choosing a global install.

Risk: Prompts and referenced local media files may be sent to dLazy API and media storage endpoints.

Mitigation: Only pass prompts and media files intended for upload to the service.

Risk: The dLazy API key is stored locally or supplied through DLAZY_API_KEY.

Mitigation: Protect the local config file and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples for generated image URLs or async task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs from files.dlazy.com, a saved local image path when --save is used, or an async generateId for later polling.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
