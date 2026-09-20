## Description:

平铺图转隐形模特立体图。平铺图 → 有体积感与版型的立体展示图。当用户说「转 3D」「立体图」「隐形模特」「把衣服撑起来」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, product-image teams, and agents use this skill to turn flat-lay garment photos into dimensional ghost-mannequin product images. It guides prompt construction, provider selection, dry-run checks, image generation, local saving, and visual quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may send selected garment images, prompts, and image URLs to dLazy or another configured image-generation provider.

Mitigation: Use dry-run first for request and cost visibility, and avoid private or unreleased product images unless the selected provider's terms allow that use.

Risk: Broad requests such as "3D image" can be ambiguous and may trigger the wrong image-generation workflow.

Mitigation: Confirm the task is specifically flat-lay clothing conversion to a ghost-mannequin style before invoking the skill.

Risk: Generated images may distort garment proportions, fabric structure, labels, or add visible mannequin/body artifacts.

Mitigation: Review outputs against the source garment and rerun with stricter preservation, no-person, and quality-control prompt constraints when defects appear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, CLI/JSON responses, and saved JPEG image files when generation commands are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost/request previews, provider selection, batch image generation, and local output paths.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
