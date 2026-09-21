## Description:

Extracts a clean e-commerce flat-lay product image from a source photo, such as a model shot, street photo, buyer image, or competitor screenshot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce operators, and developers use this skill to turn existing garment photos into clean white-background flat-lay product assets. It is intended for cases where the user has a worn, styled, or cluttered source image and needs one garment or accessory isolated for product imagery or as input to related visual workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos, prompts, and selected image URLs may be sent to the configured cloud provider.

Mitigation: Use --dry-run or --doctor to confirm the provider before running, and avoid sensitive personal or confidential images unless that provider is approved for the data.

Risk: Generated files may be written somewhere unexpected if the save path is implicit or unclear.

Mitigation: Use explicit --save paths for each run so generated assets land in the intended location.

Risk: Occluded garment areas are reconstructed from model inference rather than directly recovered from the source photo.

Mitigation: Review generated flat-lay images manually, especially around occluded design details, seams, logos, colors, and patterns.

Risk: The workflow could be misused to remove marks or alter product presentation in a way that misrepresents ownership or authenticity.

Mitigation: Use the skill only on images and products the user has rights to use, and do not use it to remove another party's branding to represent goods as your own.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with inline shell commands that generate local image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs typically target 1024x1024 flat-lay image files and may include dry-run or provider-selection commands.]

## Skill Version(s):

1.0.12 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
