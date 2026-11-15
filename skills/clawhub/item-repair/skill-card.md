## Description:

Retouches casual product photos for listing use by reducing random wrinkles, aligning presentation, evening lighting, and cleaning the background.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and studio teams can use the skill to prepare product photos for catalogs by retouching layout, random wrinkles, lighting, and backgrounds while preserving product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags broad activation and an incomplete scan, so the skill may run in a wider set of situations than intended.

Mitigation: Confirm the request is for an authorized product-photo edit and check the selected tool and provider before use.

Risk: Prompts and source images may be sent to an external image service.

Mitigation: Avoid sending sensitive images, and check that the chosen provider's data handling is acceptable before uploading.

Risk: Image edits can change product details or conceal defects.

Mitigation: Compare each result with the source; preserve style, color, structural folds, and visible defects.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/item-repair)
- [Model flags](references/model-flags.md)
- [Provider CLI guide](references/provider-cli.md)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [Related material enhancement skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Edited images, Text prompts, Shell commands]

**Output Format:** [Image files with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts 1–4 views of one product; output quality and fidelity depend on the selected image service.]

## Skill Version(s):

1.0.32 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
