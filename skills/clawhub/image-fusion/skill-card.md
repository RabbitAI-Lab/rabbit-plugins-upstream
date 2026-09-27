## Description:

Combines up to eight apparel or accessory product images into a complete e-commerce look on one model while preserving each item's visible details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Online retail teams and content creators use this skill to turn product photos into consistent model-worn outfit images for storefront and listing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional model or reference images may be sent to the configured cloud provider.

Mitigation: Use dry-run before paid generation, choose the provider deliberately, and avoid sensitive or unauthorized images.

Risk: Generated outfit images can omit items, mix colors, or get clothing layers wrong in multi-item compositions.

Mitigation: Name each item and wearing position explicitly, use batch outputs for selection, and review every saved image before publication.

Risk: Model photos could be misused to imply an unauthorized endorsement.

Mitigation: Use only authorized model imagery and do not use the skill to fabricate a person's likeness or endorsement.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0 model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, command examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce and save generated e-commerce outfit images through configured cloud image providers.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
