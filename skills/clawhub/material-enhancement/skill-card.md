## Description:

Enhances clothing material texture and reconstructs blurred fabric detail using a source image plus a high-resolution product reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce content creators and developers use this skill to perform a post-processing pass on product or model photos where garment texture is blurred but composition, model pose, color, and background should stay fixed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or model images and prompts may be sent to dLazy or another configured image provider.

Mitigation: Use the skill only when that data sharing is acceptable, review configured provider credentials, and use dry-run mode to inspect requests before generation.

Risk: Generated image files are saved to user-selected output paths.

Mitigation: Choose explicit output paths and review saved files before using them in production catalogs or campaigns.

Risk: Weak prompts or mismatched reference images can change color, silhouette, model details, or background instead of only improving texture.

Mitigation: Confirm the source and reference images show the same product, lock non-garment regions in the prompt, preserve the garment color, and compare outputs against the source image.

Risk: Very low-resolution or structurally broken source images may not contain enough information for reliable texture placement.

Mitigation: Use inputs that meet the documented size, resolution, and format rules, and rerun the upstream generation when garment structure is already incorrect.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameter List](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands and image-generation request parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated JPEG image files through the configured provider; dry-run mode can preview requests before generation.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
