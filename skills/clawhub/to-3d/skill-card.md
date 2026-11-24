## Description:

Turns flat-lay garment photos into dimensional ghost-mannequin style product images while aiming to preserve the garment's color, construction, and details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and product-content teams use the skill to turn a flat-lay garment photo into a ghost-mannequin style product image that shows the garment's shape and volume while preserving visible design details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the release suspicious because user images may be transmitted to external image-generation services, and the scan did not fully inspect every component.

Mitigation: Before use, check which external service will receive each image and avoid sending confidential images unless that transfer is understood and approved; review the skill before installation given the incomplete inspection.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)
- [dLazy](https://dlazy.com)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Generated garment image files, image-generation prompt text, and executable CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are typically JPEG; common output sizes are square or portrait.]

## Skill Version(s):

1.0.35 (source: frontmatter; confirmed by server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
