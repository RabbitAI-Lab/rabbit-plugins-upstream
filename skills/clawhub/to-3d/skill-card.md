## Description:

平铺图转隐形模特立体图。平铺图 → 有体积感与版型的立体展示图。当用户说「转 3D」「立体图」「隐形模特」「把衣服撑起来」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, content teams, and agent-assisted product photography workflows use this skill to convert flat-lay clothing photos into ghost-mannequin product images with visible volume and garment structure. It guides prompt construction, input checks, generation settings, dry runs, saved outputs, and visual quality review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clothing photos and prompts may be sent to dLazy or the selected AI provider during generation.

Mitigation: Use dry-run or doctor modes to confirm the provider before generation, avoid confidential images unless approved for that provider, and prefer local file paths or trusted image URLs.

Risk: Generated images may introduce a visible mannequin or body, change garment proportions, or lose material details.

Mitigation: Use the skill's explicit prompt constraints for no person or support, preserve original color and structure, and review outputs for body artifacts, fit changes, collar depth, and stitch fidelity before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy product site](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown instructions with bash command examples and generated JPEG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run provider checks, one or two reference images, 1:1 or 3:4 generation sizes, quality selection, batch generation, and local save paths.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
