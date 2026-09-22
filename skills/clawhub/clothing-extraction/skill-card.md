## Description:

Guides an agent to extract clothing or accessories from source photos and generate clean white-background e-commerce flat-lay product images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce operators, and developers use this skill to turn model shots, buyer photos, or competitor screenshots into product flat-lay images for catalog and creative workflows. It is intended for faithful extraction of visible garments while preserving color, texture, shape, and key construction details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send source images, including people, faces, homes, or private scenes, to a selected cloud image provider.

Mitigation: Use dry-run or provider selection to confirm where data will go, and avoid processing sensitive images unless that transfer is acceptable.

Risk: Generated flat-lay outputs may infer occluded garment areas or produce misleading product images if used to remove branding or alter the represented item.

Mitigation: Review generated images against the source, manually confirm occluded design areas, and do not use the workflow to remove branding or misrepresent goods.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy product information](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash examples and generated image file paths or URLs from CLI execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses single-image inputs for garment extraction, typically generating 1024x1024 flat-lay image files with optional batch variants.]

## Skill Version(s):

1.0.13 (source: server evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
