## Description:

商品图精修 Item Repair helps agents turn casual product photos into listing-ready retouched images by reducing wrinkles, improving alignment and lighting, cleaning backgrounds, and preserving product structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide product-photo retouching workflows for ecommerce listings, including flat-lay cleanup, garment wrinkle reduction, background purification, lighting correction, and saved image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to the configured cloud provider.

Mitigation: Use only approved providers and avoid processing confidential or sensitive product imagery unless the provider and account are authorized for that data.

Risk: Misconfigured provider selection or custom endpoints can expose images or credentials.

Mitigation: Prefer explicit provider choices, keep credentials scoped and rotated, and use custom endpoints only when they are trusted and controlled.

Risk: The bundled shared generator supports multiple tasks and providers beyond this release's item-repair workflow.

Mitigation: Constrain execution to the item-repair task, review dry-run output before paid calls, and scan commands before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Material enhancement companion skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with bash commands and image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces saved JPEG image files through a configured cloud image provider; JSON status output is available from the bundled generator.]

## Skill Version(s):

1.0.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
