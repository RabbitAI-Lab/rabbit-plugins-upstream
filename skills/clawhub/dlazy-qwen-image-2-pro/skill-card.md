## Description:

Alibaba Bailian qwen-image-2.0-pro general image generation for complex text rendering, multi-line layout, photorealistic detail, and strong semantic adherence in mixed Chinese and English image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted qwen-image-2-pro image generation workflow from an agent, supplying prompts and optional reference images to receive generated image URLs or saved image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy's hosted API and media storage.

Mitigation: Do not submit private or sensitive content unless that transfer is intended and approved for the user's environment.

Risk: The skill depends on a third-party npm CLI package.

Mitigation: Use the pinned npx invocation or pinned global install and review package/source provenance before use in sensitive environments.

Risk: The dLazy API key is stored locally or supplied through an environment variable.

Mitigation: Protect the local config and rotate or revoke the organization API key if access is no longer needed or compromise is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON result payload with generated image URLs; optional downloaded image file when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return a generateId for later polling; local media paths passed as inputs may be uploaded to dLazy hosted storage.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
