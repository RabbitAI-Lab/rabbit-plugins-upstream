## Description:

Enhances clothing photos by reconstructing fabric texture and fine surface detail from a high-resolution product reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and e-commerce image teams use the skill to improve fabric texture in an on-model clothing photo with a high-resolution reference of the same product, while aiming to preserve the image's pose, color, and background.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected photos and prompts are sent to the chosen cloud provider.

Mitigation: Choose an explicitly approved provider, avoid confidential photos unless its data handling is suitable, and preview requests with --dry-run.

Risk: Cloud image generation may incur charges, and provider credentials are needed.

Mitigation: Review costs and provider settings before running, and use a trusted CLI release.

Risk: Generated images may be confused with or overwrite source images.

Mitigation: Save results separately from originals and compare them before use.

## Reference(s):

- [Provider CLI setup, data flow, and outputs](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Files, Guidance, Shell commands]

**Output Format:** [Generated image files (typically JPEG) with Markdown guidance and shell-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch runs can produce multiple variants; compare results with the original images before use.]

## Skill Version(s):

1.0.24 (source: SKILL.md frontmatter, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
