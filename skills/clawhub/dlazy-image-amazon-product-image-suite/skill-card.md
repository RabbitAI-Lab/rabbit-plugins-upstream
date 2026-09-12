## Description:

A professional product image generation skill purpose-built for the Amazon e-commerce platform, covering main product images, secondary gallery images, and A+ Brand Content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and commerce creative teams use this skill to plan and generate Amazon-ready product image sets, including compliant main images, secondary gallery assets, and A+ Brand Content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party npm CLI that runs under the user's account and stores a dLazy API key locally.

Mitigation: Verify the intended CLI version before use, prefer on-demand npx execution where practical, and use short-lived or easily rotated API credentials.

Risk: Prompts and selected media files may be uploaded to dLazy services for generation.

Mitigation: Pass only the files needed for the image task and avoid submitting confidential or unnecessary media.

Risk: Reviewed version and provenance information are inconsistent or unavailable.

Mitigation: Use the server release version for this card, confirm package provenance before deployment, and review the referenced CLI package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with planning notes, image-generation prompts, checklists, CLI commands, and generated image URLs when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a dLazy API key and may upload selected prompts and media files to dLazy services through the dLazy CLI.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
