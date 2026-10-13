## Description:

Generates 2K, 3K, or 4K images from text prompts and optional reference images for posters, key visuals, and print projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to generate high-resolution images from prompts or reference images for posters, key visuals, and large-format print.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference files provided to the skill are sent to dLazy for cloud image generation.

Mitigation: Avoid sending sensitive prompts or images; review the files you choose to upload.

Risk: The dLazy API key is saved locally when using the login flow.

Mitigation: Protect the local key and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Image links]

**Output Format:** [JSON with generated image URLs or an asynchronous task ID; images can optionally be saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K, 3K, and 4K resolution and optional reference images.]

## Skill Version(s):

1.2.24 (source: ClawHub release metadata; artifact frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
